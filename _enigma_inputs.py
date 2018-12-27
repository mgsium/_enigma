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

default_pbset = [['a', 'b'], ['a', 'b'], ['a', 'b'], ['a', 'b'], ['a', 'b'], ['a', 'b']]
