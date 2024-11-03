import customtkinter as ctk

from modules.shared.CharacterOverlay import CharacterOverlay
from modules.start.CharacterCreationPage import CharacterCreation
from util.windows import check_for_windows
import os
import sys

# src als Root-Verzeichnis hinzufügen, falls nicht bereits vorhanden
src_path = os.path.join(os.path.dirname(__file__), 'src')
if src_path not in sys.path:
    sys.path.append(src_path)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Der RPG")
        self.geometry("1280x720")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("config/theme/custom.json")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.bind("<Escape>", lambda a:self.destroy())
        ### START WINDOW ###
        # self.start_menu_frame = StartMenu(master=self, fg_color="transparent")
        # self.start_menu_frame.grid(row=0, column=0, padx=20, pady=210, sticky="nsew")

        ### CREATION WINDOW ###
        # self.character_creation_frame = CharacterCreation(self, fg_color="transparent")
        # self.character_creation_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        ## TEST CHARACTER SHEET ###
        self.character_overlay_frame = CharacterOverlay(self)
        self.character_overlay_frame.grid(row=0, column=0, ipadx=20, ipady=20, pady=20)
        
# MAIN
check_for_windows()
app = App()

# END
app.mainloop()

