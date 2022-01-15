"""Wrapper functions for Tcl/Tk.

Tkinter provides classes which allow the display, positioning and
control of widgets. Toplevel widgets are Tk and Toplevel. Other
widgets are Frame, Label, Entry, Text, Canvas, Button, Radiobutton,
Checkbutton, Scale, Listbox, Scrollbar, OptionMenu, Spinbox
LabelFrame and PanedWindow.

Properties of the widgets are specified with keyword arguments.
Keyword arguments have the same name as the corresponding resource
under Tk.

Widgets are positioned with one of the geometry managers Place, Pack
or Grid. These managers can be called with methods place, pack, grid
available in every Widget.

Actions are bound to events by resources (e.g. keyword argument
command) or with the method bind.

Example (Hello, World):"""


from tkinter import *


main = Tk()

frame = Frame(master=main, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH, expand=1)

label = Label(master=frame, text="Hello, World")
label.pack(fill=X, expand=1)

button = Button(master=frame, text="Exit", command=main.destroy)
button.pack(side=BOTTOM)

main.mainloop()
