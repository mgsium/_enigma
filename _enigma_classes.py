from _enigma_inputs import *
import string

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
        for letter in self.beta:
            if self.beta.index(letter) == 25:
                new_beta[0] = letter
            else:
                new_beta[self.beta.index(letter) + 1] = letter
        self.beta = new_beta

    # before reflection
    def forward_sub(self, letter):
        return self.beta[string.ascii_lowercase.index(letter)]

    # after reflection
    def backward_sub(self, letter):
        return string.ascii_lowercase[self.beta.index(letter)]

# ---FUNCTIONS---
def display_message(field, ofield, rt1, rt2, rt3, ref, status):
    status.config(text="enigma emulator")
    invalid = False
    message = list(str(field.get()))
    print(message)
    for spec in message:
        if spec not in string.ascii_lowercase:
            del message[message.index(spec)]
            invalid = True

    message = ''.join(message)

    if invalid == True:
        status.config(text="special characters removed")

    if len(message) != 0:
        ofield.config(state="normal")
        for letter in message:
            ofield.insert(10, encrypt(rt1, rt2, rt3, letter.lower(), ref))
        ofield.config(state="readonly")
        field.delete(first=0, last=len(field.get()))

def clear_field(field):
    field.config(state="normal")
    field.delete(first=0, last=len(field.get()))
    field.config(state="readonly")

def encrypt(rt1, rt2, rt3, letter, ref):

    for rotor in [rt1, rt2, rt3]:
        ###
        rt1.beta=r1['beta']
        rt2.beta = r2['beta']
        rt3.beta = r3['beta']
        ###

        # offsets the rotor to the requires setting
        for i in range(string.ascii_lowercase.index(rotor_pos)):
            rotor.frotate()

    letter = pb.value_check(letter)
    letter = rt3.forward_sub(rt2.forward_sub(rt1.forward_sub(letter)))  # runs the rotors in forward order
    letter = ref.forward_sub(letter)  # runs the reflector
    letter = rt1.backward_sub(rt2.backward_sub(rt3.backward_sub(letter)))  # runs the rotors in backwards order
    return letter

def decrypt(rt1, rt2, rt3, letter, ref):
    letter = rt3.forward_sub(rt2.forward_sub(rt1.forward_sub(letter)))  # runs the rotors in forward order
    letter = ref.backward_sub(letter)  # runs the reflector
    letter = rt1.backward_sub(rt2.backward_sub(rt3.backward_sub(letter)))  # runs the rotors in backwards order
    letter = pb.value_check(letter)

    for rotor in [rt1, rt2, rt3]:
        # offsets the rotor to the requires setting
        for i in range(string.ascii_lowercase.index(rotor_pos)):
            rotor.brotate()

    return letter

#initiating class instances
pb = PlugBoard(default_pbset)

ref1 = Rotor(ref1)

rotor1 = Rotor(r1['beta'])
rotor2 = Rotor(r2['beta'])
rotor3 = Rotor(r3['beta'])
