import reflex as rx
from sqlmodel import select
from typing import List
from ..models import Product, Category

class AdminState(rx.State):
    products: List[Product] = []

    def get_products(self):
        with rx.session() as session:
            self.products = session.exec(select(Product)).all()

    def add_product(self, form_data: dict):
        with rx.session() as session:
            product = Product(
                name=form_data["name"],
                image_url=form_data["image_url"],
                description=form_data["description"],
                price=float(form_data["price"]),
                brand=form_data["brand"],
                category_id=None  # Пока не используем связь с категорией
            )
            session.add(product)
            session.commit()
            self.get_products()

def show_product(product: Product):
    return rx.table.row(
        rx.table.cell(product.name),
        rx.table.cell(rx.image(src=product.image_url, height="50px")),
        rx.table.cell(product.description),
        rx.table.cell(f"${product.price:.2f}"),
        rx.table.cell(product.brand),
    )

def admin_page():
    return rx.vstack(
        rx.heading("Админ панель"),
        
        # Форма добавления продукта
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Название продукта",
                    name="name",
                    required=True
                ),
                rx.input(
                    placeholder="URL изображения",
                    name="image_url",
                    required=True
                ),
                rx.input(
                    placeholder="Описание",
                    name="description"
                ),
                rx.input(
                    placeholder="Цена",
                    type_="number",
                    name="price",
                    required=True
                ),
                rx.input(
                    placeholder="Бренд",
                    name="brand",
                    required=True
                ),
                rx.button("Добавить", type_="submit"),
                spacing="4",
            ),
            on_submit=AdminState.add_product,
            reset_on_submit=True,
        ),

        # Таблица с продуктами
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Название"),
                    rx.table.column_header_cell("Изображение"),
                    rx.table.column_header_cell("Описание"),
                    rx.table.column_header_cell("Цена"),
                    rx.table.column_header_cell("Бренд"),
                )
            ),
            rx.table.body(
                rx.foreach(
                    AdminState.products,
                    show_product
                )
            ),
            variant="surface",
            size="3",
            width="100%"
        ),
        spacing="4",
        width="100%",
        padding="4"
    )