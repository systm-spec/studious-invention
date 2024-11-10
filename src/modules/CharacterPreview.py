import customtkinter as ctk
from PIL import Image


### CHARAKTER-PREVIEW & INFOBOX ###

class CharacterPreview(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # GRID-SYSTEM
        self.grid_columnconfigure(index= (0, 1), weight= 1)

        # PREVIEW-CLASS-IMAGE-FRAME
        self.preview_class_image_frame= ctk.CTkFrame(self)
        self.preview_class_image_frame.grid(column=0, row=0, padx=(0,12))
        # IMAGE-LOAD
        self.preview_image= ctk.CTkImage(dark_image=Image.open("assets/img/bard.png"), size=(300,480))
        self.img_wrapper= ctk.CTkLabel(master= self.preview_class_image_frame, image=self.preview_image, text="")
        self.img_wrapper.grid()

        # INFO-FRAME
        self.info_frame= ctk.CTkFrame(self, fg_color='transparent', border_color="#808080", border_width=1)
        self.info_frame.grid(column=1, row=0, sticky='NSWE')
        # GRID-SYSTEM-INFO-FRAME
        self.info_frame.grid_rowconfigure((0,1),weight=4)
        self.info_frame.grid_rowconfigure(2, weight=2)
        self.info_frame.grid_columnconfigure(0, weight=1)

        # RACE-FRAME
        self.race_info_frame= RaceInfo(self.info_frame, fg_color='transparent')
        self.race_info_frame.grid(column= 0, row=0, sticky='NSEW', ipadx=4, ipady=8, padx=(12,12), pady=(10,2))

        # CLASS-FRAME
        self.class_info_frame= ClassInfo(self.info_frame, fg_color='transparent')
        self.class_info_frame.grid(column= 0, row=1, sticky='NSEW', padx=(12,12), pady=(2,4), ipadx=4, ipady=8)

        ## BONI-FRAME
        self.boni_frame= ctk.CTkFrame(self.info_frame, fg_color='transparent')
        self.boni_frame.grid(column=0, row=2, ipadx=9,ipady= 2)

        # ATTRIBUT-FRAME
        self.attr_frame= AttributInfo(self.boni_frame, fg_color='transparent')
        self.attr_frame.grid(column=0, row=0, sticky='NSEW', ipadx=16, ipady=12, padx=(12,0))

        # PERK-FRAME
        self.perk_frame= PerkInfo(self.boni_frame, fg_color='transparent')
        self.perk_frame.grid(column=1, row=0, sticky='NSEW', ipadx=16, ipady=12, padx=(12,0))



### CLASSINFO ###
class ClassInfo(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # GRID-SYSTEM
        self.grid_columnconfigure(0,weight=1)
        self.configure(self, border_width=1, border_color='#808080')

        # HEADING-LBL
        head_lbl= ctk.CTkLabel(self, text='Bard', fg_color='transparent')
        head_lbl.grid(pady=(6,0))

        # TEXT-LBL
        self.class_info = ctk.CTkLabel(master=self, wraplength=350, fg_color='transparent', font=('Inter',12),
                                        corner_radius=12, text="Ein Barde, wie er im Buche  steht – oder zumindest, wie"
                                        "er meint, im Buche zu stehen. Kein Auftritt vergeht, ohne dass er (ungefragt) "
                                        "betont, wie brillant, unentbehrlich und einzigartig er ist. Natürlich kennt er "
                                        "alle die besten Helden der Welt und ist der Grund, warum ihre Abenteuer überhaupt"
                                        "spannend sind.Seine Lieder polarisieren, aber hey, was sind schon ein paar "
                                        "Augenrollen, wenn man die Aufmerksamkeit auf sich zieht, oder?")
        self.class_info.grid()


### RACE-INFO ###
class RaceInfo(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # GRIND-SYSTEM
        self.grid_columnconfigure(0,weight=1,)
        self.configure(self, border_width=1, border_color='#808080')

        # HEADING-LBL
        head_lbl= ctk.CTkLabel(self, text='Mensch', fg_color='transparent')
        head_lbl.grid(pady=(6,0))

        # INFO-LBL
        self.race_info = ctk.CTkLabel(master=self, wraplength=350, fg_color='transparent', font=('Inter',12),
                                    corner_radius=12, text= "Meister der Selbstdarstellung und immer überzeugt, "
                                    "dass ihre Meinung die Welt bewegt. Sie neigen dazu, sich selbst zur Hauptfigur"
                                    "in jeder Geschichte zu machen – auch wenn’s nur ums Frühstück geht. Flexibel,"
                                    "ehrgeizig und manchmal ein bisschen zu überzeugt von ihrer eigenen Großartigkeit.")
        self.race_info.grid()


### ATTRIBUT-INFO ###

class AttributInfo(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # GRID-SYSTEM
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=2)
        self.grid_rowconfigure(1,weight=3)
        self.configure(self, border_width=1, border_color="#808080")

        # ATTRIBUT-BONUS-FRAME
        self.bonus_frame= ctk.CTkFrame(self, fg_color='transparent')
        self.bonus_frame.grid(column=0, row=1)

        # HEADING-LBL
        self.heading_lbl= ctk.CTkLabel(self, font=('Inter',14,'bold'), text='Attribute', fg_color='transparent')
        self.heading_lbl.grid(column=0, row=0, ipadx=2)

        # BONUS-LBL
        self.boni_top= ctk.CTkLabel(self.bonus_frame, font=('Inter',12), text= 'Willenskraft: 2', fg_color='transparent')
        self.boni_top.grid(column=0, row=0)
        self.boni_mid= ctk.CTkLabel(self.bonus_frame, font=('Inter',12), text= 'Vitalität: 2', fg_color='transparent')
        self.boni_mid.grid(column=0, row=1)
        self.boni_low= ctk.CTkLabel(self.bonus_frame, font=('Inter',12), text= 'Charisma: -2', fg_color='transparent')
        self.boni_low.grid(column=0, row=2)



### PERK-INFO ###

class PerkInfo(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # GRID-SYSTEM
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=5)
        self.configure(self, border_width=1, border_color="#808080")

        # PERK-FRAME
        self.perk_frame= ctk.CTkFrame(self, fg_color='transparent')
        self.perk_frame.grid(column=0, row=1)

        # HEADING-LBL
        self.heading_lbl= ctk.CTkLabel(self.perk_frame, font=('Inter',14,'bold'),text='Perks', fg_color='transparent')
        self.heading_lbl.grid(column=0, row=0)

        # PERK-LBL
        self.perk_1_lbl= ctk.CTkLabel(self.perk_frame,font=('Inter',12), text= 'Tollpatsch:', fg_color='transparent')
        self.perk_1_lbl.grid(column=0, row=1, sticky='W')
        self.perk_1_desc= ctk.CTkLabel(self.perk_frame, font=('Inter',12),text= 'Verringertes Würfelglück', fg_color='transparent')
        self.perk_1_desc.grid(column=0, row=2, sticky='W')

        self.perk_2_lbl= ctk.CTkLabel(self.perk_frame,font=('Inter',12), text= 'Prahlhans:', fg_color='transparent')
        self.perk_2_lbl.grid(column=0, row=3, sticky='W')
        self.perk_2_desc= ctk.CTkLabel(self.perk_frame, font=('Inter',12), text= 'Weiss Leute zu tode zu quatschen', fg_color='transparent')
        self.perk_2_desc.grid(column=0, row=4, sticky='W')