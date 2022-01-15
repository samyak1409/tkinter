##!C:\python31##
##!/usr/bin/env python##
# Take the # before the path variable for UNIX or Windows, you can change it.
# @author: Logander4 Tutorials
# @contact: logander4@icmail.com
# @copyright: Logander4 Tutorials
# @license: GNU/GNU Public License
# @status: Stable
# @version: 2.0
###

# Imports
import tkinter
import tkinter.scrolledtext

# Hauptfenster
root = tkinter.Tk()
print("Starting TKhelp...")
root.title("Tkinter.help() RC1 1.5")
root.config(bg="lightblue")


# Funktionen
def copyright():
    print("\n(c) by Logander4 Tutorials")


def buttonf():
    but = tkinter.Toplevel(bg="lightblue", bd=2, relief="sunken", height=30, width=100)
    but.title("Widget: Button")
    bl = tkinter.Label(but,
                       text="Dies ist ein ganz normaler Button. Buttons sind in verschiedener Form\n anzeigbar. Zum Beispiel groove oder sunken. Hier ein Beispiel:\n Methode: tkinter.Button()")
    bl.pack(side=tkinter.TOP, padx=5, pady=5)
    butb = tkinter.Button(but, text="Close", command=but.destroy, relief="groove")
    butb.pack(padx=5, pady=5)


def entryf():
    ent = tkinter.Toplevel(bg="lightblue", bd=2, relief="sunken", height=30, width=100)
    ent.title("Widget: Entry")
    el = tkinter.Label(ent,
                       text="Zur einer Eingabe wird man ueber ein Entryfeld aufgerufen.\n man kann es mit Farben und Breite, sowie dem Zeichen bei Passworteingaben, ausstatten\n entry = tkinter.Entry(root)")
    el.pack(side=tkinter.TOP, padx=5, pady=5)
    ente = tkinter.Entry(ent)
    ente.pack(padx=5, pady=5)
    ente.config(bg="#CC6600")
    ente.config(fg="lightblue")

    entepwd = tkinter.Entry(ent, show="*")
    entepwd.pack(padx=5, pady=5)


def textf():
    text = tkinter.Toplevel(bg="lightblue", bd=2, relief="sunken", height=30, width=100)
    text.title("Widget: Textfield")
    txtl = tkinter.Label(text,
                         text="Ein grosses Feld zum anzeigen bzw. eingeben von Daten.\n Viele Optionen sind waehlbar\n text = tkinter.Text(root)")
    txtl.pack(side=tkinter.TOP, padx=5, pady=5)
    txt = tkinter.Text(text)
    txt.pack(padx=5, pady=5)
    txt.config(fg="lightblue")


def scrolledtextboxf():
    scrolltext = tkinter.Toplevel(bg="lightblue", bd=2, relief="sunken", height=30, width=100)
    scrolltext.title("Widget: Scrolled Textbox")
    scrolltxtl = tkinter.Label(scrolltext,
                               text="Ein Textfield das der Groesse anpassbar ist, ich meine einen Schieberegler.\n auch mit Farben geht es um \n scrolledtext = tkinter.scrolledtext.ScrolledText(root)")
    scrolltxtl.pack(side=tkinter.TOP, padx=5, pady=5)
    scrolltxt = tkinter.scrolledtext.ScrolledText(scrolltext)
    scrolltxt.pack(padx=5, pady=5)
    scrolltxt.config(bg="lightblue")
    scrolltxt.tag_config("u", underline=True)
    scrolltxt.insert("end",
                     "Hallo liebe Python Freunde,\ndiese ScrolledTextbox wird oft fuer Chatanwendungen und desgleichen genutzt,\nsozusagen als Logfile die nachher abgespeichert oder verworfen werden kann.",
                     "u")


def listboxf():
    listbox = tkinter.Toplevel(bg="lightblue", bd=2, relief="sunken", height=200, width=100)
    listbox.title("Widget: Listbox")
    listl = tkinter.Label(listbox,
                          text="The list box is a very simple list, the values of which can be read,\nOnly one selection possible\nlistbox = tkinter.Listbox (root)\nlistbox.insert ([string])")
    listl.pack(side=tkinter.TOP, padx=5, pady=5)
    listb = tkinter.Listbox(listbox)
    listb.pack(side=tkinter.BOTTOM)
    eintraege = ["Berlin", "London", "Hawai", "Paris"]

    for stadt in eintraege:
        listb.insert("end", stadt)


def radiobuttonf():
    radiobutton = tkinter.Toplevel(bd=2, relief="sunken", height=200, width=100)
    radiobutton.title("Widget: Radiobutton")
    radl = tkinter.Label(radiobutton,
                         text="Der Radiobutton wird oft in 2 oder mehrteiligen Grupen gefuehrt. Zum Auswaehlen eines Punktes,\nnur einmal auswahl moeglich\n radiobutton = tkinter.Radiobutton(root, text=[string], value=[string], variable=[string])")
    radl.pack(side=tkinter.TOP, padx=5, pady=5)

    auswahl = ["Berlin", "Moskau", "Paris", "Honolulu"]
    var = tkinter.StringVar()
    var.set("Moskau")

    for a in auswahl:
        radb = tkinter.Radiobutton(radiobutton, text=a, value=a, variable=var)
        radb.pack(side=tkinter.BOTTOM, anchor="w")


