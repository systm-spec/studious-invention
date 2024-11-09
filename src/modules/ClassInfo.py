import customtkinter as ctk


class ClassInfo(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        #Gridsystem
        self.grid_columnconfigure(0,weight=1)
        self.configure(self, border_color='red', border_width=2)
        #Header

        head_lbl= ctk.CTkLabel(self, text='Bard', fg_color='transparent')
        head_lbl.grid()

        #Textbox
        self.textbox = ctk.CTkTextbox(master=self,height=130, fg_color='transparent', font=('Inter',12), corner_radius=12, wrap='word')
        self.textbox.insert("0.0", "Ein Barde, wie er im Buche  steht – oder zumindest, wie er meint, im Buche zu stehen."
        ' Kein Auftritt vergeht, ohne dass er (ungefragt) betont, wie brillant, unentbehrlich und einzigartig er ist.'
        'Natürlich kennt er alle die besten Helden der Welt und ist der Grund, warum ihre Abenteuer überhaupt spannend'
        'sind.Seine Lieder polarisieren, aber hey, was sind schon ein paar Augenrollen, wenn man die Aufmerksamkeit auf'
        'sich zieht, oder?\n', 'end')
        self.textbox.grid(sticky='EW')