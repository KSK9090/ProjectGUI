from tkinter import *

# widgets = Buttons, textboxes, labels, images
# windows = container to hold widgets

gui = Tk()

# ------------------- Hauptfenster -------------------
gui.geometry("700x500")
gui.title("Kundenverzeichnis")
gui.configure(bg="white")
gui.columnconfigure(0, weight=1)

brand = PhotoImage(file="brand.png")
logo = PhotoImage(file="brand.png")
gui.iconphoto(True, logo)

# ---- FUNKTIONEN ----
def suchen():
    pass

# ---- HEADER ----
header = Frame(gui, bg="grey")
header.grid(row=0, column=0, columnspan=10, sticky="nsew")
header.columnconfigure(0, weight=1)

# ---- LOGO ----
logo_label = Label(
    header,
    image=brand,
    bg="white"
)
logo_label.grid(row=0, column=1, rowspan=4, sticky="e", padx=20)

# ---- SUCHFELD ----
suchfeld_label = Label(
    header,
    text="Suchfeld:",
    font=("Arial", 14, 'bold'),
    bg="grey"
)
suchfeld_label.grid(row=0, column=0, sticky="w", padx=5)

suchfeld_eingabe = Entry(
    header,
    font=("Arial", 12),
    width=15
)
suchfeld_eingabe.grid(row=1, column=0, sticky="ew", pady=10, padx=5)

# ---- SKALA ----
skala = Scale(
    header, 
    from_= 0, to = 15, 
    orient = "horizontal",
    label="Maximale Ergebnisse",
    width="15"
    )
skala.set(0)
skala.grid(row=2, column=0, sticky="ew", pady=10, padx=5)

# ---- BUTTON SUCHE ----
suche_button = Button(header,
                      command=suchen,
                      text="suchen",
                      font=14
)
suche_button.grid(row=3, column=0, pady=10)

# ---- AUSGABE ----








gui.mainloop()
