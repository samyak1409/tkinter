from tkinter import *


main = Tk()
main.title('YoYo')
main.iconbitmap('Mine.ico')

# Frame (that can contain other stuff!) to separate out things visually!
my_frame = LabelFrame(main, text='My Frame', padx=360, pady=180)
my_frame.pack(padx=8, pady=8)
# Putting other stuff
b = Button(my_frame, text='What\'s up?')
b.pack()  # grid can always be used!

main.mainloop()
