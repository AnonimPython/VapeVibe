import reflex as rx
from ..ui.colors import *

class RegisterState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        print(form_data)
        self.form_data = form_data

def register() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                rx.heading("VAPEVIBE", color=ADDITIONAL_TEXT_COLOR, size="9",margin_bottom="10px"),
                rx.text("REGISTER PAGE"),
                text_align="center",
                width="100%",
            ),
            #* inputs
            rx.hstack(
                rx.box(
                    rx.form(
                        rx.vstack(
                            rx.input(
                                placeholder="Mail",
                                name="mail",
                                width="100%",
                                style=input_style
                            ),
                            rx.input(
                                placeholder="Name",
                                name="username",
                                width="100%",
                                style=input_style
                            ),
                            rx.input(
                                placeholder="Password", 
                                name="password",
                                width="100%", 
                                style=input_style
                            ),
                            rx.input(
                                placeholder="Confirm Password", 
                                name="confirm_password",
                                width="100%", 
                                style=input_style
                            ),
                            spacing="6"
                        ),
                        rx.button(
                            rx.text("Register",font_size="20px",color="white",weight="bold"),
                            width="100%",
                            height="50px",
                            background=BROWN,
                            margin_top="20px",
                            type="submit",
                        ),
                        rx.hstack(
                            rx.checkbox(
                                name="checkbox",
                                size="3",
                            ),
                            rx.text("Confirm that you are over 18 years old."),
                            width="100%",
                            margin_top="20px",
                            align="center",
                            align_self="center",
                        ),
                        # on_submit=FormState.handle_submit,
                        reset_on_submit=True,
                    ),
                    rx.hstack(
                        rx.text("Have an account?"),
                        rx.link(
                            "Log in",
                            href="/login",
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