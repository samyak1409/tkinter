from tkinter import *


my_root = Tk()

my_label1 = Label(my_root, text='Hello World!')
my_label2 = Label(my_root, text='I am Samyak Jain!')

my_label1.grid(row=0, column=0)
my_label2.grid(row=1, column=1, pady=(100, 200))

my_root.mainloop()
