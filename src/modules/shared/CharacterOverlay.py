import customtkinter as ctk
from PIL import Image


class CharacterOverlay(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # GRID-SYSTEM
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0,1,2,3,4), weight=1)

        ## ROWS
        # FRAMES

        self.bars_frame=ctk.CTkFrame(self,fg_color="transparent",border_width=1, border_color="#808080")
        self.bars_frame.grid(column=0, row=1)
        self.main_armor_frame = ctk.CTkFrame(self,fg_color="transparent",border_width=1, border_color="#808080")
        self.main_armor_frame.grid(column=0, row=2)
        self.secondary_armor_frame=ctk.CTkFrame(self,fg_color="transparent",border_width=1, border_color="#808080")
        self.secondary_armor_frame.grid(column=0, row=3)
        self.stats_frame = ctk.CTkFrame(self,fg_color="transparent",border_width=1, border_color="#808080")
        self.grid(column=0, row=4)

        # HEADING
        self.heading_frame = ctk.CTkFrame(self,fg_color="transparent",border_width=1, border_color="#808080")
        self.heading_frame.grid(column=0, row=0)

        self.icon=ctk.CTkImage(dark_image=Image.open("assets/img/icon/spec_text_icon.png"), size=(62, 56))
        self.icon_lbl=ctk.CTkLabel(self.heading_frame, image=self.icon, text="")
        self.icon_lbl.grid(column=0, row=0)
        self.name=ctk.CTkLabel(self.heading_frame,  text="Der Schänder mit dem Ständer", font=("Inter", 28))
        self.name.grid(column=1, row=0)
        self.sub_info=ctk.CTkLabel(self.heading_frame, text="Level 1 Human Bard from the highlands")
        self.sub_info.grid(column=1, row=1)
