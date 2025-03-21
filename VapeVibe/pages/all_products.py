import reflex as rx

def all_products():
    return rx.box(
        
        rx.vstack(
                
            
                    
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