
#* COLORS
BACKGROUND = "#131313"
ADDITIONAL_BACKGROUND = "#181818"
BROWN = "#bd8767"
RED = "#fd2627"
ADDITIONAL_TEXT_COLOR = "#c18a6c"
GRAY = "#b1b1b1"


#* STYLES
input_style: dict = {
    "width": "300px",
    "height": "50px",
    "--text-field-focus-color": BROWN,
    "background": BACKGROUND,
    "color": "white",
    "& input::placeholder": {
        "padding-left":"10px",
        "color": "white"
    },
    "font-size": "20px",
    }