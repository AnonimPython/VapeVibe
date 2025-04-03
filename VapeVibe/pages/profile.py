import reflex as rx
from ..ui.nav_bar import nav_bar
from ..ui.colors import *
from .login import LoginState

def profile() -> rx.Component:
    return rx.box(
        rx.box(nav_bar()),
        rx.vstack(
            rx.vstack(
                #* profile photo
                rx.image(
                    "https://img.freepik.com/free-photo/headshot-angry-man-frowning-looking-disappointed-bothered-standing-blue-background_1258-65789.jpg?t=st=1742851813~exp=1742855413~hmac=be24ab42dd7169cb4fa9e5b761cadf005d44664873c233f9a1695282fbaff68e&w=2000",
                    width="200px",
                    height="200px", 
                    border_radius="50%",
                    object_fit="cover",
                ),
                #* profile info
                rx.vstack(
                    rx.hstack(
                        # Use the username from cookies
                        rx.text(LoginState.user_name, font_size="30px"),
                        justify="center",
                        spacing="3",
                    ),
                    # Use the email from cookies
                    rx.heading(
                        LoginState.user_email,
                        font_size="20px",
                    ),
                    #* cart
                    rx.box(
                        rx.button(
                            rx.icon(tag="shopping-cart"),
                            bg=BROWN,
                            size="3",
                            height="50px",
                        ),
                        rx.button(
                            rx.icon(tag="heart", color=RED),
                            bg=ADDITIONAL_BACKGROUND,
                            border=f"1px solid {BROWN}",
                            color=GRAY,
                            size="3",
                            height="50px",
                            margin_left="10px",
                        ),
                    ),
                    spacing="3",
                    align_items="center",
                ),
                spacing="8",
                align_items="center",
                width="100%",
            ),  
            align="center",
            width="100%",
        ),
        display=rx.breakpoints(
            initial="block",
            sm="block", 
            md="block",
            lg="none"       
        ),
        height="100vh",   
        padding=rx.breakpoints(
            initial="30px",
            sm="40px",
            md="40px",      
        ),
        bg=BACKGROUND,
    )