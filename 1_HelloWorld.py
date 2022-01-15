from tkinter import *  # importing everything

# in tkinter(t-k-inter(interface)), everything is widget! (not nepal or vinod; (vijit))

# top-level widget!
my_root = Tk()
my_root.geometry('720x360')

# creating a label widget
my_label = Label(my_root, text='Hello World!')

# shoving(pushing) onto the screen
my_label.pack()

my_root.mainloop()
