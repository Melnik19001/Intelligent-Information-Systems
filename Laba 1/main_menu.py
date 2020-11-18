from tkinter import *

from utils import *
from game_controller import GameController

class MainMenu:
    def __init__(self, root, background_color, input_file):
        self.__root = root
        self.__background_color = background_color

        self.__play = create_button(self.__root, 1, 1, "Play", command=self.__play_button_callback)
        self.__info = create_button(
            self.__root, 1, 2, "Database", command=self.__info_button_callback)
        self.__hide_all()

        self.__game_controller = \
            GameController(
                root, input_file, background_color, self.__back_to_main_menu_from_game_callback)

    def __hide_all(self):
        self.__play.grid_remove()
        self.__info.grid_remove()

    def __show_all(self):
        self.__play.grid()
        self.__info.grid()

    def __back_to_main_menu_from_game_callback(self):
        self.__show_all()

    def __play_button_callback(self):
        self.__hide_all()
        self.__game_controller.execute()

    def __info_button_callback(self):
        self.__hide_all()

    def execute(self):
        self.__show_all()

