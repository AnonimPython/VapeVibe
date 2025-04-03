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
                # 1. Добавляем отладочный вывод
                print("Attempting login with email:", form_data["email"])
                
                user = session.exec(
                    select(User).where(User.email == form_data["email"])
                ).first()
                
                if not user:
                    self.error_message = "Not HAHA 😈"
                    print("User not found")
                    return rx.toast.error(self.error_message)
                
                # 2. Проверяем хэш пароля
                print(f"Stored hash: {user.password_hash}")
                print(f"Input password: {form_data['password']}")
                
                if not verify_password(form_data["password"], user.password_hash):
                    self.error_message = "Not HAHA 😈"
                    print("Password verification failed")
                    return rx.toast.error(self.error_message)
                
                # 3. Явно обновляем состояние
                self.is_authenticated = True
                self.error_message = ""
                print("Login successful! Redirecting...")
                
                # 4. Исправляем возвращаемое значение
                return rx.redirect("/")
                
        except Exception as e:
            self.error_message = f"Not HAHA: {str(e)} 😈"
            print("Error:", str(e))
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
                                required=True,  # Add this
                                width="100%",
                                style=input_style
                            ),
                            rx.input(
                                placeholder="Password",
                                name="password",
                                type="password",  # Add this for password field
                                required=True,  # Add this 
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
                        on_submit=LoginState.handle_submit,
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