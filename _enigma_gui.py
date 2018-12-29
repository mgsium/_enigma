from tkinter import *
from _enigma_classes import *


root = Tk()
root.title("_enigma")
root.configure(width=640, height=360)
#root.geometry("640x360")
root.wm_resizable(0,0)

#menu
menu = Menu(root)
root.config(menu=menu)

file = Menu(menu)
settings = Menu(menu)
menu.add_cascade(label="File", menu=file)
menu.add_cascade(label="Settings", menu=settings)

file.add_command(label="Export to .txt", command=lambda: export('txt', root, output, position_output))
file.add_command(label="Export to .csv", command=lambda: export('csv', root, output, position_output))
file.add_separator()
file.add_command(label="Exit", command=exit)

'''
#toolbar
toolbar = Frame(root)
randomize = Button(toolbar, text="randomize", command=foo)
randomize.grid(sticky=W)

toolbar.grid(sticky=N)
'''

'''
topFrame = Frame(root)
topFrame.grid()
'''

# input label and field
ilabel = Label(text="Input : ").grid(column=0, row=1, padx="10", sticky=E)

input = Entry()
input.grid(column=1, row=1, padx="20",  pady="5", sticky=E)

# output label and field
olabel = Label(text="Output : ").grid(column=0, row=2, padx="10", sticky=E)
output = Entry(state="readonly")
output.grid(column=1, row=2, padx="20", pady="5", sticky=E)

# position input
position_input = Entry()
position_input.insert(1, "a")
position_input.grid(column=2, row=1, padx=10)
#position_input.trace()

# position output
position_output = Entry(state="readonly")
position_output.grid(column=2, row=2, padx=10)

# encrypt button
encrypt_button = Button(
    text="Encrypt",
    fg="white",
    bg="brown",
    command=lambda : display_message(input, output, rotor1, rotor2, rotor3, ref1, status_bar, 'e', position_output, position_input)
)
encrypt_button.grid(column=1, row=3, padx="20", sticky=E)

# decrypt button
decrypt_button = Button(
    text="Decrypt",
    fg="white",
    bg="brown",
    command=lambda : display_message(input, output, rotor1, rotor2, rotor3, ref1, status_bar, 'd', position_output, position_input)
)
decrypt_button.grid(column=1, row=3, padx="20", sticky=W)


# clear button
clear = Button(
    text="Clear",
    command=lambda : clear_field(input, output, position_input, position_output)
).grid(column=2, row=3, padx="10", sticky=E)

reset = Button(
    text="Reset",
    command=lambda : rotor1.reset()
).grid(column=2, row=3, padx="10", sticky=W)


# status bar
root.grid_columnconfigure(0, weight=1)
status_bar = Label(text = "enigma simulator", relief=SUNKEN, anchor=W, font="courier 10 italic")
status_bar.grid(sticky=W, column=0,row=4, columnspan=3)

