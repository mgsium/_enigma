from tkinter import *
from tkinter import ttk
from _enigma_classes import *

# window setup
root = Tk()
root.title("_enigma")
root.wm_resizable(0,0)

# main frame

main = LabelFrame(root, text="Control")
main.pack(padx=5, pady=5, ipadx=5, ipady=5)

#menu
menu = Menu(root)
root.config(menu=menu)

# menu bar setup
file = Menu(menu)
settings = Menu(menu)
menu.add_cascade(label="File", menu=file)
menu.add_cascade(label="Settings", menu=settings)

# file section of the menu bar
file.add_command(label="Export to .txt", command=lambda: export('txt', root, output, position_output))  # adds export to txt option
file.add_command(label="Export to .csv", command=lambda: export('csv', root, output, position_output))  # adds export to csv option
file.add_separator()
file.add_command(label="Exit", command=exit)

# settings section of the menu bar
settings.add_command(label="Change Rotor", command=lambda: rotor_settings(r_settings))
settings.add_command(label="Change Reflector", command=lambda: reflector_settings(ref))

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
ilabel = ttk.Label(main, text="Input : ").grid(column=0, row=1, padx="10", sticky=E)
input = ttk.Entry(main)
input.grid(column=1, row=1, padx="20",  pady="5", sticky=E)

# output label and field
olabel = ttk.Label(main, text="Output : ").grid(column=0, row=2, padx="10", sticky=E)
output = ttk.Entry(main, state="readonly")
output.grid(column=1, row=2, padx="20", pady="5", sticky=E)

# position input
position_input = ttk.Entry(main)
#position_input.insert(1, "a")
position_input.grid(column=2, row=1, padx=10)
#position_input.trace()

# position output
position_output = ttk.Entry(main, state="readonly")
position_output.grid(column=2, row=2, padx=10)

# encrypt button
encrypt_button = ttk.Button(
    main,
    text="Encrypt",
    command=lambda : display_message(input, output, r_settings.first, r_settings.second, r_settings.third, ref['chosen'], status_bar, 'e', position_output, position_input)
)
encrypt_button.grid(column=1, row=3, padx="20")

# decrypt button
decrypt_button = ttk.Button(
    main,
    text="Decrypt",
    command=lambda : display_message(input, output, r_settings.first, r_settings.second, r_settings.third, ref['chosen'], status_bar, 'd', position_output, position_input)
)
decrypt_button.grid(column=1, row=4, padx="20")


# clear button - clears the fields
clear = ttk.Button(
    main,
    text="Clear",
    command=lambda : clear_field(input, output, position_input, position_output)
).grid(column=2, row=3, padx="10")

# reset button - resets rotor positioning
reset = ttk.Button(
    main,
    text="Reset",
    command=lambda : rotor_classes[0].reset()
).grid(column=2, row=4, padx="10")


# status bar
root.grid_columnconfigure(0, weight=1)
status_bar = ttk.Label(text = "enigma simulator", relief=SUNKEN, anchor=W, font="courier 10 italic")
status_bar.pack(fill=X)

