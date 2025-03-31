import reflex as rx
from sqlmodel import select
from datetime import datetime
from uuid import UUID
from ..models import *

class CategoryState(rx.State):
    categories: list[Category] = []
    new_category_name: str = ""
    new_category_description: str = ""

    @rx.event  # Добавляем декоратор
    def on_load(self):
        """Load existing categories."""
        with rx.session() as session:
            self.categories = session.exec(
                select(Category).order_by(Category.created_at.desc())
            ).all()
            # Добавляем refresh для избежания stale object exceptions
            for category in self.categories:
                session.refresh(category)

    @rx.event  # Добавляем декоратор 
    def add_category(self):
        if not self.new_category_name:
            return rx.window_alert("Введите название категории")
        
        try:
            with rx.session() as session:
                # Проверяем существование категории
                existing = session.exec(
                    select(Category).where(Category.name == self.new_category_name)
                ).first()
                
                if existing:
                    return rx.window_alert("Категория с таким названием уже существует")

                new_category = Category(
                    name=self.new_category_name,
                    description=self.new_category_description or None
                )
                session.add(new_category)
                session.commit()
                session.refresh(new_category)
                
                # Обновляем список после успешного добавления
                self.categories = session.exec(
                    select(Category).order_by(Category.created_at.desc())
                ).all()
                
                self.new_category_name = ""
                self.new_category_description = ""
                
            return rx.window_alert("Категория успешно добавлена!")
        except Exception as e:
            print("Error adding category:", e)
            return rx.window_alert(f"Ошибка при добавлении категории: {str(e)}")

def category_card(category: Category):
    return rx.vstack(
        rx.heading(category.name, size="5"),
        rx.text(
            rx.cond(
                category.description,
                category.description,
                "Без описания"
            )
        ),
        rx.moment(
            category.created_at,
            format="YYYY-MM-DD HH:mm"
        ),
        padding="1em",
        border="1px solid #eaeaea", 
        border_radius="md",
        width="100%"
    )

def categories_page():
    return rx.vstack(
        rx.vstack(
            rx.heading("Добавить новую категорию"),
            rx.form(
                rx.vstack(
                    rx.input(
                        placeholder="Название категории*",
                        value=CategoryState.new_category_name,
                        on_change=CategoryState.set_new_category_name,
                        required=True
                    ),
                    rx.text_area(
                        placeholder="Описание категории",
                        value=CategoryState.new_category_description,
                        on_change=CategoryState.set_new_category_description
                    ),
                    rx.button(
                        "Сохранить категорию",
                        type_="submit",
                        color_scheme="green"
                    ),
                    spacing="3"
                ),
                on_submit=CategoryState.add_category
            ),
            padding="2em",
            border="1px solid #eaeaea",
            border_radius="10px",
            width="100%",
            max_width="600px"
        ),
        
        rx.heading("Существующие категории"),
        rx.vstack(
            rx.foreach(
                CategoryState.categories,
                lambda category: category_card(category)
            ),
            spacing="3",
            width="100%"
        ),
        on_mount=CategoryState.on_load,
        spacing="5",
        padding="2em",
        width="100%",
        max_width="1200px"
    )
