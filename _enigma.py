from _enigma_classes import *
from _enigma_inputs import *
from _enigma_gui import *

#print(f"OUTPUT : {encrypt(rotor1, rotor2, rotor3, 'z', ref1)}")

#print(f"INPUT : {decrypt(rotor1, rotor2, rotor3, 'd', ref1)}")

'''
print(rotor3.rotate())
print(rotor3.forward_sub("a"))
print(rotor3.backward_sub('d'))

set = PlugBoard(default_pbset)
set.value_check('a')
'''

# runs the gui mainloop

root.mainloop()
