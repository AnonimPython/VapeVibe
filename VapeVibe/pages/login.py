import reflex as rx
from sqlmodel import select
from ..models import User
from .auth_utils import verify_password
from ..ui.colors import *

class LoginState(rx.State):
    is_authenticated: bool = False
    error_message: str = ""
    user_id: str = rx.Cookie()  
    user_name: str = rx.Cookie()
    user_email: str = rx.Cookie()

    @rx.event
    def handle_submit(self, form_data: dict):
        try:
            with rx.session() as session:
                print("Attempting login with email:", form_data["email"])
                
                user = session.exec(
                    select(User).where(User.email == form_data["email"])
                ).first()
                
                if not user:
                    self.error_message = "Not HAHA 😈"
                    print("User not found")
                    return rx.toast.error(self.error_message)

                if not verify_password(form_data["password"], user.password_hash):
                    self.error_message = "Not HAHA 😈"
                    print("Password verification failed")
                    return rx.toast.error(self.error_message)

                # Convert ID to string before storing in cookie
                self.user_id = int(user.id)  # Convert to string here
                self.user_name = user.username
                self.user_email = user.email

                self.is_authenticated = True
                self.error_message = ""
                print("Login successful! Redirecting...")

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
                                required=True, 
                                width="100%",
                                style=input_style
                            ),
                            rx.input(
                                placeholder="Password",
                                name="password",
                                type="password", 
                                required=True,
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