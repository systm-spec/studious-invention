import customtkinter as ctk
from customtkinter import CTkFrame


class AttributInfo(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        #Gridsystem
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=2)
        self.grid_rowconfigure(1,weight=3)
        self.configure(self, border_width=1, border_color="#808080")

        #BonusFrame
        self.bonus_frame= ctk.CTkFrame(self, fg_color='transparent')
        self.bonus_frame.grid(column=0, row=1)

        #Heading_lbl
        self.heading_lbl= ctk.CTkLabel(self, font=('Inter',14,'bold'), text='Boni', fg_color='transparent')
        self.heading_lbl.grid(column=0, row=0, ipadx=2)

        #Boni_lbl
        self.boni_top= ctk.CTkLabel(self.bonus_frame, font=('Inter',12), text= 'Willenskraft: 2', fg_color='transparent')
        self.boni_top.grid(column=0, row=0)

        self.boni_mid= ctk.CTkLabel(self.bonus_frame, font=('Inter',12), text= 'Vitalität: 2', fg_color='transparent')
        self.boni_mid.grid(column=0, row=1)

        self.boni_low= ctk.CTkLabel(self.bonus_frame, font=('Inter',12), text= 'Charisma: -2', fg_color='transparent')
        self.boni_low.grid(column=0, row=2)