'''
 ▗▄▖ ▗▖  ▗▖ ▗▄▖ ▗▖  ▗▖▗▄▄▄▖▗▖  ▗▖▗▄▄▖ ▗▖  ▗▖▗▄▄▄▖▗▖ ▗▖ ▗▄▖ ▗▖  ▗▖
▐▌ ▐▌▐▛▚▖▐▌▐▌ ▐▌▐▛▚▖▐▌  █  ▐▛▚▞▜▌▐▌ ▐▌ ▝▚▞▘   █  ▐▌ ▐▌▐▌ ▐▌▐▛▚▖▐▌
▐▛▀▜▌▐▌ ▝▜▌▐▌ ▐▌▐▌ ▝▜▌  █  ▐▌  ▐▌▐▛▀▘   ▐▌    █  ▐▛▀▜▌▐▌ ▐▌▐▌ ▝▜▌
▐▌ ▐▌▐▌  ▐▌▝▚▄▞▘▐▌  ▐▌▗▄█▄▖▐▌  ▐▌▐▌     ▐▌    █  ▐▌ ▐▌▝▚▄▞▘▐▌  ▐▌
'''
import reflex as rx
from rxconfig import config
from .ui.colors import *
#* USER PAGES
from .pages.main import main
from .pages.login import login
from .pages.register import register
from .pages.all_products import all_products
from .pages.product_details import product_details
from .pages.error_404 import error_404



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
        "breakpoints": ["640px", "768px", "1024px","1367px"],
        "font_family": "Montserrat, sans-serif",
        "height": "100vh",
        "width": "100%",
        "background": BACKGROUND,
    }
)
# app.add_page(index)
#* USER PAGES
app.add_page(main, route="/")
app.add_page(login, route="/login")
app.add_page(register, route="/register")
app.add_page(all_products, route="/all")
# app.add_page(product_details, route="/product/[product_id]") 
app.add_page(product_details, route="/product/") 

app.add_page(
    error_404,
    route="/404",
    title="404 - Page not found",
)
#* ADMIN PAGES