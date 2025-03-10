import reflex as rx
from rxconfig import config

#* USER PAGES
from .pages.main import main
from .pages.login import login
from .pages.register import register


app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
    ),
    #* font
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap"
    ],
    #* global styles
    style={
        "font_family": "Montserrat sans-serif;",
        # "background_color": BACKGROUND,
        "height": "100%",
        "width": "100%",
    }
)
# app.add_page(index)
app.add_page(main, route="/")
app.add_page(login, route="/register")
app.add_page(register, route="/login")
