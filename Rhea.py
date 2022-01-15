# DATE INPUT


from tkinter import *
from tkcalendar import DateEntry


window = Tk()  # window initialisation
window.title('Date Input')
window.geometry('192x108')  # 'widthxheight'


Label(master=window, text='Start Date:').pack()  # pack()- a way to fix a widget in main window ('window')

# start_date = StringVar()  # a var which will hold the str data being written to Entry widget
# Entry(master=window, textvariable=start_date).pack()
start_date = DateEntry(window, width=12, background='darkblue', foreground='white', borderwidth=2, year=2010)
start_date.pack()


Label(master=window, text='End Date:').pack()

# end_date = StringVar()
# Entry(master=window, textvariable=end_date).pack()
end_date = DateEntry(window, width=12, background='darkblue', foreground='white', borderwidth=2, year=2010)
end_date.pack()


def get_data():
    start_date_ = start_date.get()  # get()- will get the str data from entry widget
    end_date_ = end_date.get()
    print(start_date_, end_date_)  # debugging
    # start_date.set('')  # erasing the inputted data
    # end_date.set('')
    window.quit()  # if u want the window to close after taking input (implicitly)


Button(master=window, text='Ok', command=get_data).pack()  # at the press of button, we are taking the input

window.mainloop()  # the main window loops(come and go) all the time to track all the actions and be visible

# Label, Entry, Button- widgets
