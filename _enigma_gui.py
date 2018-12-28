from tkinter import *
from _enigma_classes import *


root = Tk()
root.title("_enigma")
root.configure(width=640, height=360)
#root.geometry("640x360")
root.wm_resizable(0,0)

'''
topFrame = Frame(root)
topFrame.grid()
'''

# input label and field
ilabel = Label(text="INPUT : ")
ilabel.grid(column=0, row=1, padx="10", sticky=E)

input = Entry()
input.grid(column=1, row=1, padx="20",  pady="5", sticky=E)

# output label and field
olabel = Label(text="OUTPUT : ")
olabel.grid(column=0, row=2, padx="10", sticky=E)

output = Entry(state="readonly")
output.grid(column=1, row=2, padx="20", pady="5", sticky=E)

# submit button
button = Button(
    text="submit",
    fg="white",
    bg="brown",
    command=lambda : display_message(input, output, rotor1, rotor2, rotor3, ref1, status_bar))
button.grid(column=1, row=3, padx="20", sticky=E)

# clear button
clear = Button(
    text="clear",
    command=lambda : clear_field(output)
)
clear.grid(column=1, row=3, padx="20", sticky=W)

# status bar
status_bar = Label(text = "enigma emulator", relief=SUNKEN, anchor=W, font="courier 10 italic")
status_bar.grid(sticky=W, column=0,row=4, columnspan=2)

