__author__ = 'saipc'
from itertools import chain
class PlayFairCipher:
    """ Playfair Cipher using multi-dimension matrix
    """
    matrix_size = 5
    alphabets = 'abcdefghiklmnopqrstuvwxyz' #no j, all j is i
    def __init__(self, keyword):
        self.keyword = keyword.replace('j', 'i')
        # mutable list as matrix, so each object gets its own
        # if declared as a class variable will lead to shared matrix

    def generate_matrix(self):
        alpha_set = []
        for char in chain(self.keyword, self.alphabets):
            if char not in alpha_set:
                alpha_set.append(char)
        self.matrix = [alpha_set[i:i+5] for i in xrange(0,25,5)]

    def print_matrix(self):
        for row in self.matrix:
            print(str('|'.join([str(i) for i in row[:]])) +"\n__________")





pfc = PlayFairCipher("monarchy")
pfc.generate_matrix()
pfc.print_matrix()

pfc2 = PlayFairCipher("world")
pfc2.generate_matrix()
#pfc2.print_matrix()