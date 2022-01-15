from tkinter import *
from tkinter import font


root = Tk()
root.title('Font Families')
fonts = list(font.families())
fonts.sort()


def populate(frame):
    """Put in the fonts"""
    list_num = 1
    for item in fonts:
        Label(frame, text=item, font=(item, 16)).pack()
        list_num += 1


def onFrameConfigure(canvas):
    """Reset the scroll region to encompass the inner frame"""
    canvas.configure(scrollregion=canvas.bbox("all"))


canvas = Canvas(root, borderwidth=0, background="#ffffff")
frame = Frame(canvas, background="#ffffff")
vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4, 4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

populate(frame)

print(font.families())  # :)

root.mainloop()
