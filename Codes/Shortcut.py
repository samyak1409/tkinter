from tkinter import Tk, Button, Event
from tkinter.messagebox import askyesno


window = Tk()


def func(event: Event = None):  # we have bind it with an event (ctrl+q) so we have to pass the event in the func (it's just like that.)
    if askyesno('QUIT', 'Are you sure?'):
        window.quit()


butt = Button(text='Quit', command=func)
butt.pack()

# butt.bind_all('<Control-q>', func)
window.bind('<Control-q>', func)  # both functions same.

window.mainloop()
