from _enigma_inputs import *
from tkinter import *
from tkinter import filedialog, ttk, messagebox
import string, math, csv, datetime

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
        self.obeta = beta

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
        while self.beta[0] != self.obeta[0]:
            self.frotate()

    # before reflection
    def forward_sub(self, letter):
        return self.beta[string.ascii_lowercase.index(letter)]  # substitutes letter in the forward direction

    # after reflection
    def backward_sub(self, letter):
        return string.ascii_lowercase[self.beta.index(letter)]  # substitutes letter in the backward direction


class RotorSettings:
    def __init__(self, def1, def2, def3, def4, def5):
        self.first = Rotor(def1['beta'])
        self.second = Rotor(def2['beta'])
        self.third = Rotor(def3['beta'])
        self.choices = ["I", "II", "III", "IV", "V"]
        self.dchoices = [1, 2, 3, 4, 5]
        self.rotor_betas = [d['beta'] for d in [def1, def2, def3, def4, def5]]

    def set_first(self, input_rotor):
        self.first = [self.dchoices[input_rotor], self.choices[input_rotor]]
        self.choices.remove(self.choices[input_rotor])
        self.dchoices.remove(self.dchoices[input_rotor])

    def set_second(self, input_rotor):
        self.second = [self.dchoices[input_rotor], self.choices[input_rotor]]
        self.choices.remove(self.choices[input_rotor])
        self.dchoices.remove(self.dchoices[input_rotor])

    def set_third(self, input_rotor):
        self.third = [self.dchoices[input_rotor], self.choices[input_rotor]]
        self.choices.remove(self.choices[input_rotor])
        self.dchoices.remove(self.dchoices[input_rotor])

    def rotorize(self):
        self.first =  Rotor(self.rotor_betas[self.first[0]-1])
        self.second = Rotor(self.rotor_betas[self.second[0] - 1])
        self.third = Rotor(self.rotor_betas[self.third[0] - 1])

    def autoset(self, input_rotor):
        if self.first == []:
            self.set_first(input_rotor)
        elif self.second == []:
            self.set_second(input_rotor)
        elif self.third == []:
            self.set_third(input_rotor)

    def clear(self):
        self.first, self.second, self.third =[], [], []

# ---FUNCTIONS---
def display_message(field, ofield, rt1, rt2, rt3, ref, status, process, pos_out, pos_in):
    status.config(text="enigma emulator")  # changes the status bar text
    invalid = False
    message = field.get()  # stores the input string
    for spec in message:
        #removes special characters
        if spec not in string.ascii_lowercase:
            message = list(message)
            del message[message.index(spec)]
            message = ''.join(message)
            invalid = True

    message = ''.join(message)  # converts the message list to a string

    if invalid:
        status.config(text="special characters removed")  # outputs message if special characters have been removed

    if len(message) != 0 and (len(pos_in.get()) == 3 or len(pos_in.get()) == 0):
        i = 0
        current_message, output_message = '', []

        # rotor positioning
        if len(pos_in.get()) == 3:
            # offsets the rotor to the required setting
            while rt1.beta[0] != pos_in.get()[0]:
                rt1.frotate()
            while rt2.beta[0] != pos_in.get()[1]:
                rt2.frotate()
            while rt3.beta[0] != pos_in.get()[2]:
                rt3.frotate()

        '''
        for x in range(math.ceil(len(message)/10)):
            current_message = message[i: i+10]
            i+=10
            ofield.config(state="normal")
            if process == 'e':
                for letter in current_message:
                    current_letter, position = encrypt(rt1, rt2, rt3, letter.lower(), ref)
                    ofield.insert(100, current_letter)
            elif process == 'd':
                # decrypts each letter
                for letter in current_message[::-1]:
                    current_letter, position = decrypt(rt1, rt2, rt3, letter.lower(), ref)
                    output_message += current_letter
                ofield.insert(100, ''.join(output_message[::-1])) # inserts the decrypted message into the output field
            ofield.config(state="readonly")
        '''

        current_message = message
        ofield.config(state="normal")
        if process == 'e':
            for letter in current_message:
                current_letter, position = encrypt(rt1, rt2, rt3, letter.lower(), ref)
                ofield.insert(100, current_letter)
        elif process == 'd':
            # decrypts each letter
            for letter in current_message[::-1]:
                current_letter, position = decrypt(rt1, rt2, rt3, letter.lower(), ref)
                output_message += current_letter
            ofield.insert(100, ''.join(output_message[::-1]))  # inserts the decrypted message into the output field
        ofield.config(state="readonly")

        field.delete(first=0, last=len(field.get()))

        try:
            pos_out.config(state="normal")
            pos_out.delete(first=0, last=len(pos_out.get()))
            pos_out.insert(10, ''.join(position))
        except UnboundLocalError:
            pass
        pos_out.config(state="readonly")
    else:
        status.config(text="enter a message and rotor positions")


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
    '''
    if rt1.beta[0] == rt1.obeta[0]:
        rt2.frotate()
    '''
    return letter, [rt1.beta[0], rt2.beta[0], rt3.beta[0]]

