from tkinter import *


my_root = Tk()


def my_click():
    greeting = 'Hello ' + my_input.get()
    my_label = Label(my_root, text=greeting)
    my_label.pack()
    my_input.delete(0, END)  # yo!, .set, .get .place etc


my_input = Entry(my_root, width=50, fg='white', bg='blue', borderwidth=5)
my_input.pack()
# my_input.insert(0, 'Enter here')

my_button1 = Button(my_root, text='Enter your name', command=my_click)
my_button1.pack()

my_root.mainloop()
