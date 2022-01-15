from tkinter import *
from tkinter.messagebox import showerror
from datetime import datetime


date_list = []
root = Tk()


def button_1():  # ok
    start, end = startvalue.get(), endvalue.get()
    if start == '' or end == '':
        return

    try:
        start, end = datetime.strptime(start, '%d%B,%Y'), datetime.strptime(end, '%d%B,%Y')
    except ValueError:
        showerror('Invalid Value', 'Please check the format and spellings and try again.')
        return

    print(start, end)
    date_list.extend([start, end])
    root.quit()


f1 = Frame(root)
f1.pack()

Start_Date = Label(f1, text="Start Date (DDmonth,YYYY)")
Start_Date.pack()

startvalue = StringVar()
startentry = Entry(f1, textvariable=startvalue)
startentry.pack()

End_Date = Label(f1, text="End Date (DDmonth,YYYY)")
End_Date.pack()

endvalue = StringVar()
endentry = Entry(f1, textvariable=endvalue)
endentry.pack()

startentry.focus()
startentry.bind("<Return>", lambda func: endentry.focus() if startvalue.get() != '' else None)  # when pressed Enter focus shifts from one entry to another
endentry.bind('<Return>', lambda func: b1.focus() if endvalue.get() != '' else None)

f2 = Frame(root)
f2.pack()

b1 = Button(master=f2, text="OK", command=button_1)
b1.pack()

root.mainloop()
