from _enigma_classes import *
from _enigma_inputs import *


def encrypt(rt1, rt2, rt3, letter, ref):
    letter = rt3.forward_sub(rt2.forward_sub(rt1.forward_sub(letter)))  # runs the rotors in forward order
    letter = ref.forward_sub(letter)  # runs the reflector
    letter = rt3.backward_sub(rt2.backward_sub(rt1.backward_sub(letter))) # runs the rotors in backwards order
    return letter

ref1 = Rotor(ref1)

rotor1 = Rotor(r1['beta'])
rotor2 = Rotor(r2['beta'])
rotor3 = Rotor(r3['beta'])

print(f"OUTPUT : {encrypt(rotor1, rotor2, rotor3, 'a', ref1)}")

print(rotor3.rotate())
print(rotor3.forward_sub("a"))
print(rotor3.backward_sub('d'))

set = PlugBoard(default_pbset)
set.value_check('a')