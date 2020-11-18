from tkinter import *

from main_menu import *
from utils import *

class MainWindow:
    def __init__(self, input_file):
        self.__input_file = input_file

    def __load_window(self):
        # self.__background_color = "orchid1"
        self.__background_color = "light goldenrod yellow"
        self.__root = Tk()
        self.__root.title("Laba 1")
        self.__root.geometry("500x400")
        self.__root.minsize(500, 400)
        self.__root.configure(background=self.__background_color)
        self.__root.attributes('-topmost', True)
        self.__root.state('zoomed')
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(100, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)
        self.__root.grid_columnconfigure(100, weight=1)

        label = Label(
            self.__root,
            text="Designed by Daniil Melnichenka, 2020",
            background=self.__background_color,
            font=("Helvetica", 13, "italic")
        )
        label.place(relx=0.5, rely=0.95, anchor="center")

    def __play(self):
        pass

    def execute(self):
        self.__load_window()
        self.__main_menu = MainMenu(self.__root, self.__background_color, self.__input_file)
        self.__main_menu.execute()
        self.__root.mainloop()


if __name__ == "__main__":
    MainWindow("data/rules.json").execute()

# tkinter._test()
