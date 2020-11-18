from tkmacosx import *

def create_button(root, x, y, text, command=None, background_color="seagreen1"):
    # seagreen1
    button = Button(
        root,
        text=text,
        command=command,
        bg=background_color,
        borderless=True,
        font=("Times New Roman", 20, "italic"),
    )
    if x and y:
        button.grid(row=x, column=y, padx=(0, 0))
    return button
