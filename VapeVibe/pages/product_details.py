import reflex as rx
from typing import Optional
from ..ui.colors import *
from ..ui.nav_bar import nav_bar
from reflex_image_zoom import image_zoom
from ..models import Product
from sqlmodel import select

class ProductDetailState(rx.State):
    """State for product details."""
    product: Optional[Product] = None
    
    @rx.var
    def get_product(self) -> Optional[Product]:
        """Get product from URL param."""
        product_id = self.router.page.params.get("product_id", None)
        if product_id:
            with rx.session() as session:
                return session.get(Product, int(product_id))
        return None

def product_details() -> rx.Component:
    return rx.box(
        rx.box(nav_bar()),
        rx.vstack(
            rx.hstack(
                rx.input(
                    rx.input.slot(
                        rx.icon(tag="search"),   
                    ),
                    height="50px",
                    width="70%",
                ),
                rx.box(
                    rx.hstack(
                        rx.link(
                            rx.icon(tag="heart", color='white', size=30,), 
                            background="transparent",
                            padding="0",
                            align="center",
                            align_self="center",
                        ),  
                    ),    
                ),
                width="100%",
                align="center",
                align_self="center",
                justify="between",
            ),
            rx.container(
                rx.cond(
                    ProductDetailState.get_product,
                    rx.box(
                        rx.vstack(
                            rx.box(
                                image_zoom(
                                    rx.image(
                                        src=ProductDetailState.get_product.image_url,
                                        border_radius="15px",
                                        box_shadow=f"0 0 20px {BROWN}40",
                                        width="100%"
                                    )  
                                ),
                                padding="20px",
                                align_self="center",
                            ),
                            rx.vstack(
                                rx.heading(
                                    ProductDetailState.get_product.name,
                                    font_size=rx.breakpoints(
                                        initial="20px",
                                        sm="30px",
                                        md="40px",
                                    ),
                                    color=BROWN,
                                    margin_bottom="20px",
                                    text_align="center",
                                ),
                                rx.heading(
                                    ProductDetailState.get_product.description,
                                    font_size=rx.breakpoints(
                                        initial="10px",
                                        sm="10px",
                                        md="20px",
                                    ),
                                    color=GRAY,
                                    margin_bottom="20px",
                                    text_align="center",
                                ),
                                rx.hstack(
                                    rx.text(
                                        "30ml", 
                                        color=GRAY, 
                                        font_size=rx.breakpoints(
                                            initial="18px",
                                            sm="20px",
                                            md="24px",
                                        ),
                                    ),
                                    rx.icon(tag="arrow-right-left", color=GRAY, margin_x="10px"),
                                    rx.text(
                                        "20mg", 
                                        color=GRAY, 
                                        font_size=rx.breakpoints(
                                            initial="18px",
                                            sm="20px",
                                            md="24px",
                                        ),
                                    ),
                                    margin_bottom="30px",
                                    justify="center",
                                    width="100%",
                                    align="center",
                                    align_self="center",
                                ),
                                rx.text(
                                    f"{ProductDetailState.get_product.price}$",
                                    font_size=rx.breakpoints(
                                        initial="30px",
                                        sm="35px",
                                        md="40px",
                                    ), 
                                    color=ADDITIONAL_TEXT_COLOR,
                                    margin_bottom="30px",
                                    text_align="center",
                                ),
                                rx.hstack(
                                    rx.box(
                                        rx.text(
                                            "Amount: 5",
                                            font_size=rx.breakpoints(
                                                initial="16px",
                                                sm="18px",
                                                md="20px",
                                            ),
                                        )
                                    ),
                                    margin_bottom="30px",
                                    justify="center",
                                ),
                                rx.flex(
                                    rx.button(
                                        rx.icon(tag="heart", color=RED),
                                        "Like",
                                        bg=ADDITIONAL_BACKGROUND,
                                        color=GRAY,
                                        size="4",
                                        width=rx.breakpoints(
                                            initial="100%",
                                            sm="48%",
                                            md="48%",
                                        ),
                                        height="50px",
                                        margin_bottom=rx.breakpoints(
                                            initial="10px",
                                            sm="0",
                                        ),
                                    ),
                                    rx.button(
                                        rx.icon(tag="shopping-cart"),
                                        "Add to cart",
                                        bg=BROWN,
                                        color="white", 
                                        size="3",
                                        width=rx.breakpoints(
                                            initial="100%",
                                            sm="48%",
                                            md="48%",
                                        ),
                                        height="50px",
                                    ),
                                    flex_direction=rx.breakpoints(
                                        initial="column",
                                        sm="row",
                                    ),
                                    justify="between",
                                    width="100%",
                                    spacing="4",
                                ),
                                align_items="center",
                                width="100%",
                                spacing="3",
                            ),
                            spacing="4",
                            width="100%",
                        ),
                        margin_top="50px",    
                        margin_bottom="90px",
                        bg=BACKGROUND,
                        padding=rx.breakpoints(
                            initial="20px",
                            sm="30px",
                            md="40px",
                        ),
                        border_radius="20px",
                        box_shadow=f"0 0 30px {BROWN}20",
                    ),
                    rx.center(
                        rx.heading("Loading...", size="5"),
                    ),
                ),
                center_content=True,
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
        ),
        bg=BACKGROUND,
    )