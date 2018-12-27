from _enigma_inputs import *

class PlugBoard:
    def __init__(self, settings):
        self.settings = settings

    def value_check(self, letter):
        for pair in self.settings:
            if letter in pair:
                del pair[pair.index(letter)]
                print(f"MATCHING LETTER: {''.join(pair)}")
                break

class Rotor:
    def __init__(self, beta):
        self.beta = beta

    # rotate the rotor
    def rotate(self):
        new_beta = [0 for i in range(26)]
        for letter in self.beta:
            if self.beta.index(letter) == 0:
                new_beta[25] = letter
            else:
                new_beta[self.beta.index(letter)-1] = letter
        self.beta = new_beta
        return new_beta

    # before reflection
    def forward_sub(self, letter):
        return self.beta[alpha.index(letter)]

    # after reflection; don't call for reflectors
    def backward_sub(self, letter):
      return alpha[self.beta.index(letter)]



