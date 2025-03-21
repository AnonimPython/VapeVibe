import reflex as rx
from ..ui.colors import *
from ..ui.social_links import social_link
from ..ui.nav_bar import nav_bar


def main() -> rx.Component:
    return rx.box(
    #* header
        rx.center(
            rx.vstack(
                rx.hstack(
                    rx.box(
                        #* logo
                        rx.image(src="https://img.freepik.com/free-vector/vape-shop-neon-sign-e-cigarette-with-smoke-cloud-night-bright-advertisement_1262-11928.jpg?t=st=1741911322~exp=1741914922~hmac=9622d76fa0654e740730bde6ec8681a0f15ae431cf4e8e5951819de186d52957&w=1380"),
                        width=rx.breakpoints(
                            initial="60px",
                            sm="100px",
                            md="100px",      
                        ),
                        height="100%",
                    ),
                    rx.spacer(),
                    #* social links
                    rx.box(
                        rx.hstack(
                            social_link(tag="youtube"),
                            social_link(tag="facebook"),
                            social_link(tag="instagram"),
                            
                            spacing="5",
                        ),
                    ),
                    justify="between",
                    width="100%",
                    align="center",
                    align_self="center",
                ),
                
                width="100%",  
                align_items="center",  
            ),
            #! indicators
            style={
                "@media screen and (max-width:1024px)": {
                    "background": "red", 
                },
                "@media screen and (max-width:1080px)": {
                    "background": "yellow", 
                },
                "@media screen and (max-width:640px)": {
                    "background": "blue",
                },
            },   
            # margin="40px",  
        ),
        #* main content
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.text(
                        "one stop shop for the",
                        font_size=rx.breakpoints(
                            initial="30px",
                            sm="40px",
                            md="40px",
                        ),
                        margin_bottom="5px",
                    ),
                    rx.heading(
                        "Vapeing World",
                        font_size=rx.breakpoints(
                            initial="30px",
                            sm="40px",
                            md="40px",
                        ),
                    ),    
                ),
                rx.box(
                    social_link("search",blank=False),    
                ),

                margin_top="50px",
                justify="between",
                width="100%",
                    padding_left=rx.breakpoints(
                    sm="20px",
                    md="120px",
                ),
            ),
            #* scroll area with filter buttons
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
                margin_top="50px",
                width="100%",
                overflow="hidden",
            ),
            #* scroll area with product
            rx.box(
                rx.scroll_area(
                    rx.flex(
                        *[rx.link(
                            rx.vstack(
                                rx.image(
                                    src="https://static.insales-cdn.com/r/9l1M24o5xE0/rs:fit:1000:0:1/q:100/plain/images/products/1/5370/612308218/Vaporesso-Xros-Mini-1000mAh-MTL-Pod-Kit-Sakura_Pink-3.jpeg@jpeg",
                                    width="200px",
                                    height="200px",
                                    object_fit="cover",
                                    border_radius="10px",
                                ),
                                rx.text(
                                    "Vaporesso XROS Mini",
                                    width="200px", 
                                    font_size="20px",
                                    color=GRAY,
                                    margin_top="10px",
                                ),
                                rx.text(
                                    "200$",
                                    font_size="35px",
                                    color=BROWN, 
                                    font_weight="bold",
                                ),
                                spacing="2",
                                align="center",
                            ),
                            href="#",
                            _hover={"text_decoration": "none"},
                            min_width="250px",
                            margin_right="20px",
                        ) for _ in range(10)],  #! TEST
                        
                        direction="row",
                        spacing="0",
                        wrap="nowrap",
                        min_width="max-content",
                        padding="10px",
                    ),
                    scrollbars="horizontal",
                    type="hover",
                    width="100%",
                    style={
                        "overflowX": "auto",
                        "whiteSpace": "nowrap",
                    }
                ),
                width="100%",
                margin_top="50px",
                overflow="hidden",
            ),
            rx.box(
                rx.hstack(
                    rx.text(
                        "Feature Products",
                        font_size=rx.breakpoints(
                            initial="20px",
                            sm="25px",
                            md="30px",
                        ),
                        font_weight="bold",
                    ),
                    rx.spacer(),
                    rx.link(
                        "View All",
                        href="/all",
                        color=BROWN,
                        underline="always",
                        weight="bold",
                        font_size=rx.breakpoints(
                            initial="20px",
                            sm="25px",
                            md="30px",
                        ),
                    ),
                ),
                #* products
                rx.box(
                    rx.flex(
                        #* card of product
                        *[rx.box(
                            rx.hstack(
                                rx.image(
                                    "https://tabac.ru/files/products/vaporesso_xros_3_nano_1000_mah_pod_kit_-_lilac_purple.800x600.jpg", 
                                    width="100px",
                                    height="100px",
                                    object_fit="cover",
                                    border_radius="8px"
                                ),    
                                rx.vstack(
                                    rx.text("Vaporesso XROS 3 Nano", font_size="20px", color=GRAY),
                                    rx.text("200$", font_size="20px", color=BROWN, font_weight="bold"),
                                    spacing="1",
                                    align_items="start",
                                    flex="1",
                                ),
                                rx.button(
                                    rx.icon(tag="heart", color='red', size=30,), 
                                    #! if user click -> style={"fill": "red"}
                                    background="transparent",
                                    padding="0",
                                    align="center",
                                    align_self="center",
                                ),
                                spacing="3",
                                width="100%",
                                padding="10px",
                            ), 
                            border=f"1px solid #202020",
                            border_radius="12px",
                            min_width="300px",
                            flex="1 1 300px",
                            margin=rx.breakpoints(
                                initial="0",
                                sm="5px",
                                md="10px",
                            ),
                        ) for _ in range(10)], #! TEST
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
                    overflow="hidden",
                ),
                width="100%",
                margin_top="50px",
            ),
            rx.box(nav_bar(),),
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
        # width="100%",
    )