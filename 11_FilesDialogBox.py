from tkinter import *
from tkinter import filedialog


main_win = Tk()
main_win.title('YEAH!!')

main_win.filename = filedialog.askopenfilename(initialdir='E:/Samyak',
                                               title='Select a file',
                                               filetypes=(('jpg file', '*.jpg'), ('all files', '*.*')))

Label(master=main_win, text=main_win.filename).pack()

main_win.mainloop()
