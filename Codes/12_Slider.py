from tkinter import *


main = Tk()
main.geometry('720x360')

vertical = Scale(main, from_=180, to=360)
vertical.pack()

horizontal = Scale(main, from_=360, to=720, orient=HORIZONTAL)
horizontal.pack()


def clicked():  # one use!
    main.geometry(f'{horizontal.get()}x{vertical.get()}')


Button(main, text='ChangeWindowsSize', command=clicked).pack()

main.mainloop()
