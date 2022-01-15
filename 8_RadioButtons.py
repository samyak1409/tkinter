# https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PL3O_UPHCHww-WBuLQSPzDR_seOF1hwMG0&index=3&t=7669s


from tkinter import *


main_win = Tk()
main_win.title('YEAH!!')

list_of_tuples = [('Samyak', 'Badminton'), ('Mantavya', 'Volleyball'), ('Sarthak', 'Football')]

game = StringVar()
game.set('Sport')

for (name, sport) in list_of_tuples:
    Radiobutton(master=main_win, text=name, value=sport, variable=game).pack()


def get_stuff(string):
    Label(master=main_win, text=string).pack()


ok_button = Button(master=main_win, text='Okay', command=lambda: get_stuff(game.get())).pack()

main_win.mainloop()
