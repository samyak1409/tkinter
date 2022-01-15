from tkinter import *
from tkinter import messagebox


main_win = Tk()
main_win.title('YEAH!!')


'''
    print("info", showinfo("Spam", "Egg Information"))
    print("warning", showwarning("Spam", "Egg Warning"))
    print("error", showerror("Spam", "Egg Alert"))
    print("question", askquestion("Spam", "Question?"))
    print("proceed", askokcancel("Spam", "Proceed?"))
    print("yes/no", askyesno("Spam", "Got it?"))
    print("yes/no/cancel", askyesnocancel("Spam", "Want it?"))
    print("try again", askretrycancel("Spam", "Try again?"))
'''


def pop_up():
    # messagebox.showinfo('Information', 'Some random but important information 😘😘')
    # messagebox.showwarning('Information', 'Some random but important information 😘😘')
    # messagebox.showerror('Information', 'Some random but important information 😘😘')
    # messagebox.askquestion('Information', 'Some random but important information 😘😘')
    # messagebox.askokcancel('Information', 'Some random but important information 😘😘')
    response = messagebox.askyesno('Information', 'Some random but important information 😘😘')

    if response:
        Label(master=main_win, text=': )').pack()
    else:
        Label(master=main_win, text=': (').pack()


Button(master=main_win, text='GetInfo', command=pop_up).pack()

main_win.mainloop()
