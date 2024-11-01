import customtkinter as ctk
from src.classes.StartMenu import StartMenu
from src.util.windows import check_for_windows
from PIL import Image
import os


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Der RPG")
        self.geometry("680x720")
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("./config/theme/custom.json")

        self.start_menu_frame = StartMenu(master=self, fg_color="transparent")
        self.start_menu_frame.pack(fill="both", expand=True, padx=120, pady=240)
        # self.start_menu_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
# MAIN
check_for_windows()
app = App()

# END
app.mainloop()

