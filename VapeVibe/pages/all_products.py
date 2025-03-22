import reflex as rx
from ..ui.nav_bar import nav_bar
from ..ui.colors import *


class FilterState(rx.State):
    filter1: bool = False 
    filter2: bool = False

    def apply_filters(self):
        pass

def all_products():
    return rx.box(
        rx.box(nav_bar(),),
        rx.vstack(
            #* top bar
            rx.hstack(
                rx.input(
                    rx.input.slot(
                        rx.icon(tag="search"),   
                    ),
                    # padding="20px",
                    height="50px",
                    width="70%",
                ),
                rx.link(
                    rx.icon(tag="heart", color='white', size=30,), 
                    background="transparent",
                    padding="0",
                    align="center",
                    align_self="center",
                ),
                width="100%",
                align="center",
                align_self="center",
                justify="between",
            ),
            #* filter
            rx.box(
                rx.hstack(
                    rx.box(
                        rx.dialog.root(
                            rx.dialog.trigger(
                                rx.button(
                                    rx.icon(tag="filter"),
                                    size="4",
                                    border=f"1px solid {ADDITIONAL_TEXT_COLOR}",
                                    background="transparent",
                                        
                                ),
                            ),
                            rx.dialog.content(
                                rx.dialog.title("Filters"),
                                rx.dialog.description(
                                    "Select filters to apply",
                                ),
                                rx.flex(
                                    rx.checkbox(
                                        "Filter 1",
                                        on_change=FilterState.set_filter1,
                                    ),
                                    rx.checkbox(
                                        "Filter 2", 
                                        on_change=FilterState.set_filter2,
                                    ),
                                    rx.flex(
                                        rx.dialog.close(
                                            rx.button(
                                                "Cancel",
                                                variant="soft",
                                                color_scheme="gray",
                                            ),
                                        ),
                                        rx.dialog.close(
                                            rx.button("Apply"),
                                        ),
                                        spacing="3",
                                        justify="end",
                                    ),
                                    direction="column",
                                    spacing="4",
                                ),
                                max_width="450px",
                            ),
                        ),
                    ),
                    #* popular filters
                    rx.box(
                        rx.scroll_area(
                            rx.flex(
                                *[
                                    rx.button(
                                        "Creamy Milk",
                                        font_size="25px",
                                        background="transparent",
                                        border=f"1px solid {ADDITIONAL_TEXT_COLOR}",
                                        padding="10px",
                                    ) for _ in range(10)
                                ],  #! TEST],
                            ),    
                        ),    
                    ),
                    align="center",
                    align_self="center",
                    padding="10px",
                ),    
            ),
                    
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
    
    )