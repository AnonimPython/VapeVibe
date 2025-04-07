import reflex as rx
from .models import Product
from sqlmodel import select

class State(rx.State):
    """The app state."""
    products: list[Product] = []

    def on_mount(self):
        """Load products when the page mounts."""
        with rx.session() as session:
            statement = select(Product)
            self.products = session.exec(statement).all()