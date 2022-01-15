from tkinter import *


main = Tk()

clicked = StringVar()
clicked.set('Select day from here')

drop = OptionMenu(main, clicked, 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
drop.pack()


def show():
    Label(main, text=clicked.get()).pack()


Button(main, text='Show Selection', command=show).pack()

main.mainloop()
