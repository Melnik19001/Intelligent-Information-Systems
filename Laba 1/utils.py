from tkmacosx import *

def create_button(root, x, y, text, command=None, background_color="seagreen1"):
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

def convert_rule_to_str(rule):
    result = "Если "
    composite_condition = rule["if"]
    for idx, simple_condition in enumerate(composite_condition):
        result += simple_condition["condition"] + ": " + simple_condition["consequence"]
        if idx + 1 != len(composite_condition):
            result += " и "
    result += ", то "
    result += rule["then"]["target"] + ": " + rule["then"]["value"]
    return result
