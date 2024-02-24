from tkinter import *
from time import *


def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    time_label.after(1000, update)


window = Tk()

window.title("Digital Clock by Saiful")
time_label = Label(window, font=("Arial", 50), fg="#00ff00", bg="black")
time_label.pack()

day_label = Label(window, font=("Ink Free", 30), fg="black")
day_label.pack()

date_label = Label(window, font=("Ink Free", 20), fg="black")
date_label.pack()

update()

window.mainloop()
