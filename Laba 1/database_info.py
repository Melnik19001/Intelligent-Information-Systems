from tkinter import *
import json

from utils import *

class DatabaseInfo:
    def __init__(self, root, input_file, background_color, back_to_main_menu_callback):
        self.__root = root

        self.__rules_box = Listbox(self.__root)
        self.__rules_box.grid(row=1, column=1, sticky="nswe")
        self.__rules_box.config(bg=background_color, bd=0)
        for rule in self.__get_rules_as_strings(input_file):
            self.__rules_box.insert(END, rule)

        self.__vertical_scrollbar = Scrollbar(root)
        self.__rules_box.config(yscrollcommand = self.__vertical_scrollbar.set)
        self.__vertical_scrollbar.config(command = self.__rules_box.yview)
        self.__vertical_scrollbar.grid(row=1, column=2, sticky="nse")

        self.__horizontal_scrollbar = Scrollbar(root, orient='horizontal')
        self.__rules_box.config(xscrollcommand = self.__horizontal_scrollbar.set)
        self.__horizontal_scrollbar.config(command = self.__rules_box.xview)
        self.__horizontal_scrollbar.grid(row=2, column=1, sticky="new")


        def back_to_menu_button_callback():
            self.__hide_all()
            back_to_main_menu_callback()
        self.__back_to_menu_button = \
            create_button(
                self.__root, None, None,
                "Вернуться в главное меню", command=back_to_menu_button_callback)

        self.__hide_all()

    def __get_rules_as_strings(self, input_file):
        with open(input_file, "r") as file:
            rules = json.load(file)
        result = []
        for rule in rules:
            result.append(convert_rule_to_str(rule))
        return result

    def __hide_all(self):
        self.__root.grid_rowconfigure(1, weight=0)
        self.__root.grid_rowconfigure(100, weight=2)
        self.__root.grid_columnconfigure(1, weight=0)
        self.__rules_box.grid_remove()
        self.__vertical_scrollbar.grid_remove()
        self.__horizontal_scrollbar.grid_remove()
        self.__back_to_menu_button.grid_remove()

    def __show_all(self):
        self.__root.grid_rowconfigure(1, weight=40)
        self.__root.grid_rowconfigure(100, weight=2)
        self.__root.grid_columnconfigure(1, weight=20)
        self.__rules_box.grid()
        self.__vertical_scrollbar.grid()
        self.__horizontal_scrollbar.grid()
        self.__back_to_menu_button.grid(row=3, column=1, columnspan=2, rowspan=98, pady=(15, 30), sticky='n')

    def execute(self):
        self.__show_all()
