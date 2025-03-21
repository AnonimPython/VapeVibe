import reflex as rx
from ..ui.colors import *

def nav_bar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.link(
                rx.icon(
                    "home",
                    color="white",
                    size=40,
                ),
                href="/",
            ),
            rx.link(
                rx.icon(
                    "shopping-cart",
                    color="white",
                    size=40,
                ),
                href="/",
            ),
            rx.link(
                rx.icon(
                    "ticket",
                    color="white",
                    size=40,
                ),
                href="/",
            ),
            rx.link(
                rx.icon(
                    "user",
                    color="white",
                    size=40,
                ),
                href="/",
            ),
            spacing="4",
            justify_content="space-around",
            align="center",
            width="100%",
            height="90px",
            padding_y="3",
        ),
        position="fixed",
        bottom="0",
        left="0",
        right="0",
        background=BACKGROUND,
        width="100%",
    )