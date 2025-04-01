import reflex as rx
from sqlmodel import select
from ..models import Category

class CategoryState(rx.State):
    """The category state."""
    categories: list[Category] = []
    
    @rx.event
    def load_categories(self) -> list[Category]:
        """Get all categories from the database."""
        with rx.session() as session:
            self.categories = session.exec(select(Category)).all()
    
    @rx.event
    def add_category(self, form_data: dict):
        """Add a category to the database."""
        with rx.session() as session:
            # Check if category with this name already exists
            if session.exec(select(Category).where(
                Category.name == form_data["name"])).first():
                return rx.toast.warning("Category with this name already exists")
            
            new_category = Category(**form_data)
            session.add(new_category)
            session.commit()
            
            # Reload categories after adding new one
            self.load_categories()
            return rx.toast.success(f"Category {form_data['name']} has been added.")

def show_category(category: rx.Var):
    """Show a category in a table row."""
    return rx.table.row(
        rx.table.cell(category.name),
        # Using rx.cond instead of or operator
        rx.table.cell(rx.cond(category.description != "", category.description, "")),
        # rx.table.cell(rx.text(str(category.created_at))),
    )

def categories_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Categories", font_size="2em"),
        
        # Form for adding new categories
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Category Name",
                    name="name",
                    required=True
                ),
                rx.text_area(
                    placeholder="Category Description (optional)",
                    name="description",
                ),
                rx.button("Add Category", type="submit"),
                spacing="4",
            ),
            on_submit=CategoryState.add_category,
            reset_on_submit=True,
        ),
        
        # Table showing existing categories
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Name"),
                    rx.table.column_header_cell("Description"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    CategoryState.categories,
                    show_category
                ),
            ),
            on_mount=CategoryState.load_categories,
            variant="surface",
            size="3",
            width="100%",
        ),
        spacing="8",
        width="100%",
        padding="6",
    )