def decrypt(rt1, rt2, rt3, letter, ref):

    '''
    if rt1.beta[0] == rt1.obeta[0]:
        rt2.brotate()
    '''

    rt1.brotate()
    letter = rt3.forward_sub(rt2.forward_sub(rt1.forward_sub(letter)))  # runs the rotors in forward order
    letter = ref.backward_sub(letter)  # runs the reflector
    letter = rt1.backward_sub(rt2.backward_sub(rt3.backward_sub(letter)))  # runs the rotors in backwards order
    letter = pb.value_check(letter)
    print(letter)
    return letter, [rt1.beta[0], rt2.beta[1], rt3.beta[2]]

def export(file_type, master, o_field, o_pos):
    while True:
        try:
            if file_type == "txt":
                master.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                                    filetypes=(("Text", "*.txt"), ("All files", "*.*")))
                f = open(master.filename, "a")
                # exports the message in a user-friendly format
                f.write(f"\n===================\nEncrypted message : {o_field.get()} "
                        f"\nRotor 1 position : {o_pos.get()[0]}"
                        f"\nRotor 2 position : {o_pos.get()[1]}"
                        f"\nRotor 3 position : {o_pos.get()[2]}"
                        f"\nTime : {datetime.datetime.now()}\n===================\n")
            elif file_type == "csv":
                master.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                                    filetypes=(("Comma Separated Values (csv)", "*.csv"), ("All files", "*.*")))
                f = open(master.filename, "a")
                f_writer = csv.writer(f, delimiter=",")
                f_writer.writerow([o_field.get(), o_pos.get(), datetime.datetime.now()])
            break
        except FileNotFoundError:  # ignores files that do not exist
            break

def rotor_settings(s):
    s.clear()
    # settings window
    rs = Toplevel()
    rs.title("rotor settings")
    rs.wm_resizable(0, 0)

    rs.grab_set() # makes only the popup selectable

    # rotor labelframe
    rotors_frame = LabelFrame(rs, text="Rotors")
    rotors_frame.grid(row=0, column=0, padx=5, pady=5, ipadx=5, ipady=5)

    rotors = Listbox(rotors_frame)
    rotors.grid(row=0, column=0, padx=5, pady=5)

    #controls labelframe
    controls_frame = LabelFrame(rs, text="Controls")
    controls_frame.grid(row=0, column=1, padx=5, pady=5)

    rotor_labels = []


    for rotor in ["I", "II", "III", "IV", "V"]:
        rotors.insert(END, rotor)

    add = ttk.Button(controls_frame, text="Add", command=lambda: add_to_selection(rs, rotors, s) )
    add.grid(row=0, column=0, sticky=N)

def add_to_selection(main, list, s):
    try:
        s.autoset(list.curselection()[0])
        list.delete(list.curselection()[0])

        if s.third!=[]:
            main.destroy()
            messagebox.showinfo(
                title="alert",
                message=f"Rotor 1 : {s.first[1]}\nRotor 2 : {s.second[1]}\nRotor 3 : {s.third[1]}"
            )
            for i in [s.first, s.second, s.third]:
                i = rotor_classes[i[0]]
                print(i)

            s.rotorize()
            print(s)

        print(s.first, s.second, s.third)
    except IndexError:
        pass

def reflector_settings(ref):
    # settings window
    refs = Toplevel()
    refs.title("reflector settings")
    refs.wm_resizable(0, 0)

    ref_a_button = ttk.Button(refs, text="A", command=lambda: set_ref(ref, 0, refs)).pack()
    ref_b_button = ttk.Button(refs, text="B", command=lambda: set_ref(ref, 1, refs)).pack()
    ref_c_button = ttk.Button(refs, text="C", command=lambda: set_ref(ref, 2, refs)).pack()

def set_ref(ref, index, window):
    ref['chosen'] = ref['all'][index]
    window.destroy()



#initiating class instances
pb = PlugBoard(default_pbset)

ref_a = Rotor(A)
ref_b = Rotor(B)
ref_c = Rotor(C)

ref = {
    'chosen': ref_a,
    'all':[ref_a, ref_b, ref_c]
}

r_settings = RotorSettings(r1, r2, r3, r4, r5)

rotor_classes = [Rotor(r1['beta']),Rotor(r2['beta']), Rotor(r3['beta']),  Rotor(r4['beta']),  Rotor(r5['beta'])]

