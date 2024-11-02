import customtkinter as ctk

class CharacterConfig(ctk.CTkFrame):
    def __init__(self,master ,**kwargs):
        super().__init__(master, **kwargs)

        # GRID-SYSTEM
        self.grid_rowconfigure(index=(0,1,2,3,4), weight=1)

        ## ROWS
        # GENDER
        self.gender = ctk.CTkFrame(self)
        self.gender.grid(row=0)
        self.male = ctk.CTkRadioButton(self.gender, value=0)
        self.male.grid(column=0, row=0)
        self.female = ctk.CTkRadioButton(self.gender, value=1 )
        self.female.grid(column=1,row=0)

        # RACES
        self.races = ctk.CTkFrame(self)
        self.races.grid(row=1)
        self.human_radio = ctk.CTkRadioButton(self.races, value=0)
        self.human_radio.grid(row=0, column=0)
        self.dwarf_radio = ctk.CTkRadioButton(self.races, value=1)
        self.dwarf_radio.grid(row=0,column=1)
        self.elves_radio = ctk.CTkRadioButton(self.races, value=2)
        self.elves_radio.grid(row=1, column=0)
        self.orcs_radio = ctk.CTkRadioButton(self.races, value=3)
        self.orcs_radio.grid(row=1,column=1)

        # SPECIALISATIONS
        self.specs = ctk.CTkFrame(self)
        self.specs.grid(row=2)
        self.archer_btn = ctk.CTkButton(self.specs)
        self.archer_btn.grid(column=0, row=0)
        self.bard_btn = ctk.CTkButton(self.specs)
        self.bard_btn.grid(column=1, row=0)
        self.druid_btn = ctk.CTkButton(self.specs)
        self.druid_btn.grid(column=2, row=0)
        self.occult_btn = ctk.CTkButton(self.specs)
        self.occult_btn.grid(column=0, row=1)
        self.doctor_btn = ctk.CTkButton(self.specs)
        self.doctor_btn.grid(column=1, row=1)
        self.chemist_btn=ctk.CTkButton(self.specs)
        self.chemist_btn.grid(column=2,row=1)

        # NAME
        self.name = ctk.CTkFrame(self)
        self.name.grid(row=3)
        self.name_ntry = ctk.CTkEntry(self.name)
        self.name_ntry.grid()

        # START BTN
        self.start_btn = ctk.CTkButton(self)
        self.start_btn.grid(row=4)