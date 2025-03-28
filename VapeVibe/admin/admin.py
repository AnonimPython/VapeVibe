import reflex as rx
from pathlib import Path
from sqlmodel import select
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime
from ..models import *

class ProductState(rx.State):
    products: list[Product] = []
    name: str = ""
    description: str = ""
    price: str = "0"
    brand: str = ""
    flavor: str = ""
    device_type: str = ""
    battery: bool = False
    capacity: str = "0"
    nicotine: str = ""
    caption: str = ""
    is_active: bool = True

    @rx.event
    def on_load(self):
        """Load existing products on page load."""
        with rx.session() as session:
            self.products = session.exec(
                select(Product).order_by(Product.created_at.desc())
            ).all()

    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        if not self.name:
            return rx.window_alert("Заполните обязательные поля")
        
        try:
            price = float(self.price)
            capacity = int(self.capacity)
        except ValueError:
            return rx.window_alert("Некорректные числовые значения")

        try:
            with rx.session() as session:
                product = Product(
                    name=self.name,
                    description=self.description or None,
                    price=price,
                    brand=self.brand,
                    flavor=self.flavor,
                    device_type=self.device_type,
                    battery=self.battery,
                    capacity=capacity,
                    nicotine=self.nicotine or None,
                    is_active=self.is_active,
                    images=[]
                )
                session.add(product)
                session.commit()
                session.refresh(product)

                if files:
                    images = []
                    for file in files:
                        upload_data = await file.read()
                        outfile = rx.get_upload_dir() / file.filename
                        
                        with outfile.open("wb") as file_object:
                            file_object.write(upload_data)
                        
                        db_image = Image(
                            filename=file.filename,
                            caption=self.caption,
                            path=file.filename
                        )
                        session.add(db_image)
                        session.commit()
                        session.refresh(db_image)
                        
                        images.append({
                            "id": str(db_image.id),
                            "filename": db_image.filename,
                            "path": file.filename,
                            "caption": db_image.caption,
                            "created_at": db_image.created_at.isoformat()
                        })
                    
                    product.images = images
                    session.add(product)
                    session.commit()
                    session.refresh(product)

                # Update products list immediately
                self.products = [product] + [p for p in self.products if p.id != product.id]

            self.reset_fields()
            return rx.window_alert("Товар успешно добавлен!")
            
        except Exception as e:
            print("Error:", e)
            return rx.window_alert(f"Ошибка при сохранении: {str(e)}")

    def reset_fields(self):
        self.name = ""
        self.description = ""
        self.price = "0"
        self.brand = ""
        self.flavor = ""
        self.device_type = ""
        self.battery = False
        self.capacity = "0"
        self.nicotine = ""
        self.caption = ""

def product_card(product: Product):
    return rx.vstack(
        rx.foreach(
            product.images,
            lambda img: rx.vstack(
                rx.image(
                    src=rx.get_upload_url(img['path']),
                    height="200px",
                    width="auto",
                ),
                rx.text(img["caption"]),
                spacing="2"
            )
        ),
        rx.heading(product.name),
        rx.text(product.description),
        rx.text(f"Цена: {product.price} ₽"),
        rx.text(f"Бренд: {product.brand}"),
        rx.moment(product.created_at, format="DD.MM.YYYY HH:mm"),
        padding="1em",
        border="1px solid red",
        border_radius="",
        width="100%",
        box_shadow="sm"
    )

def admin_page():
    return rx.vstack(
        rx.box(
            rx.vstack(
                rx.heading("Добавить новый товар", size="4"),
                rx.vstack(
                    rx.input(
                        placeholder="Название товара*",
                        value=ProductState.name,
                        on_change=ProductState.set_name,
                        required=True
                    ),
                    rx.text_area(
                        placeholder="Описание товара",
                        value=ProductState.description,
                        on_change=ProductState.set_description
                    ),
                    rx.hstack(
                        rx.input(
                            placeholder="Цена*",
                            type_="number", 
                            value=ProductState.price,
                            on_change=ProductState.set_price,
                            width="48%"
                        ),
                        rx.input(
                            placeholder="Емкость (мл)*",
                            type_="number",
                            value=ProductState.capacity,
                            on_change=ProductState.set_capacity,
                            width="48%"
                        ),
                        width="100%"
                    ),
                    rx.hstack(
                        rx.input(
                            placeholder="Бренд*",
                            value=ProductState.brand,
                            on_change=ProductState.set_brand,
                            width="48%"
                        ),
                        rx.input(
                            placeholder="Вкус",
                            value=ProductState.flavor,
                            on_change=ProductState.set_flavor,
                            width="48%"
                        ),
                        width="100%"
                    ),
                    rx.input(
                        placeholder="Тип устройства",
                        value=ProductState.device_type,
                        on_change=ProductState.set_device_type
                    ),
                    rx.hstack(
                        rx.checkbox(
                            "Батарея в комплекте",
                            checked=ProductState.battery,
                            on_change=ProductState.set_battery
                        ),
                        rx.checkbox(
                            "Активный товар",
                            checked=ProductState.is_active,
                            on_change=ProductState.set_is_active
                        ),
                        spacing="4"
                    ),
                    rx.input(
                        placeholder="Никотин (мг/мл)",
                        value=ProductState.nicotine,
                        on_change=ProductState.set_nicotine
                    ),
                    rx.text_area(
                        placeholder="Подпись для изображений",
                        value=ProductState.caption,
                        on_change=ProductState.set_caption
                    ),
                    rx.upload(
                        rx.vstack(
                            rx.button(
                                "Выберите файл",
                                color="rgb(107,99,246)",
                                bg="white",
                                border="1px solid rgb(107,99,246)",
                            ),
                            rx.text(
                                "Перетащите файлы сюда или нажмите для выбора"
                            ),
                        ),
                        border="1px dotted rgb(107,99,246)",
                        padding="2em",
                        multiple=True,
                        accept={
                            "image/png": [".png"],
                            "image/jpeg": [".jpg", ".jpeg"],
                        },
                        id="product_upload"
                    ),
                    rx.hstack(
                        rx.foreach(
                            rx.selected_files("product_upload"),
                            rx.text
                        )
                    ),
                    rx.hstack(
                        rx.button(
                            "Сохранить",
                            on_click=ProductState.handle_upload(
                                rx.upload_files(upload_id="product_upload")
                            ),
                            color_scheme="green"
                        ),
                        rx.button(
                            "Очистить",
                            on_click=rx.clear_selected_files("product_upload"),
                            variant="outline"
                        ),
                        spacing="3"
                    ),
                    spacing="4",
                    width="100%"
                ),
                width="100%",
                max_width="800px",
                padding="2em",
                bg="black",
                border_radius="4"
            ),
            width="100%",
            padding="2em",
            bg="#f8f9fa"
        ),
        rx.vstack(
            rx.heading("Список товаров", size="4"),
            rx.foreach(
                ProductState.products,
                lambda product: product_card(product)
            ),
            spacing="4",
            width="100%",
            max_width="1200px",
            padding="2em"
        ),
        on_mount=ProductState.on_load,
        width="100%"
    )