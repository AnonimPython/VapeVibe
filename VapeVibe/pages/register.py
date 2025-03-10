import reflex as rx


def register() -> rx.Component:
    return rx.mobile_and_tablet(
        rx.heading("REGISTER PAGE"),
    )