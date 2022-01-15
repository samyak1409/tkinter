from tkinter import *
from PIL import ImageTk, Image


main = Tk()
main.title('YoYo')
main.iconbitmap('Mine.ico')

my_img = ImageTk.PhotoImage(Image.open('DP.jpg'))
my_label = Label(image=my_img)
my_label.pack()

main.mainloop()
