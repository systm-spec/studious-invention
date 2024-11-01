import customtkinter as ctk

from src.classes.CharacterPreview import CharacterPreview


class CharacterSelect(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)



        # Grid-System
        self.grid_rowconfigure(index= (0, 1), weight= 1)
        self.grid_columnconfigure(index= 0, weight= 1)

        # Heading_Frame
        self.heading_frame= ctk.CTkFrame(self, fg_color= "#808080")
        self.heading_frame.grid(row= 0, column= 0)
        self.heading_lbl= ctk.CTkLabel(self.heading_frame, text= "Start Your Adventure", fg_color= "gray14", text_color= "#FAFAFA", font= ("inter", 46))
        self.heading_lbl.grid(padx= 2, pady= 2, ipadx= 100, ipady= 10)

        # Character_Select_Frame
        self.body_frame= ctk.CTkFrame(self, fg_color= "blue")
        self.body_frame.grid(row= 1, column= 0)
        # Body_Grid
        self.body_frame.grid_rowconfigure(index= 0, weight= 1)
        self.body_frame.grid_columnconfigure(index= 0, weight= 1)
        self.body_frame.grid_columnconfigure(index= 1, weight= 3)
        # Character_Config_Frame
        self.character_config_frame= ctk.CTkFrame(self.body_frame, fg_color= "red")
        self.character_config_frame.grid(row= 0, column= 0, ipadx= 4, ipady= 4)
        self.character_config_frame.grid_rowconfigure((0, 1, 2, 3, 4), weight= 1)
        # Character_Preview_Frame
        self.character_preview_frame= CharacterPreview(master, fg_color= "green")
        self.character_preview_frame.grid(row= 0, column= 1, padx= (10, 0))











