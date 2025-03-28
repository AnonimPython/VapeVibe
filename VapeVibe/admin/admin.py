import reflex as rx
from pathlib import Path
from sqlmodel import select, Field
from typing import Optional
from ..models import *


class State(rx.State):
    """The app state."""
    images: list[Image] = []
    caption: str = ""
    
    def on_load(self):
        """Load existing images on page load."""
        with rx.session() as session:
            self.images = session.exec(
                select(Image).order_by(Image.created_at.desc())
            ).all()

    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        if not files or not self.caption:
            return rx.window_alert("Пожалуйста, добавьте подпись к изображению")
            
        upload_dir = Path("assets/uploads")
        upload_dir.mkdir(parents=True, exist_ok=True)
        
        for file in files:
            upload_data = await file.read()
            outfile = upload_dir / file.name  # Changed from filename to name
            with open(outfile, "wb") as file_object:
                file_object.write(upload_data)
            
            with rx.session() as session:
                db_image = Image(
                    filename=file.name,  # Changed from filename to name
                    caption=self.caption,
                    path=f"uploads/{file.name}"  # Changed from filename to name
                )
                session.add(db_image)
                session.commit()
                session.refresh(db_image)
                
                self.images = [db_image] + self.images
            self.caption = ""

def image_card(image: rx.Var[Image]):
    return rx.vstack(
        rx.image(
            src=image.path,
            height="200px",
            width="auto",
        ),
        rx.text(image.caption),
        rx.moment(
            image.created_at,
            format="YYYY-MM-DD HH:mm:ss"
        ),
        padding="5",
        border="1px solid #eaeaea",
        border_radius="md",
        width="100%",
    )

def admin_page():
    return rx.vstack(
        rx.vstack(
            rx.heading("Добавить новое изображение"),
            rx.text_area(
                placeholder="Добавьте подпись к изображению...",
                value=State.caption,
                on_change=State.set_caption,
                margin_bottom="5",
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
                id="upload1",
                border="1px dotted rgb(107,99,246)",
                padding="2em",
                accept={
                    "image/png": [".png"],
                    "image/jpeg": [".jpg", ".jpeg"],
                },
                margin_bottom="5",
            ),
            rx.hstack(
                rx.foreach(
                    rx.selected_files("upload1"),
                    rx.text
                )
            ),
            rx.hstack(
                rx.button(
                    "Загрузить",
                    on_click=State.handle_upload(
                        rx.upload_files(upload_id="upload1")
                    ),
                ),
                rx.button(
                    "Очистить",
                    on_click=rx.clear_selected_files("upload1"),
                ),
                spacing="5",
            ),
            padding="2em",
            border="1px solid #eaeaea",
            border_radius="10px",
            width="100%",
            margin_bottom="2em",
        ),
        
        rx.heading("Галерея изображений"),
        rx.vstack(
            rx.foreach(
                State.images,
                image_card
            ),
            spacing="5",
            width="100%",
        ),
        width="100%",
        max_width="800px",
        margin="0 auto",
        padding="2em",
        on_mount=State.on_load,
    )