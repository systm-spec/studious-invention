import customtkinter as ctk

from src.classes.CharacterSelect import CharacterSelect
from src.classes.StartMenu import StartMenu
from src.util.windows import check_for_windows
from PIL import Image
import os


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Der RPG")
        self.geometry("1280x720")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("./config/theme/custom.json")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        ### START WINDOW ###
        # self.start_menu_frame = StartMenu(master=self, fg_color="transparent")
        # self.start_menu_frame.grid(row=0, column=0, padx=20, pady=210, sticky="nsew")

        ### CREATION WINDOW ###
        self.start_character_frame = CharacterSelect(self, fg_color="transparent")
        self.start_character_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
# MAIN
check_for_windows()
app = App()

# END
app.mainloop()

