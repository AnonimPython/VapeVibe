import reflex as rx
from ..ui.colors import *
def login() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                rx.heading("VAPEVIBE", color=ADDITIONAL_TEXT_COLOR, size="9",margin_bottom="10px"),
                rx.text("LOGIN PAGE"),
                text_align="center",
                width="100%",
            ),
            #* inputs
            rx.hstack(
                rx.box(
                    rx.form(
                        rx.input(placeholder="Email", width="100%",style=input_style),
                        rx.input(placeholder="Password", width="100%", margin_top="20px",style=input_style),
                        
                        rx.button(
                            rx.text("Login",font_size="20px",color="white",weight="bold"),
                            width="100%",
                            background=BROWN,
                            margin_top="20px",
                            type="submit",
                        ),
                        # on_submit=FormState.handle_submit,
                        reset_on_submit=True,
                    ),
                    rx.hstack(
                        rx.text("Don't have an account?"),
                        rx.link(
                            "Sing up",
                            href="/register",
                            color=BROWN,
                            font_size="15px",
                            font_weight="bold"
                        ),
                        margin_top="20px",
                    ),
                    
                    
                ),
                
            ),
            
            justify_content="center",
            align_items="center",
            width="100%",
            height="100vh",
            display=rx.breakpoints(
                initial="flex",  # mobile
                sm="flex",      # tablets
                md="flex",      # middle screen
                lg="none"       # big screen < 1366px
            ),
        ),
    )