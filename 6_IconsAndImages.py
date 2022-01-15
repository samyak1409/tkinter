from tkinter import *
from PIL import ImageTk, Image


main = Tk()
main.title('YoYo')
main.iconbitmap('MineIcon.ico')

my_img = ImageTk.PhotoImage(Image.open('dp.jpg'))
my_label = Label(image=my_img)
my_label.pack()

main.mainloop()
