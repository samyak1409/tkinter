import tkinter as tk


window = tk.Tk()

widget = tk.Button(window)  # :)

for item in widget.keys():
    print(item, '-', widget.cget(item))
