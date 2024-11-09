import customtkinter as ctk
from PIL import Image

from src.modules.BonusInfo import BonusInfo
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
        self.preview_image_frame.grid(column=0, row=0)

        # Image Load
        self.preview_image= ctk.CTkImage(dark_image=Image.open("assets/img/bard.png"), size=(100,240))
        self.img_wrapper= ctk.CTkLabel(master= self.preview_image_frame, image=self.preview_image, text="")
        self.img_wrapper.grid()

        #InfoFrame
        self.info_frame= ctk.CTkFrame(self, fg_color='transparent')
        self.info_frame.grid(column=1, row=0, ipadx=8, ipady=8)

        # Raceframe(Race)
        self.race_info_frame= RaceInfo(self.info_frame, fg_color='transparent')
        self.race_info_frame.grid(column= 0, row=0,sticky='ew', ipadx=9, ipady=2)

        # Classframe
        self.class_info_frame= ClassInfo(self.info_frame, fg_color='transparent')
        self.class_info_frame.grid(column= 0, row=1, sticky='EW', ipadx=9, ipady=2)

        # Boniframe
        self.boni_frame= ctk.CTkFrame(self.info_frame, fg_color='transparent')
        self.boni_frame.grid(column=0, row=2, ipadx=9,ipady= 2)

        # Attr_Frame
        self.attr_frame= BonusInfo(self.boni_frame, fg_color='transparent')
        self.attr_frame.grid(column=0, row=0, sticky='NSEW')

        # Perk_Frame
        self.perk_frame= PerkInfo(self.boni_frame, fg_color='transparent')
        self.perk_frame.grid(column=1, row=0)