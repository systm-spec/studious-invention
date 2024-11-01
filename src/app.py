import customtkinter as ctk
from PIL import Image
import os
from src.util.windows import check_for_windows
check_for_windows()
app = ctk.CTk()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("./config/theme/custom.json")
app.title("RPG")
app.geometry("680x720")



# Mainframe - Start Menu
start_menu_frame = ctk.CTkFrame(app, fg_color="transparent")
start_menu_frame.pack(fill="both", expand=True, padx=120, pady=240)
start_menu_frame.grid_columnconfigure(0, weight=1)
start_menu_frame.grid_rowconfigure((0,1), weight=1)

# Subframes - Start Menu
# Label-Frame
title_lbl_frame = ctk.CTkFrame(start_menu_frame, fg_color="#808080")
title_lbl_frame.grid(column=0, row=0)
title_lbl_frame.grid_columnconfigure(0, weight=0)
# Label
title_lbl = ctk.CTkLabel(title_lbl_frame, text="RPG GAME", fg_color="gray14", text_color="#EFEFEF", font=("Inter", 24))
title_lbl.grid(padx=2, pady=2, ipadx=140, ipady=20)

# buttons-frame
title_btn_frame = ctk.CTkFrame(start_menu_frame )
title_btn_frame.grid(column=0, row=1)
# buttons
start_btn = ctk.CTkButton(title_btn_frame, fg_color="transparent", corner_radius=2, text="Start" )
start_btn.grid(ipadx=3, ipady=4, column=0, row=0)
quit_btn = ctk.CTkButton(title_btn_frame, fg_color="transparent", corner_radius=2, text="Quit")
quit_btn.grid(ipadx=3, ipady=4, column=1, row=0)

app.mainloop()