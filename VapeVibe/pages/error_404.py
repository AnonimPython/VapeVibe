import reflex as rx


def error_404() -> rx.Component:
    return rx.box(
        rx.text("404 - Page not found"),
    )