from tkinter import *


main_win = Tk()
main_win.title('YEAH!!')


def open_win():

    other_win = Toplevel()
    other_win.title('Any but imp.')

    Label(master=other_win, text='Yeah Whatever').pack()

    Button(master=other_win, text='Close : )', command=other_win.destroy).pack()


Button(master=main_win, text='Open it : )', command=open_win).pack()

main_win.mainloop()
