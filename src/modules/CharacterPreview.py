import customtkinter as ctk
from PIL import Image

from src.modules.AttributInfo import AttributInfo
from src.modules.ClassInfo import ClassInfo
from src.modules.RaceInfo import RaceInfo
from src.modules.PerkInfo import PerkInfo


class CharacterPreview(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Grid-System
        self.grid_columnconfigure(index= (0, 1), weight= 1)

        # Preview_Image_Frame
        self.preview_image_frame= ctk.CTkFrame(self)
        self.preview_image_frame.grid(column=0, row=0, padx=(0,12))

        # Image Load
        self.preview_image= ctk.CTkImage(dark_image=Image.open("assets/img/bard.png"), size=(300,480))
        self.img_wrapper= ctk.CTkLabel(master= self.preview_image_frame, image=self.preview_image, text="")
        self.img_wrapper.grid()

        #InfoFrame
        self.info_frame= ctk.CTkFrame(self, fg_color='transparent', border_color="#808080", border_width=1)
        self.info_frame.grid(column=1, row=0, sticky='NSWE')
        self.info_frame.grid_rowconfigure((0,1),weight=4)
        self.info_frame.grid_rowconfigure(2, weight=2)
        self.info_frame.grid_columnconfigure(0, weight=1)

        # Raceframe(Race)
        self.race_info_frame= RaceInfo(self.info_frame, fg_color='transparent')
        self.race_info_frame.grid(column= 0, row=0, sticky='NSEW', ipadx=4, ipady=8, padx=(12,12), pady=(10,2))

        # Classframe
        self.class_info_frame= ClassInfo(self.info_frame, fg_color='transparent')
        self.class_info_frame.grid(column= 0, row=1, sticky='NSEW', padx=(12,12), pady=(2,4), ipadx=4, ipady=8)


        # Boniframe
        self.boni_frame= ctk.CTkFrame(self.info_frame, fg_color='transparent')
        self.boni_frame.grid(column=0, row=2, ipadx=9,ipady= 2)

        # Attr_Frame
        self.attr_frame= AttributInfo(self.boni_frame, fg_color='transparent')
        self.attr_frame.grid(column=0, row=0, sticky='NSEW', ipadx=16, ipady=12, padx=(12,0))

        # Perk_Frame
        self.perk_frame= PerkInfo(self.boni_frame, fg_color='transparent')
        self.perk_frame.grid(column=1, row=0, sticky='NSEW', ipadx=16, ipady=12, padx=(12,0))