from _enigma_inputs import *
import string

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



