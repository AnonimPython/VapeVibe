import reflex as rx


def main() -> rx.Component:
    return rx.box(
        #* header
        rx.box(
            rx.hstack(
                #* user image 
                rx.box(
                    rx.image(""),
                ),    
            ),
            
        ),
        
    display=rx.breakpoints(
        initial="block",  #? mobile
        sm="block",      #? tablets
        md="block",      #? middle screen
        lg="none"        #? big screen < 1366px
    ),
    )