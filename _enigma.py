from _enigma_classes import *
from _enigma_inputs import *
from _enigma_gui import *

gui()  # initiates the gui

pb = PlugBoard(default_pbset)


def encrypt(rt1, rt2, rt3, letter, ref):

    for rotor in [rt1, rt2, rt3]:
        # offsets the rotor to the requires setting
        for i in range(string.ascii_lowercase.index(rotor_pos)):
            rotor.frotate()

    letter = pb.value_check(letter)
    letter = rt3.forward_sub(rt2.forward_sub(rt1.forward_sub(letter)))  # runs the rotors in forward order
    letter = ref.forward_sub(letter)  # runs the reflector
    letter = rt1.backward_sub(rt2.backward_sub(rt3.backward_sub(letter))) # runs the rotors in backwards order
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



ref1 = Rotor(ref1)

rotor1 = Rotor(r1['beta'])
rotor2 = Rotor(r2['beta'])
rotor3 = Rotor(r3['beta'])

print(f"OUTPUT : {encrypt(rotor1, rotor2, rotor3, 'z', ref1)}")

print(f"INPUT : {decrypt(rotor1, rotor2, rotor3, 'd', ref1)}")

'''
print(rotor3.rotate())
print(rotor3.forward_sub("a"))
print(rotor3.backward_sub('d'))

set = PlugBoard(default_pbset)
set.value_check('a')
'''