import customtkinter as ctk
from PIL import Image
class CharacterPreview(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Grid-System
        self.grid_columnconfigure(index= (0, 1), weight= 1)

        # Preview_Image_Frame
        self.preview_image_frame= ctk.CTkFrame(self, fg_color= "yellow")
        self.preview_image_frame.grid(column= 0)
        # Image Load
        self.preview_image= ctk.CTkImage(dark_image= Image.open("../assets/img/cls/Bard.png", "r"), size= (400, 640))
        self.img_wrapper= ctk.CTkLabel(master= self.preview_image_frame, image= self.preview_image)
        self.img_wrapper.grid()

        # Preview_Description_Frame
        self.preview_description_frame= ctk.CTkFrame(self, fg_color= "orange")
        self.preview_description_frame.grid(column= 1)
