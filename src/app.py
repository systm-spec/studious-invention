import os
import random
import customtkinter as ctk
from PIL import Image
from customtkinter import CTkImage, CTkToplevel
from pygments.styles.dracula import background



# Initialisiere das ctk-Fenster
ctk.set_appearance_mode("light")  # Oder "dark"
ctk.set_default_color_theme("blue")  # Wähle ein Farbschema

root = ctk.CTk()  # Erstelle das Hauptfenster
root.title("Mein RPG")  # Setze den Fenstertitel
root.geometry("800x600")  # Setze die Fenstergröße



# Attributswerte
attribute = ["Kraft", "Intelligenz", "Charisma", "Wortgewandtheit", "Glaube", "Willenskraft"]
attribute_labels = {}

# Spezielle Klassenattribute
standardwerte = {
    "Barbarian": {"Kraft": 1, "Intelligenz": 1, "Willenskraft": 1, "Charisma": 0, "Wortgewandtheit": 0, "Glaube": 0},
    "Warrior": {"Kraft": 2, "Intelligenz": 0, "Willenskraft": 0, "Charisma": 1, "Wortgewandtheit": 0, "Glaube": 0},
    "Bard": {"Kraft": 0, "Intelligenz": 0, "Willenskraft": 0, "Charisma": 1, "Wortgewandtheit": 2, "Glaube": 0},
    "Mage": {"Kraft": 0, "Intelligenz": 2, "Willenskraft": 1, "Charisma": 0, "Wortgewandtheit": 0, "Glaube": 0},
    "Druid": {"Kraft": 0, "Intelligenz": 1, "Willenskraft": 0, "Charisma": 0, "Wortgewandtheit": 1, "Glaube": 1},
    "Cleric": {"Kraft": 0, "Intelligenz": 0, "Willenskraft": 1, "Charisma": 0, "Wortgewandtheit": 0, "Glaube": 2}
}

# Funktion zum Aktivieren des Startknopfs
def klasse_ausgewaehlt(event):
    start_button.configure(state="normal")  # Aktiviert den Startknopf
    klassenattribute_hinzufuegen()  # Füge die Standardwerte der gewählten Klasse hinzu

# Funktion zum Beenden des Spiels
def spiel_beenden():
    root.destroy()  # Schließt das Fenster


# Aktuelle Attribute (werden nach dem Würfeln aktualisiert)
aktuelle_attribute = {attr: 0 for attr in ["Kraft", "Intelligenz", "Charisma", "Wortgewandtheit", "Glaube", "Willenskraft"]}

# Funktion zum Würfeln der Attributswerte
def wuerfeln():
    gewaehlte_klasse = klassenauswahl.get()
    for attr in aktuelle_attribute:
        wuerfel_wert = random.randint(1, 6)  # Würfle eine Zahl zwischen 1 und 6
        aktuelle_attribute[attr] = wuerfel_wert  # Setze den Würfelwert
        attribute_labels[attr].configure(text=f"{attr}: {aktuelle_attribute[attr]}")  # Aktualisiere die Anzeige


# Funktion zum Anwenden der Klassenattribute
def klassenattribute_hinzufuegen():
    gewaehlte_klasse = klassenauswahl.get()
    if gewaehlte_klasse:  # Überprüfe, ob eine Klasse gewählt wurde
        for attr in aktuelle_attribute:
            # Addiere die Standardwerte der gewählten Klasse zu den aktuellen Attributen
            aktuelle_attribute[attr] += standardwerte[gewaehlte_klasse][attr]
            attribute_labels[attr].configure(text=f"{attr}: {aktuelle_attribute[attr]}")  # Aktualisiere die Anzeige

