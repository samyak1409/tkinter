from tkinter import *


main = Tk()

var_a = IntVar()
var_b = IntVar()
var_c = IntVar()

a = Checkbutton(main, text='Badminton', variable=var_a).pack()
b = Checkbutton(main, text='TableTennis', variable=var_b).pack()
c = Checkbutton(main, text='Cricket', variable=var_c).pack()


def do():
    Label(main, text=f'{var_a.get()}, {var_b.get()}, {var_c.get()}').pack()


Button(main, text='Done', command=do).pack()

main.mainloop()
