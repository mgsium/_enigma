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
print(f'{alpha}\n{r1}\n{r2}\n{r3}')


#reflector
ref1 = list(map(str, 'aeltphqxrubknwcmoydfgivjzs'))

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
