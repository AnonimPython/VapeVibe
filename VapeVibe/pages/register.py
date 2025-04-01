import reflex as rx
from sqlmodel import select
from ..ui.colors import *
from ..models import Register

class RegisterState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        
        try:
            if not form_data.get("checkbox"):
                return rx.toast.error("Please confirm you are over 18")

            if form_data["password"] != form_data["confirm_password"]:
                return [
                    rx.set_value("password", ""),
                    rx.set_value("confirm_password", ""),
                    rx.toast.error("Passwords do not match")
                ]
                
            with rx.session() as session:
                # Check existing user in single query
                existing_user = session.exec(
                    select(Register).where(
                        (Register.username == form_data["username"]) | 
                        (Register.email == form_data["email"])
                    )
                ).first()
                
                if existing_user:
                    return rx.toast.error("Username or email already exists")
                    
                # Create new user
                new_user = Register(
                    username=form_data["username"],
                    email=form_data["email"],
                    password=form_data["password"]  # Should hash password in production
                )
                session.add(new_user)
                session.commit()
                
                return rx.redirect("/")
                
        except Exception as e:
            return rx.toast.error(str(e))

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
                                placeholder="Email",
                                name="email",
                                type="email",
                                required=True,
                                style=input_style
                            ),
                            rx.input(
                                placeholder="Username", 
                                name="username",
                                required=True,
                                style=input_style
                            ),
                            rx.input(
                                placeholder="Password",
                                name="password", 
                                type="password",
                                required=True,
                                style=input_style
                            ),
                            rx.input(
                                placeholder="Confirm Password",
                                name="confirm_password",
                                type="password", 
                                required=True,
                                style=input_style
                            ),
                            rx.hstack(
                                rx.checkbox(
                                    name="checkbox",
                                    required=True
                                ),
                                rx.text("I confirm I am over 18 years old")
                            ),
                            rx.button(
                                "Register",
                                type="submit",
                                width="100%"
                            ),
                            spacing="4",
                        ),
                        on_submit=RegisterState.handle_submit,
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