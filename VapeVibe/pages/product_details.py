import reflex as rx
from ..ui.colors import *
from ..ui.nav_bar import nav_bar
from reflex_image_zoom import image_zoom

def product_details() -> rx.Component:
    return rx.box(
        rx.box(nav_bar()),
        rx.vstack(
            #* top bar
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
                        #* image
                        rx.box(
                            image_zoom(
                                rx.image(
                                    "https://megabuzz.ru/wp-content/uploads/2022/11/52-324x324.png",
                                    border_radius="15px",
                                    box_shadow=f"0 0 20px {BROWN}40",
                                    width="100%"
                                )  
                            ),
                            padding="20px",
                            align_self="center",
                        ),
                        #* product info
                        rx.vstack(
                            # Title
                            rx.heading(
                                "Jam Monster Grape", 
                                font_size=rx.breakpoints(
                                    initial="20px",
                                    sm="30px",
                                    md="40px",
                                ),
                                color=BROWN,
                                margin_bottom="20px",
                                text_align="center",
                            ),
                            # Product details
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
                            # Price
                            rx.text(
                                "10$", 
                                font_size=rx.breakpoints(
                                    initial="30px",
                                    sm="35px",
                                    md="40px",
                                ), 
                                color=ADDITIONAL_TEXT_COLOR,
                                margin_bottom="30px",
                                text_align="center",
                            ),
                            # Quantity selector
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
                                # width="100%",
                            ),
                            # Action buttons
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