def checkbuttonf():
    checkbox = tkinter.Toplevel()
    checkbox.title("Widget: Checkbutton")
    checkl = tkinter.Label(checkbox, text="Die Checkbox ist ein Auswahlwidget mit einem Haken")
    checkl.pack(side=tkinter.TOP)
    check = tkinter.Checkbutton(checkbox, text="Ich bin ein Checkbutton")
    check.pack()


def spinboxf():
    spinbox = tkinter.Toplevel()
    spinbox.title("Widget: SpinBox")
    spinl = tkinter.Label(spinbox, text="Die Spinbox dient zum Einstellen von Zahlen!")
    spinl.pack(side=tkinter.TOP, padx=5, pady=5)
    spin = tkinter.Spinbox(spinbox, values=(1, 2, 3, 4, 5, 6))
    spin.pack(padx=5, pady=5)


def menuf():
    menu = tkinter.Toplevel()
    menu.title("Widget: Menu")

    def m():
        pass

    ml = tkinter.Label(menu,
                       text="The menu widget is a very popular widget,\nit creates the menus that can be found everywhere!")
    ml.pack(side=tkinter.TOP)

    menubar = tkinter.Menu(menu)

    # create a pulldown menu, and add it to the menu bar
    filemenu = tkinter.Menu(menu, tearoff=0)
    filemenu.add_command(label="Open", command=m)
    filemenu.add_command(label="Save", command=m)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=m)
    menubar.add_cascade(label="File", menu=filemenu)
    menu.config(menu=menubar)


def canvasf():
    canvas = tkinter.Toplevel(bg="lightblue", bd=2, relief="sunken", height=30, width=100)
    canvas.title("Widget: Canvas")
    canl = tkinter.Label(canvas,
                         text="Auf dieser Flaeche kann man zeichnen oder auch ein Bild anzeigen, In einem normalen Fenster.\n canvas = tkinter.Canvas(root, width=200, height=200)")
    canl.pack(side=tkinter.TOP, padx=5, pady=5)
    can = tkinter.Canvas(canvas, width=200, height=200)
    can.pack(padx=5, pady=5)
    can.create_oval(50, 50, 150, 150, fill="orange", width=3)
    can.create_line(50, 150, 150, 50, width=3)
    can.create_line(50, 50, 150, 150, width=3)


def labelf():
    lab = tkinter.Toplevel()
    lab.title("Widget: Label")
    labl = tkinter.Label(lab, text="Das Label ist das Steuerlement zum Anzeigen von Text!")
    labl.pack(side=tkinter.TOP, padx=5, pady=5)
    label = tkinter.Label(lab, text="Ich bin ein Label")
    label.pack(padx=5, pady=5)


# Definiere Frames
print("Definiere Frames...")
butframe = tkinter.Frame(root)
footer = tkinter.Frame(root)

# Definiere Buttons
print("Definiere Buttons...")
button = tkinter.Button(butframe, text="Button", command=buttonf)
entry = tkinter.Button(butframe, text="Entry", command=entryf)
text = tkinter.Button(butframe, text="Text", command=textf)
scrolledtextbox = tkinter.Button(butframe, text="Scrolled Textbox", command=scrolledtextboxf)
listbox = tkinter.Button(butframe, text="Listbox", command=listboxf)
radiobutton = tkinter.Button(butframe, text="Radiobutton", command=radiobuttonf)
menu = tkinter.Button(butframe, text="Menu", command=menuf)
spinbox = tkinter.Button(butframe, text="SpinBox", command=spinboxf)
canvas = tkinter.Button(butframe, text="Canvas", command=canvasf)
label = tkinter.Button(butframe, text="Label", command=labelf)
checkbutton = tkinter.Button(butframe, text="CheckButton", command=checkbuttonf)

# Fuege Spalte 1 hinzu
print("1 Spalte hinzufuegen...")
button.grid(row=1, column=1)
entry.grid(row=2, column=1)
text.grid(row=3, column=1)
spinbox.grid(row=4, column=1)

# Fuege Spalte 2 hinzu
print("2 Spalte hinzufuegen...")
scrolledtextbox.grid(row=1, column=2)
listbox.grid(row=2, column=2)
radiobutton.grid(row=3, column=2)
canvas.grid(row=4, column=2)

# Fuege 3 Spalte hinzu
print("3 Spalte hinzufuegen...")
checkbutton.grid(row=1, column=3)
label.grid(row=2, column=3)
menu.grid(row=3, column=3)

# Definiere Buttonbreite
print("Buttonbreite definieren...")
button.config(width=15)
entry.config(width=15)
text.config(width=15)
scrolledtextbox.config(width=15)
listbox.config(width=15)
radiobutton.config(width=15)
checkbutton.config(width=15)
spinbox.config(width=15)
canvas.config(width=15)
menu.config(width=15)
label.config(width=15)

# Definiere Footer
print("Footer definieren...")
copyright = tkinter.Button(footer, text="(c) by Logander4 Tutorials :: RC1 1.5", command=copyright, relief="groove")
copyright.pack()
copyright.config(bg="#CC6600")

# Starte Endlosschleife
print("Enddlosschleife starten...")
butframe.pack()
footer.pack(side=tkinter.BOTTOM)
butframe.config(bg="lightblue")
footer.config(bg="lightblue")
butframe.config(bd="5px")
butframe.config(relief="ridge")
print("Endlosschleife gestartet! Starte GUI-Anwendung!")
root.mainloop()
