import reflex as rx

def register() -> rx.Component:
    return rx.box(
        rx.heading("REGISTER PAGE"),
        
        
        
    display=rx.breakpoints(
        initial="block",  #? mobile
        sm="block",      #? tablets
        md="block",      #? middle screen
        lg="none"        #? big screen < 1366px
    ),
    )