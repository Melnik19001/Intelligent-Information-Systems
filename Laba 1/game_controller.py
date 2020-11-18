from tkinter import *
import json
from collections import defaultdict

class GameController:
    def __init__(self, root, input_file, background_color):
        self.__root = root
        self.__input_file = input_file
        self.__background_color = background_color

        self.__main_target = "фрукт"

        self.__label = Label(
            self.__root,
            text="Выберите наиболее подходящий вариант",
            background=self.__background_color,
            font=("Times New Roman", 18, "italic")
        )
        self.__label.grid(row=1, column=1)


        self.__question_frame = Frame(self.__root)
        self.__question_frame.config(background=self.__background_color)
        self.__question_text = StringVar()
        self.__question = Label(
            self.__question_frame,
            textvariable=self.__question_text,
            background=self.__background_color,
            font=("Times New Roman", 22, "italic")
        )
        self.__question.grid(row=0, column=0)
        self.__client_answer = StringVar(self.__question_frame)
        self.__options = OptionMenu(self.__question_frame, self.__client_answer, "1")
        self.__options.config(bg=self.__background_color)
        self.__options.grid(row=0, column=1, pady=(7, 0))
        self.__question_frame.grid(row=2, column=1)
        self.__hide_all()

    def __hide_all(self):
        self.__label.grid_remove()
        self.__question_frame.grid_remove()

    def __show_all(self):
        self.__label.grid()
        self.__question_frame.grid()

    def __precalc_options(self, rules):
        options = defaultdict(set)
        for rule in rules:
            composite_condition = rule["if"]
            for simple_condition in composite_condition:
                options[simple_condition["condition"]].add(simple_condition["consequence"])
        return options

    def __find_rule(self, current_target, rules):
        for rule in rules:
            if rule["then"]["target"] == current_target:
                return rule
        return None

    def __check_rule(self, rule, known_attributes):
        for condition in rule["if"]:
            if not known_attributes.get(condition["condition"]):
                return condition["condition"]
            if known_attributes.get(condition["condition"]) != condition["consequence"]:
                return False
        return True

    def __ask_question(self, target, options, known_attributes):
        print(target.capitalize())
        self.__question_text.set(target.capitalize() + ":")
        self.__client_answer.set("")
        self.__options.grid_forget()
        self.__options = OptionMenu(self.__question_frame, self.__client_answer, *options[target])
        self.__options.config(width=10)
        self.__options.config(bg=self.__background_color)
        self.__options.grid(row=0, column=1, pady=(7, 0))
        # for option in options[target]:
        #     self.__options['menu'].add_command(
        #         slabel=option, command=_setit(self.__client_answer, option))


    def execute(self):
        self.__show_all()
        with open(self.__input_file, "r") as file:
            rules = json.load(file)
        options = self.__precalc_options(rules)

        targets = [self.__main_target]
        known_attributes = {}
        while True:
            current_target = targets[-1]
            # print(targets)
            rule = self.__find_rule(current_target, rules)

            if not rule:
                self.__ask_question(current_target, options, known_attributes)
                break

            check_rule_result = self.__check_rule(rule, known_attributes)
            if check_rule_result == True:
                pass
            if check_rule_result == False:
                pass
            targets.append(check_rule_result)
