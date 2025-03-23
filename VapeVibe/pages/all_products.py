import reflex as rx
from ..ui.colors import *
from ..ui.social_links import social_link
from ..ui.nav_bar import nav_bar


class FilterState(rx.State):
    filter1: bool = False 
    filter2: bool = False

    def apply_filters(self):
        pass

def all_products() -> rx.Component:
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
                rx.box(
                    rx.hstack(
                        rx.link(
                    rx.icon(tag="heart", color='white', size=30,), 
                    background="transparent",
                    padding="0",
                    align="center",
                    align_self="center",
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
                    
                        width="100%",
                        align="center",
                        align_self="center",
                        padding="10px",
                        ),    
                        ),    
                    ),    
                ),
                width="100%",
                align="center",
                align_self="center",
                justify="between",
            ),
            #* navigation bar
            rx.box(nav_bar(),),
            #* popular filters
            rx.box(
                rx.scroll_area(
                    rx.flex(
                        *[rx.button("Creamy Milk", font_size="25px", background="transparent") for _ in range(10)],  #! TEST],

                        direction="row",
                        spacing="4",
                        wrap="nowrap",
                        min_width="max-content",
                        width="100%",
                    ),
                    scrollbars="horizontal",
                    type="hover",
                    width="100%",
                    height="auto",
                    style={
                        "overflowX": "auto",
                        "whiteSpace": "nowrap",
                    }
                ),
                width="100%",
                overflow="hidden",
            ),
            rx.box(
                rx.flex(
                    *[rx.box(
                        rx.hstack(
                            rx.image(
                                src="https://megabuzz.ru/wp-content/uploads/2022/11/52-324x324.png",
                                width="100px",
                                height="100px", 
                                object_fit="cover",
                                border_radius="8px"
                            ),
                            rx.vstack(
                                rx.text(
                                    "Creamy Milk",
                                    font_size="20px",
                                    color=GRAY
                                ),
                                rx.text(
                                    "10$",
                                    font_size="20px",
                                    color=BROWN,
                                    font_weight="bold"
                                ),
                                spacing="1",
                                align_items="start",
                                flex="1",
                            ),
                            rx.button(
                                rx.icon(
                                    tag="heart",
                                    color="red",
                                    size=30,
                                ),
                                background="transparent", 
                                padding="0",
                                align="center",
                                align_self="center",
                            ),
                            spacing="3",
                            width="100%",
                            padding="10px",
                        ),
                        border="1px solid #202020",
                        border_radius="12px",
                        min_width="300px",
                        flex="1 1 300px",
                        margin=rx.breakpoints(
                            initial="0",
                            sm="5px", 
                            md="10px",
                        ),
                    ) for _ in range(40)], #! TEST
                    wrap="wrap",
                    justify="center", 
                    gap="10px",
                    padding=rx.breakpoints(
                        initial="0",
                        sm="10px",
                        md="20px",
                    ),
                    width="100%",
                ),
                width="100%",
                margin_top="50px",
                margin_bottom="90px",
                
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