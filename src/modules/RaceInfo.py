import customtkinter as ctk


class RaceInfo(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0,weight=1,)
        self.configure(self, border_width=1, border_color='#808080')

        #Header
        head_lbl= ctk.CTkLabel(self, text='Mensch', fg_color='transparent')
        head_lbl.grid(pady=(6,0))

        #Textbox
        self.textbox = ctk.CTkLabel(master=self, wraplength=350, fg_color='transparent', font=('Inter',12), corner_radius=12, text= "Meister der Selbstdarstellung und immer überzeugt, dass ihre Meinung die"
                                    "Welt bewegt. Sie neigen dazu, sich selbst zur Hauptfigur in jeder Geschichte zu"
                                    "machen – auch wenn’s nur ums Frühstück geht. Flexibel, ehrgeizig und manchmal ein"
                                    "bisschen zu überzeugt von ihrer eigenen Großartigkeit.")
        self.textbox.grid()