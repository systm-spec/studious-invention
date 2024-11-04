import customtkinter as ctk
from PIL import Image
from pygame.examples.cursors import image

from src.modules.CharacterConfig import CharacterConfig
from src.modules.CharacterPreview import CharacterPreview

class CharacterSelect(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Grid-System
        self.grid_rowconfigure(index= (0, 1), weight= 1)
        self.grid_columnconfigure(index= 0, weight= 1)

        # Heading_Frame
        self.heading_frame= ctk.CTkFrame(self, fg_color= "transparent")
        self.heading_frame.grid(row= 0, column= 0)
        # Image_Load
        self.heading_image = ctk.CTkImage(dark_image=Image.open("assets/img/Header.png"), size=(750, 100))
        self.heading_lbl= ctk.CTkLabel(master= self.heading_frame, image=self.heading_image)
        self.heading_lbl.grid()

        # Character_Config_Frame
        self.body_frame= ctk.CTkFrame(self, fg_color= "transparent")
        self.body_frame.grid(row= 1, column= 0)

        # Body_Grid
        self.body_frame.grid_rowconfigure(index=0, weight=0)
        self.body_frame.grid_columnconfigure(0, weight= 1)
        self.body_frame.grid_columnconfigure(1, weight= 3)

        # Character_Config_Frame
        self.character_config_frame= CharacterConfig(self.body_frame, fg_color= "transparent",border_width=1, border_color="#808080")
        self.character_config_frame.grid( column= 0, sticky="nwsn", padx=12, pady=4)

        # Character_Preview_Frame
        self.character_preview_frame= CharacterPreview(master=self.body_frame, fg_color= "transparent")
        self.character_preview_frame.grid(row= 0, column= 1, padx= 0, pady=4)











