from tkinter import *


def gui():
    root = Tk()
    root.title("_enigma")
    root.configure(width=640, height=360)
    root.geometry("640x360")

    '''
    topFrame = Frame(root)
    topFrame.grid()
    '''

    # input label and field
    ilabel = Label(text="INPUT : ")
    ilabel.grid(column=0, row=0, padx="20", sticky=E)

    input = Entry()
    input.grid(column=1, row=0, sticky=E)

    # output label and field
    olabel = Label(text="OUTPUT : ")
    olabel.grid(column=0, row=1, padx="20", sticky=E)

    output = Entry()
    output.grid(column=1, row=1, sticky=E)

    # submit button
    button = Button(text="Submit", fg="white", bg="brown")
    button.grid(column=1, row=2, padx="20", sticky=N)

    root.mainloop()

