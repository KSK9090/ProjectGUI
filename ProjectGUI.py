from tkinter import *

# widgets = Buttons, textboxes, labels, images
# windows = container to hold widgets

gui = Tk()

# ------------------- Hauptfenster -------------------
gui.geometry("500x500")
gui.title("Kundenverzeichnis")
gui.configure(bg="white")

brand = PhotoImage(file="brand.png")

logo = PhotoImage(file="logo.png")
gui.iconphoto(True, logo)

# ------------------- FRAMES -------------------
header = Frame(gui, bg="grey", height=120)
header.pack(fill="x")

content = Frame(gui, 
                bg="white"
                )
content.pack(fill="both")

"""
# Verschoben auf header frame
skala_frame = LabelFrame(
    gui, 
    bg="white"
    )
skala_frame.pack()
"""

# ------------------- LOGO NE -------------------
logo_label = Label(
    header,
    image=brand,
    bg="white"
)
logo_label.pack(side="right", padx=20, pady=10)

# ------------------- LABELS INHALT -------------------
suchfeld_label = Label(
    header,
    text="Suchfeld:",
    font=("Arial", 16, 'bold'),
    bg="grey"
)
suchfeld_label.pack(padx=5, pady=5, anchor="nw")

suchfeld_eingabe = Entry(
    header,
    font=("Arial", 12),
    width=25
)
suchfeld_eingabe.pack(anchor="nw", padx=10, pady=5)  

skala = Scale(
    header, 
    from_= 0, to = 50, 
    orient = "horizontal",
    label="Wie viele Ergebnisse sollen angezeigt werden?"
    )
skala.set(0)
skala.pack(fill="x", padx=10, pady=10)

gui.mainloop()
