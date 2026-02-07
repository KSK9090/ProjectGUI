from tkinter import *
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    database="projectGUI"
)
cursor = conn.cursor()

# ---- HAUPTFENSTER ----
gui = Tk()
gui.geometry("700x500")
gui.title("Kundenverzeichnis")
gui.configure(bg="white")
gui.columnconfigure(0, weight=1)

brand = PhotoImage(file="brand.png")
logo = PhotoImage(file="brand.png")
gui.iconphoto(True, logo)

# ---- FUNKTIONEN ----
def suchen():
    suchwort_input = suchfeld_eingabe.get().strip()
    if not suchwort_input:
        text = "Bitte Suchwort eingeben."
    else:
        suchwort = "%" + suchwort_input + "%"
        sql = "SELECT * FROM Firmenname WHERE Ansprechpartner LIKE %s LIMIT %s"
        cursor.execute(sql, (suchwort, skala.get()))
        ergebnisse = cursor.fetchall()
        if ergebnisse:
            text = ""
            for row in ergebnisse:
                text += f"{row[0]} | {row[1]} | {row[2]}\n"
        else:
            text = "Keine Treffer gefunden. Für Testzwecke bitte Muster, Mustermann oder Musterfrau eingeben und den Slider anpassen."

    if not hasattr(gui, "ergebnis_label"):
        gui.ergebnis_label = Label(gui, text=text, justify="left", bg="white")
        gui.ergebnis_label.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    else:
        gui.ergebnis_label.config(text=text)


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








gui.mainloop()
