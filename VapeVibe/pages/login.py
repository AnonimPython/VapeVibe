import reflex as rx

def login() -> rx.Component:
    return rx.box(
        rx.heading("LOGIN PAGE"),
        rx.text("VAPEVIBE", color="orange"),
        
        
    display=rx.breakpoints(
        initial="block",  #? mobile
        sm="block",      #? tablets
        md="block",      #? middle screen
        lg="none"        #? big screen < 1366px
    ),
    )