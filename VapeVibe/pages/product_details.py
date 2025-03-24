import reflex as rx
from ..ui.colors import *
from ..ui.nav_bar import nav_bar
from reflex_image_zoom import image_zoom

def product_details() -> rx.Component:
    return rx.box(
        rx.box(nav_bar()),
        rx.vstack(
            #* top bar (оставляем как есть)
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
            #* main content
            rx.container(
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            #* left - image
                            rx.box(
                                image_zoom(
                                    rx.image(
                                        "https://megabuzz.ru/wp-content/uploads/2022/11/52-324x324.png",
                                        border_radius="15px",
                                        box_shadow=f"0 0 20px {BROWN}40",
                                    )  
                                ),
                                padding="20px",
                            ),
                            #* right - product info
                            rx.vstack(
                                # Title
                                rx.heading(
                                    "Jam Monster Grape", 
                                    font_size="40px",
                                    color=BROWN,
                                    margin_bottom="20px",
                                ),
                                # Product details
                                rx.hstack(
                                    rx.text("30ml", color=GRAY, font_size="24px"),
                                    rx.text("|", color=GRAY, margin_x="10px"),
                                    rx.text("20mg", color=GRAY, font_size="24px"),
                                    margin_bottom="30px",
                                ),
                                # Price
                                rx.text(
                                    "10$", 
                                    font_size="40px", 
                                    color=ADDITIONAL_TEXT_COLOR,
                                    margin_bottom="30px",
                                ),
                                # Quantity selector
                                rx.hstack(
                                    rx.button(
                                        rx.icon(tag="minus",size=20),
                                        bg=ADDITIONAL_BACKGROUND,
                                        color=GRAY,
                                        # size="3",
                                    ),
                                    rx.text(
                                        "1",
                                        font_size="24px",
                                        color=GRAY,
                                        margin_x="20px",
                                    ),
                                    rx.button(
                                        rx.icon(tag="plus",size=20),
                                        bg=ADDITIONAL_BACKGROUND,
                                        color=GRAY,
                                        # size="4",
                                    ),
                                    rx.box(rx.text("Amount: 5")),
                                    margin_bottom="30px",
                                    align="center",
                                    align_self="center",
                                ),
                                # Action buttons
                                rx.hstack(
                                    rx.button(
                                        rx.icon(tag="heart", color=RED),
                                        "Like",
                                        bg=ADDITIONAL_BACKGROUND,
                                        color=GRAY,
                                        size="4",
                                        margin_right="10px",
                                    ),
                                    rx.button(
                                        rx.icon(tag="shopping-cart"),
                                        "Add to cart",
                                        bg=BROWN,
                                        color="white",
                                        size="3",
                                    ),
                                ),
                                align_items="start",
                                spacing="3",
                            ),
                            spacing="4",
                        ),
                        justify="center",
                        width="100%",
                    ),
                    margin_top="50px",    
                    margin_bottom="90px",
                    width="100%",
                    bg=BACKGROUND,
                    padding="40px",
                    border_radius="20px",
                    box_shadow=f"0 0 30px {BROWN}20",
                ),
                center_content=True,
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