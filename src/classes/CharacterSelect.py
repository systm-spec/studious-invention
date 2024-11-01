import customtkinter as ctk
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
        self.body_frame= ctk.CTkFrame(self, fg_color= "#808080")
        self.body_frame.grid(row= 1, column= 0)

        #






