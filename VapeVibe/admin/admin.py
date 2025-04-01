# import reflex as rx
# from pathlib import Path
# from datetime import datetime
# from sqlmodel import select, Field
# from ..models import Product, Image

# class AdminState(rx.State):
#     """Состояние админ-панели."""
#     products: list[Product] = []
#     caption: str = ""
#     selected_files: list = []  # Add this line to track selected files
    
#     def on_load(self):
#         """Загрузка существующих продуктов при загрузке страницы."""
#         with rx.session() as session:
#             self.products = session.exec(
#                 select(Product).order_by(Product.created_at.desc())
#             ).all()

#     @rx.event
#     async def handle_upload_and_save(self, form_data: dict):
#         """Добавление нового продукта и его изображений."""
#         files = await rx.upload_files(upload_id="upload1")
#         if not files:
#             return rx.window_alert("Пожалуйста, добавьте хотя бы одно изображение")
            
#         upload_dir = Path("assets/uploads")
#         upload_dir.mkdir(parents=True, exist_ok=True)

#         with rx.session() as session:
#             # Create product first
#             product = Product(
#                 name=form_data["name"],
#                 description=form_data["description"],
#                 price=float(form_data["price"]),
#                 brand=form_data["brand"],
#             )
#             session.add(product)
#             session.commit()
#             session.refresh(product)
            
#             # Then save images
#             for file in files:
#                 upload_data = await file.read()
#                 outfile = upload_dir / file.filename
#                 with open(outfile, "wb") as file_object:
#                     file_object.write(upload_data)
                
#                 image = Image(
#                     filename=file.filename,
#                     path=f"uploads/{file.filename}",
#                     product_id=product.id
#                 )
#                 session.add(image)
            
#             session.commit()
#             self.products = [product] + self.products
#             # Clear selected files after successful upload
#             self.selected_files = []

# def product_form():
#     return rx.form(
#         rx.vstack(
#             rx.input(
#                 placeholder="Название продукта",
#                 name="name",
#                 required=True
#             ),
#             rx.text_area(
#                 placeholder="Описание продукта",
#                 name="description"
#             ),
#             rx.input(
#                 type_="number",
#                 placeholder="Цена",
#                 name="price",
#                 required=True
#             ),
#             rx.input(
#                 placeholder="Бренд",
#                 name="brand",
#                 required=True
#             ),
#             rx.vstack(
#                 rx.upload(
#                     rx.vstack(
#                         rx.button(
#                             "Выберите файл",
#                             color="rgb(107,99,246)",
#                             bg="white",
#                             border="1px solid rgb(107,99,246)",
#                         ),
#                         rx.text(
#                             "Перетащите файлы сюда или нажмите для выбора"
#                         ),
#                     ),
#                     id="upload1",
#                     border="1px dotted rgb(107,99,246)",
#                     padding="2em",
#                     accept={
#                         "image/png": [".png"],
#                         "image/jpeg": [".jpg", ".jpeg"],
#                     },
#                     multiple=True,  # Add this line to allow multiple files
#                 ),
#                 rx.text(
#                     rx.foreach(
#                         rx.selected_files("upload1"),
#                         lambda x: rx.text(x)
#                     )
#                 ),
#             ),
#             rx.button("Добавить продукт", type="submit"),
#             spacing="4",
#         ),
#         on_submit=AdminState.handle_upload_and_save,
#         reset_on_submit=True,
#     )

# def product_card(product: Product):
#     return rx.vstack(
#         rx.heading(product.name, size="4"),
#         rx.text(product.description),
#         rx.text(f"Цена: {product.price}"),
#         rx.text(f"Бренд: {product.brand}"),
#         # Check if product.images exists before mapping
#         rx.cond(
#             product.images is not None,
#             rx.foreach(
#                 product.images,
#                 lambda image: rx.image(
#                     src=f"/uploads/{image.filename}",
#                     height="200px",
#                     width="auto"
#                 )
#             ),
#         ),
#         padding="4",
#         border="1px solid #eaeaea",
#         border_radius="lg",
#     )

# def admin_page():
#     return rx.vstack(
#         rx.heading("Админ панель", size="5"),
#         rx.divider(),
#         rx.heading("Добавить новый продукт", size="4"),
#         product_form(),
#         rx.divider(),
#         rx.heading("Существующие продукты", size="4"),
#         rx.foreach(
#             AdminState.products,
#             product_card
#         ),
#         width="100%",
#         max_width="800px",
#         margin="0 auto",
#         padding="2em",
#         spacing="4",
#         on_mount=AdminState.on_load
#     )
