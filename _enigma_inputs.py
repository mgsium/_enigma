import string

# creates a list of regular alphabet characters
alpha = list(map(str, string.ascii_lowercase))

r1 = {
    'beta': list(map(str, 'ekmflgdqvzntowyhxuspaibrcj')),
}
r2 = {
    'beta': list(map(str, 'ajdksiruxblhwtmcqgznpyfvoe'))
}
r3 = {
    'beta': list(map(str, 'bdfhjlcprtxvznyeiwgakmusqo'))
}
r4 = {
    'beta': list(map(str, 'esovpzjayquirhxlnftgkdcmwb'))
}
r5 = {
    'beta': list(map(str, 'vzbrgityupsdnhlxawmjqofeck'))
}

print(f'{alpha}\n{r1}\n{r2}\n{r3}')


#reflectors
A = list(map(str, 'aeltphqxrubknwcmoydfgivjzs'))
B = list(map(str, 'aeltphqxrubknwcmoydfgivjzs'))
C = list(map(str, 'aeltphqxrubknwcmoydfgivjzs'))

#plugboard settings
default_pbset = [
    ['a', 'b'],
    ['c', 'd'],
    ['e', 'f'],
    ['g', 'h'],
    ['i', 'j'],
    ['k', 'l'],
    ['m', 'n'],
    ['o', 'p'],
    ['q', 'r'],
    ['s', 't']]

#rotor positions
rotor_pos = 'd'
