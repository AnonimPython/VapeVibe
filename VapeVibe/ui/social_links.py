import reflex as rx
from ..ui.colors import *

def social_link(tag="grid-2x2",color="white",href="#") -> rx.Component:
    return rx.link(
    rx.box(
        rx.icon(
            tag=tag,
            size=40,
        ),
        background=ADDITIONAL_BACKGROUND,
        padding="8px",
        display="flex",
        align_items="center",
        justify_content="center",
    ),
        color=color,
        href=href,
    )