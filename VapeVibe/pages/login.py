import reflex as rx
from sqlmodel import select
from ..models import User
from .auth_utils import verify_password
from ..ui.colors import *

class LoginState(rx.State):
    is_authenticated: bool = False
    error_message: str = ""

    @rx.event
    def handle_submit(self, form_data: dict):
        try:
            with rx.session() as session:
                user = session.exec(
                    select(User).where(User.email == form_data["email"])
                ).first()
                
                if not user:
                    self.error_message = "Not HAHA 😈"
                    return rx.toast.error(self.error_message)
                
                if not verify_password(form_data["password"], user.password_hash):
                    self.error_message = "Not HAHA 😈"
                    return rx.toast.error(self.error_message)
                
                # Устанавливаем флаг аутентификации
                self.is_authenticated = True
                self.error_message = ""
                
                # Сохраняем пользователя в состоянии
                return [
                    rx.toast.success("Access 🔓"),
                    rx.redirect("/")
                ]
                
        except Exception as e:
            self.error_message = f"Not HAHA: {str(e)} 😈"
            return rx.toast.error(self.error_message)
        
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
                        rx.vstack(
                            rx.input(
                                placeholder="Mail",
                                name="email",
                                width="100%",
                                style=input_style
                            ),
                            rx.input(
                                placeholder="Password", 
                                name="password",
                                width="100%", 
                                style=input_style
                            ),
                            spacing="6"
                        ),
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