# Funktion für das Info-Fenster
def zeige_info():
    gewaehlte_klasse = klassenauswahl.get()
    info_text = {
        "Barbarian": "Wildheit:\n Erhöht Kraft, Intelligenz\nWillenskraft um jeweils 1.",
        "Warrior": "Kampferprobt:\n Erhöht Kraft um 2\nCharisma um 1.",
        "Bard": "Schwätzer:\n Erhöht Wortgewandtheit um 2\n Charisma um 1.",
        "Mage": "Wissen:\n Erhöht Intelligenz um 2\n Willenskraft um 1.",
        "Druid": "Naturwissen:\n Erhöht Glaube, Willenskraft\nIntelligenz um jeweils 1.",
        "Cleric": "Standhaft:\n Erhöht Willenskraft um 1\n Glaube um 2."
    }
    # Prüfen, ob das Info-Fenster bereits offen ist
    if hasattr(zeige_info, 'info_window') and zeige_info.info_window.winfo_exists():
        return  # Wenn ja, nichts tun
    zeige_info.info_window = CTkToplevel(root)
    zeige_info.info_window.title(f"Info über {gewaehlte_klasse}")

    # Positioniere das Info-Fenster in der Mitte des Hauptfensters
    x = root.winfo_x() + (root.winfo_width() // 2) - 150  # 150 ist die Breite des Fensters (Anpassen)18
    y = root.winfo_y() + (root.winfo_height() // 2) - 100  # 100 ist die Höhe des Fensters (Anpassen)
    zeige_info.info_window.geometry(f"300x200+{x}+{y}")  # Setze die Größe und Position

    info_label = ctk.CTkLabel(zeige_info.info_window, text=info_text.get(gewaehlte_klasse, "Keine Informationen verfügbar."))
    info_label.pack(padx=20, pady=20)
    # Infofenster_Schließen-Button
    close_button = ctk.CTkButton(zeige_info.info_window, text="Schließen", command=zeige_info.info_window.destroy)
    close_button.pack(pady=(0, 20))
    # Stelle sicher, dass das Info-Fenster blockiert das hauptfenster
    zeige_info.info_window.grab_set()
    zeige_info.info_window.protocol("WM_DELETE_WINDOW", zeige_info.info_window.destroy)  # Schließen des Fensters


# Funktion zur Überprüfung der Eingaben
def eingaben_pruefen():
    if (klassenauswahl.get() and rasse_var.get() != "-1" and geschlecht_var.get() != "-1"
        and name_entry.get().strip()):
        start_button.configure(state="normal")  # Aktiviere den Startbutton
    else:
        start_button.configure(state="disabled")  # Deaktiviere den Startbutton

# Funktion um das Spiel zu starten
def start_game():
    options_frame.grid_forget()
    root.geometry('800x600')

    # Hintergrundbild laden
    hintergrundbild_path = os.path.join(os.getcwd(), "images/Hintergrundlayout.jpg")
    hintergrundbild = Image.open(hintergrundbild_path)
    hintergrundbild = CTkImage(hintergrundbild, size=(800, 600))  # Passe die Größe an
    hintergrund_label = ctk.CTkLabel(root, image=hintergrundbild, text="")
    hintergrund_label.place(x=0, y=0, relwidth=1, relheight=1)

    text_frame = ctk.CTkFrame(root, image=hintergrund_option_frame)
    text_frame.place(relx=0.5, rely=0.5, anchor='center')
    ctk.CTkLabel(text_frame, text="Das Abenteuer beginnt!").grid()

    narrative_text = [
        "##########DAS DIENT NUR DER VERANSCHAULICHUNG###########",
        '############### DAMIT ICH SEHE WO DAS###################',
        '############# DAS EINGABEFELD ERSCHEINT#### ################',
        "",
        ""
    ]
    for i, line in enumerate(narrative_text):
        ctk.CTkLabel(text_frame, text=line).grid(sticky='w', padx=10, pady=2)
        if i == 2:
            give_name = ctk.CTkEntry(text_frame)
            give_name.grid(sticky='e', padx=10, pady=5)
            give_name.bind("<KeyRelease>", lambda event: enable_weiter_btn())

    def enable_weiter_btn():
        if give_name.get():
            weiter_button.configure(state='normal')
        else:
            weiter_button.configure(state='disabled')

    button_frame = ctk.CTkFrame(root)
    button_frame.place(relx=0.5, rely=0.8, anchor='center')

    back_button = ctk.CTkButton(button_frame, text='Zurück!')
    back_button.grid(row=0, column=0, padx=5)

    weiter_button = ctk.CTkButton(button_frame, text='Weiter')
    weiter_button.grid(row=0, column=1, padx=5)
    weiter_button.configure(state='disabled')

# Hintergrundbild laden und Labeln
hintergrundbild_path = os.path.join(os.getcwd(), "images/Hintergrundbild_Start.jpg")
hintergrundbild = Image.open(hintergrundbild_path)
hintergrundbild = CTkImage(hintergrundbild, size=(800, 600))  # Passe die Größe an
hintergrund_label = ctk.CTkLabel(root, image=hintergrundbild, text="")
hintergrund_label.place(x=0, y=0, relwidth=1, relheight=1)  # Setze das Label auf die gesamte Fenstergröße

# "Spieltitel/Überschrift"
spieltitel_label = ctk.CTkLabel(root, text="Willkommen bei irgendeinem Rollenspiel", font=("Helvetica", 30), bg_color="transparent")
spieltitel_label.place(relx=0.5, rely=0.1, anchor='center')  # Zentriert im oberen Bereich

# option_frame
options_frame = ctk.CTkFrame(root)
options_frame.place(relx=0.5, rely=0.4, anchor='center')  # Positioniere das Frame
#'hintergrund für optionsframe laden '
hintergrundbild_path = os.path.join(os.getcwd(), "images/optionshintergrund.jpg")
hintergrundbild = Image.open(hintergrundbild_path)
hintergrundbild = CTkImage(hintergrundbild, size=(400, 400))  # Passe die Größe an

hintergrund_option_frame = ctk.CTkLabel(options_frame, image=hintergrundbild, text="")
hintergrund_option_frame.place(x=0, y=0, relwidth=1, relheight=1)




# Eingabefeld für den Charaktername
name_entry = ctk.CTkEntry(root, width=200, placeholder_text='Gib einen Namen ein')
name_entry.place(relx=0.5, rely=0.67, anchor='center')  # Positioniere das Eingabefeld für den Namen

#### Buttons #####

# Radiobuttons für Geschlecht
geschlecht_var = ctk.StringVar(value=-1)
ctk.CTkRadioButton(options_frame, text="Männlich", variable=geschlecht_var, value="Männlich").grid(row=1, column=0, sticky='w')
ctk.CTkRadioButton(options_frame, text="Weiblich", variable=geschlecht_var, value="Weiblich").grid(row=2, column=0, sticky='w')

# Radiobuttons für Rasse
rasse_var = ctk.StringVar(value=-1)
ctk.CTkRadioButton(options_frame, text="Mensch", variable=rasse_var, value="Mensch").grid(row=1, column=1, sticky='w')
ctk.CTkRadioButton(options_frame, text="Elf", variable=rasse_var, value="Elf").grid(row=2, column=1, sticky='w')
ctk.CTkRadioButton(options_frame, text="Ork", variable=rasse_var, value="Ork").grid(row=3, column=1, sticky='w')


attribute_labels = {}
for i, attr in enumerate(attribute):  # Alle Attribute
    label = ctk.CTkLabel(options_frame, text=f"{attr}: 0")
    label.grid(row=4 + i // 2, column=0 + (i % 2), sticky='w', padx=(0, 15))  # Anpassen der Position
    attribute_labels[attr] = label


# Würfel-Button direkt im options_frame
wuerfel_button = ctk.CTkButton(options_frame, text="Würfeln", command=wuerfeln)
wuerfel_button.grid(row=7, column=0, columnspan=2, pady=10)

start_button = ctk.CTkButton(root, text="Start", command=start_game)
start_button.place(relx=0.5, rely=0.75, anchor='center')  # Zentriert im unteren Bereich
start_button.configure(state="disabled")

info_button = ctk.CTkButton(root, text="Info", command=zeige_info)
info_button.place(relx=0.5, rely=0.85, anchor='center')  # Unter dem Startknopf

quit_button = ctk.CTkButton(root, text="Beenden", command=spiel_beenden)
quit_button.place(relx=0.5, rely=0.95, anchor='center')  # Unter dem Info-Button


# Dropdown-Menü für die Klassenauswahl
klassenauswahl = ctk.CTkComboBox(options_frame, values=[
    "Barbarian", "Bard", "Warrior", "Mage", "Druid", "Cleric"],
    command=klasse_ausgewaehlt,
    state="readonly")  # Verhindert das Schreiben
klassenauswahl.grid(row=1, column=2, padx=10, pady=10)

# Bindet die Enter-Taste zum Start des Spiels
root.bind('<Return>', lambda e: start_game)

# Bindings
klassenauswahl.bind("<<ComboboxSelected>>", lambda e: eingaben_pruefen())
geschlecht_var.trace_add("write", lambda *args: eingaben_pruefen())
rasse_var.trace_add("write", lambda *args: eingaben_pruefen())
name_entry.bind("<KeyRelease>", lambda e: eingaben_pruefen())  # Überwache Tasteneingaben im Namensfeld


root.mainloop() # hier ist Ende, kein Code darunter