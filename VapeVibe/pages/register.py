import reflex as rx
from sqlmodel import select
from ..models import User
from .auth_utils import hash_password
from ..ui.colors import *

class RegisterState(rx.State):
    success_message: str = ""
    error_message: str = ""

    @rx.event
    def handle_submit(self, form_data: dict):
        try:
            #* checkbox 
            if not form_data.get("checkbox"):
                self.error_message = "Only 18+ users! 🚫"
                return rx.toast.error(self.error_message)

            #* password validation
            if len(form_data["password"]) < 8:
                self.error_message = "8 simbols in password or more 👎"
                return rx.toast.error(self.error_message)
                
            if not any(char.isdigit() for char in form_data["password"]):
                self.error_message = "In password write numbers 🔢"
                return rx.toast.error(self.error_message)
                
            if form_data["password"] != form_data["confirm_password"]:
                self.error_message = "Passwords didn't match ❌"
                return [
                    rx.set_value("password", ""),
                    rx.set_value("confirm_password", ""),
                    rx.toast.error(self.error_message)
                ]

            #* check if user exists in database
            with rx.session() as session:
                existing_user = session.exec(
                    select(User).where(
                        (User.username == form_data["username"]) | 
                        (User.email == form_data["email"])
                    )
                ).first()
                
                if existing_user:
                    self.error_message = "Пользователь уже существует 😞"
                    return rx.toast.error(self.error_message)

                # Создание нового пользователя
                new_user = User(
                    username=form_data["username"],
                    email=form_data["email"],
                    password_hash=hash_password(form_data["password"])
                )
                session.add(new_user)
                session.commit()
                session.refresh(new_user)

                self.success_message = "Регистрация успешна! 🔓"
                return [
                    rx.toast.success(self.success_message),
                    rx.redirect("/login")
                ]
            
        except Exception as e:
            self.error_message = f"Ошибка: {str(e)} 😢"
            return rx.toast.error(self.error_message)


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