from tkinter import *


def gui():
    root = Tk()
    root.title("_enigma")
    root.configure(width=640, height=360, background="#000000")

    button = Button(text="Start")
    button.grid(column=1, row=2)

    root.mainloop()

