import reflex as rx
from ..ui.colors import *
from ..ui.social_links import social_link
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
                            initial="10px",
                            sm="30px",
                            md="40px",
                        ),
                        margin_bottom="5px",
                    ),
                    rx.heading(
                        "Vapeing World",
                        font_size=rx.breakpoints(
                            sm="30px",
                            md="40px",
                        ),
                    ),    
                ),
                rx.box(
                    social_link("search"),    
                ),

                margin_top="50px",
                justify="between",
                width="100%",
            ),
            #* scroll area with filter buttons
            rx.box(
                #! test data
                rx.scroll_area(
                    rx.flex(
                        rx.box(
                            rx.button(
                                rx.text("Creamy Milk",font_size="25px"),
                                background="transparent",
                            ), 
                            rx.button(
                                rx.text("Salty Caramel"),font_size="25px",
                                background="transparent",
                            ),   
                        ),
                        direction="row",
                        spacing="4", 
                        wrap="nowrap",
                        width="80%",
                    ),    
                    scrollbars="horizontal",
                    type="always",
                    width="100%",
                    style={"height": "auto"},
                ),   
                margin_top="50px", 
                width="100%",
            ),
            #* scroll area with product
            rx.box(
                rx.scroll_area(
                    rx.flex(
                        rx.box(
                            rx.link(
                                rx.image(
                                    src="https://static.insales-cdn.com/r/9l1M24o5xE0/rs:fit:1000:0:1/q:100/plain/images/products/1/5370/612308218/Vaporesso-Xros-Mini-1000mAh-MTL-Pod-Kit-Sakura_Pink-3.jpeg@jpeg",
                                    width="200px",
                                    height="200px",       
                                ),
                                rx.text(
                                    "Vaporesso XROS Mini",
                                    width="100%", 
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
                            ),
                        ),
                        direction="row",
                        spacing="4",
                        wrap="nowrap",
                        padding="8px",
                        style={"width": "max-content"},
                    ),
                    type="always", 
                    scrollbars="horizontal",
                    style={"height": "auto", "maxWidth": "100%"},
                ),
                width="100%",
                margin_top="50px",
            ),
            
            margin_left=rx.breakpoints(
                sm="20px",
                md="120px",
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
        # width="100%",
    )