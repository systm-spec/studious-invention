import customtkinter as ctk
from customtkinter import CTkFrame


class PerkInfo(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        #Gridsystem
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=5)
        self.configure(self, border_width=1, border_color="#808080")


        #PerkFrame
        self.perk_frame= ctk.CTkFrame(self, fg_color='transparent')
        self.perk_frame.grid(column=0, row=1)

        #Heading_lbl
        self.heading_lbl= ctk.CTkLabel(self.perk_frame, font=('Inter',14,'bold'),text='Perks', fg_color='transparent')
        self.heading_lbl.grid(column=0, row=0)

        #Boni_lbl
        self.perk_1_lbl= ctk.CTkLabel(self.perk_frame,font=('Inter',12), text= 'Tollpatsch:', fg_color='transparent')
        self.perk_1_lbl.grid(column=0, row=1, sticky='W')

        self.perk_1_desc= ctk.CTkLabel(self.perk_frame, font=('Inter',12),text= 'Verringertes Würfelglück', fg_color='transparent')
        self.perk_1_desc.grid(column=0, row=2, sticky='W')

        self.perk_2_lbl= ctk.CTkLabel(self.perk_frame,font=('Inter',12), text= 'Prahlhans:', fg_color='transparent')
        self.perk_2_lbl.grid(column=0, row=3, sticky='W')

        self.perk_2_desc= ctk.CTkLabel(self.perk_frame, font=('Inter',12), text= 'Weiss Leute zu tode zu quatschen', fg_color='transparent')
        self.perk_2_desc.grid(column=0, row=4, sticky='W')