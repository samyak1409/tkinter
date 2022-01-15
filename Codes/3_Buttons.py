from tkinter import *


my_root = Tk()


def my_click():
    my_label = Label(my_root, text='Hey!')
    my_label.pack()


my_button1 = Button(my_root, text='Click Me')
my_button2 = Button(my_root, text='Disabled', state=DISABLED)
my_button3 = Button(my_root, text='Size and Color', padx=10, pady=5, fg='white', bg='black')
my_button4 = Button(my_root, text='Command', command=my_click)

my_button1.pack()
my_button2.pack()
my_button3.pack()
my_button4.pack()

exit_button = Button(my_root, text='Exit', command=my_root.destroy)
exit_button.pack()

my_root.mainloop()
