import reflex as rx


def main() -> rx.Component:
    return rx.mobile_and_tablet(
        rx.heading("MAIN PAGE"),
    )