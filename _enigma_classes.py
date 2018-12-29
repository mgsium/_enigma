from _enigma_inputs import *
from tkinter import filedialog
import string
import math
import csv
import datetime

# ---CLASSES---
class PlugBoard:
    def __init__(self, settings):
        self.settings = settings

    def value_check(self, letter):
        for pair in self.settings:
            if letter in pair:
                for value in pair:
                    if value != letter:
                        return value
            else:
                return letter

class Rotor:
    def __init__(self, beta):
        self.beta = beta

    # rotate the rotor
    def frotate(self):
        new_beta = [0 for i in range(26)]
        for letter in self.beta:
            if self.beta.index(letter) == 0:
                new_beta[25] = letter
            else:
                new_beta[self.beta.index(letter)-1] = letter
        self.beta = new_beta

    def brotate(self):
        new_beta = [0 for i in range(26)]
        for letter in self.beta[::-1]:
            if self.beta.index(letter) == 25:
                new_beta[0] = letter
            else:
                new_beta[self.beta.index(letter) + 1] = letter
        self.beta = new_beta

    def reset(self):
        pass

    # before reflection
    def forward_sub(self, letter):
        return self.beta[string.ascii_lowercase.index(letter)]

    # after reflection
    def backward_sub(self, letter):
        return string.ascii_lowercase[self.beta.index(letter)]

# ---FUNCTIONS---
def display_message(field, ofield, rt1, rt2, rt3, ref, status, process, pos_out, pos_in):
    status.config(text="enigma emulator")
    invalid = False
    for spec in message:
        if spec not in string.ascii_lowercase:
            del message[message.index(spec)]
            invalid = True

    message = ''.join(message)

    if invalid:
        status.config(text="special characters removed")

    if len(message) != 0:
        i = 0
        current_message, output_message = '', []
        for x in range(math.ceil(len(message)/10)):
            current_message = message[i: i+10]
            i+=10
            ofield.config(state="normal")
            if process == 'e':
                for letter in current_message:
                    current_letter, position = encrypt(rt1, rt2, rt3, letter.lower(), ref)
                    ofield.insert(100, current_letter)
            elif process == 'd':
                # offsets the rotor to the required setting
                while rt1.beta[0] != pos_in.get():
                    rt1.frotate()
                # decrypts each letter
                for letter in current_message[::-1]:
                    current_letter, position = decrypt(rt1, rt2, rt3, letter.lower(), ref)
                    output_message += current_letter
                ofield.insert(100, ''.join(output_message[::-1])) # inserts the decrypted message into the output field
            ofield.config(state="readonly")

        field.delete(first=0, last=len(field.get()))

        while True:
            try:
                pos_out.config(state="normal")
                pos_out.delete(first=0, last=len(pos_out.get()))
                pos_out.insert(10, position)
                break
            except UnboundLocalError:
                break
        pos_out.config(state="readonly")


def clear_field(i, o, i_pos, o_pos):
    for field in [i, o, i_pos, o_pos]:
        field.config(state="normal")
        field.delete(first=0, last=len(field.get()))
    o.config(state="readonly")
    o_pos.config(state="readonly")


def encrypt(rt1, rt2, rt3, letter, ref):
    letter = pb.value_check(letter)
    letter = rt3.forward_sub(rt2.forward_sub(rt1.forward_sub(letter)))  # runs the rotors in forward order
    letter = ref.forward_sub(letter)  # runs the reflector
    letter = rt1.backward_sub(rt2.backward_sub(rt3.backward_sub(letter)))  # runs the rotors in backwards order
    rt1.frotate()
    return letter, rt1.beta[0]

def decrypt(rt1, rt2, rt3, letter, ref):
    rt1.brotate()
    letter = rt3.forward_sub(rt2.forward_sub(rt1.forward_sub(letter)))  # runs the rotors in forward order
    letter = ref.backward_sub(letter)  # runs the reflector
    letter = rt1.backward_sub(rt2.backward_sub(rt3.backward_sub(letter)))  # runs the rotors in backwards order
    letter = pb.value_check(letter)
    print(letter)

    return letter, rt1.beta[0]

def export(file_type, master, o_field, o_pos):
    while True:
        try:
            if file_type == "txt":
                master.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                                    filetypes=(("Text", "*.txt"), ("All files", "*.*")))
                f = open(master.filename, "a")
                f.write(f"\n===================\nEncrypted message : {o_field.get()} \nPosition : {o_pos.get()}\nTime : {datetime.datetime.now()}\n===================\n")
            elif file_type == "csv":
                master.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                                    filetypes=(("Comma Separated Values (csv)", "*.csv"), ("All files", "*.*")))
                f = open(master.filename, "a")
                f_writer = csv.writer(f, delimiter=",")
                f_writer.writerow([o_field.get(), o_pos.get(), datetime.datetime.now()])
            break
        except FileNotFoundError:
            break

#initiating class instances
pb = PlugBoard(default_pbset)

ref1 = Rotor(ref1)

rotor1 = Rotor(r1['beta'])
rotor2 = Rotor(r2['beta'])
rotor3 = Rotor(r3['beta'])

for rotor in [rotor1, rotor2, rotor3]:
    rotor1.beta = r1['beta']
    rotor2.beta = r2['beta']
    rotor3.beta = r3['beta']