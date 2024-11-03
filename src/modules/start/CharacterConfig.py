import tkinter as tk
import customtkinter as ctk

class CharacterConfig(ctk.CTkFrame):
    def __init__(self,master ,**kwargs):
        super().__init__(master, **kwargs)

        # GRID-SYSTEM
        self.grid_rowconfigure(index=(0,1,2,3,4), weight=1)

        ## ROWS
        # GENDER
        self.gender = ctk.CTkFrame(self,fg_color="transparent",border_width=1, border_color="#808080")
        self.gender.grid(row=0)
        self.gender_value=tk.IntVar(value=0)
        self.female = ctk.CTkRadioButton(self.gender,text="Female", value=1,variable=self.gender_value)
        self.female.grid(column=0, row=0, padx=(48,6), pady=8)
        self.male = ctk.CTkRadioButton(self.gender, text="Male",value=2, variable=self.gender_value )
        self.male.grid(column=1,row=0, padx=(6,18), pady=8)

        # RACES
        self.races = ctk.CTkFrame(self,fg_color="transparent",border_width=1, border_color="#808080")
        self.races.grid(row=1, sticky="nswe", padx=86, pady=28)
        self.races.grid_rowconfigure((0,1), weight=1)
        self.races.grid_columnconfigure((0, 1), weight=1)
        self.race_value=tk.StringVar(value="")
        self.human_radio = ctk.CTkRadioButton(self.races, text="Human",variable=self.race_value, value="human")
        self.human_radio.grid(row=0, column=0)
        self.dwarf_radio = ctk.CTkRadioButton(self.races, text="Dwarf",variable=self.race_value, value="dwarf")
        self.dwarf_radio.grid(row=0,column=1)
        self.elves_radio = ctk.CTkRadioButton(self.races, text="Elf",variable=self.race_value, value="elf")
        self.elves_radio.grid(row=1, column=0)
        self.orcs_radio = ctk.CTkRadioButton(self.races, text="Orc",variable=self.race_value, value="orc")
        self.orcs_radio.grid(row=1,column=1)

        # SPECIALISATIONS
        self.specs = ctk.CTkFrame(self, fg_color="transparent")
        self.specs.grid(row=2, padx=10)
        self.archer_btn = ctk.CTkButton(self.specs, corner_radius=2, fg_color="transparent", text="Archer", border_color="#ccc", border_width=1)
        self.archer_btn.grid(column=0, row=0, padx=3, pady=3, ipady=1)
        self.bard_btn = ctk.CTkButton(self.specs, corner_radius=2, fg_color="transparent", text="Bard", border_color="#ccc", border_width=1)
        self.bard_btn.grid(column=1, row=0, padx=3, pady=3, ipady=1)
        self.druid_btn = ctk.CTkButton(self.specs, corner_radius=2, fg_color="transparent", text="Druid", border_color="#ccc", border_width=1)
        self.druid_btn.grid(column=2, row=0, padx=3, pady=3, ipady=1)
        self.occult_btn = ctk.CTkButton(self.specs, corner_radius=2, fg_color="transparent", text="Occult", border_color="#ccc", border_width=1)
        self.occult_btn.grid(column=0, row=1, padx=3, pady=3, ipady=1)
        self.doctor_btn = ctk.CTkButton(self.specs, corner_radius=2, fg_color="transparent", text="Doctor", border_color="#ccc", border_width=1)
        self.doctor_btn.grid(column=1, row=1, padx=3, pady=3, ipady=1)
        self.chemist_btn=ctk.CTkButton(self.specs, corner_radius=2, fg_color="transparent", text="Chemist", border_color="#ccc", border_width=1)
        self.chemist_btn.grid(column=2,row=1, padx=3, pady=3, ipady=1)

        # NAME
        self.name = ctk.CTkFrame(self, fg_color="#808080")
        self.name.grid(row=3, sticky="we", padx=80)
        self.name.grid_columnconfigure(0, weight=1)
        self.name_ntry = ctk.CTkEntry(self.name, fg_color="gray14", border_width=0, placeholder_text="Name", placeholder_text_color="#808080",  corner_radius=0)
        self.name_ntry.grid(column=0, pady=(0,2), sticky="we")

        # START BTN
        self.start_btn = ctk.CTkButton(self, corner_radius=2, fg_color="transparent", text="START", border_color="#808080", border_width=2)
        self.start_btn.grid(row=4, ipady=5, ipadx=8)