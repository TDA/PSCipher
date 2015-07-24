__author__ = "saipc"
# Note to self: I always use snake_casing for Python, and camelCasing for most other languages (no pun intended)
from itertools import chain
import re
class PlayFairCipher:
    """ Playfair Cipher using multi-dimension matrix
    """
    matrix_size = 5
    filler = "x"
    alphabets = "abcdefghiklmnopqrstuvwxyz" #no j, all j is considered as i
    def __init__(self, keyword = None, plaintext = None):
        # replace all j by i and store it
        if(keyword != None):
            self.keyword = keyword.replace("j", "i")
        else:
            # set a default keyword
            self.keyword = "keyword"
        # default constructor for other
        self.plaintext = plaintext
        self.charset = []
        self.matrix = []
        self.cipher_charset = []
        self.ciphertext = ""


    def generate_matrix(self):
        alpha_set = []
        # create a list of alphabets in the order of (keyword followed by alphabets not in keyword)
        for char in chain(self.keyword, self.alphabets):
            # prevent duplication of alphabets in (keyword + alphabets)
            if char not in alpha_set:
                alpha_set.append(char)
        # create each row iteratively, equivalent to matrix[i][j] in
        # strongly typed languages like Java
        self.matrix = [alpha_set[i:i+5] for i in xrange(0,25,5)]

    def preformat_plaintext(self, plaintext):
        """
        :param plaintext: The plaintext to be encoded, no special characters or spaces
        :return: a set of digrams that can be used to encode the plaintext
        """
        self.plaintext = plaintext.replace("j", "i") # replace all j with i
        # remove/strip all special characters and spaces
        self.plaintext = re.sub(r"[-_)(*&^\\/%$#@!\"\' ]", "", self.plaintext)
        charset = []
        i = 0
        # collect all the two letters(digrams) and store them in a list
        while(i < len(self.plaintext)):
            digram = ""
            # but check if they are the same letters
            first_letter = self.plaintext[i]
            # maintain spaces

            if ((i + 1) >= len(self.plaintext)):
                second_letter = "x"
            else:
                second_letter = self.plaintext[i+1]

            if(first_letter != second_letter):
                # if they are different, store them and move onto the next two letters
                digram = first_letter + second_letter
                i = i + 2
            else:
                # if same letters, use a filler letter and move one letter NOT two
                digram = first_letter + self.filler
                i = i + 1

            # append each digram to the list
            charset.append(digram)
        self.charset = charset

    def print_cipher(self):
        # just print the matrix in a neat way
        # totally cosmetic, no need to implement if not required
        print("The PlayFair Matrix is:")
        for row in self.matrix:
            print(str("|".join([str(i) for i in row[:]])) +"\n__________")
        print ("The plain text was '" + str(self.plaintext) + "'")
        print ("The preformatted plain text digrams were '" + str(self.charset) + "'")
        # print("k was found at " + str(self.find_indices('k')))
        print("The generated cipher digrams were " + str(self.cipher_charset))
        print("The generated cipher text is " + str(self.ciphertext))

    def find_indices(self, char):
        # some shenanigans for matrix traversal in python
        # this is the same as using two for loops in Java
        # this is why you should choose the best tool for any program
        # clearly python isnt suited for matrices, unless you use numPy
        # and even with numPy, not for ragged arrays
        # EDIT: you can still use two for loops, just not suited for
        # initializing matrices
        """
        :param char: the character to be found
        :return: indices where @char is found
        """
        for i in xrange(0, len(self.matrix)):
            for j in xrange(0, len(self.matrix[i])):
                if(char == self.matrix[i][j]):
                    return i,j
        # original looping I used, the one above is easier to read, so changed it.
        # for i, row in enumerate(self.matrix):
        #    for j, value in enumerate(row):
        #        if(char == value):
        #            return i,j


    def generate_cipher_text(self):
        for digram in self.charset:
            first_letter = digram[0]
            second_letter = digram[1]
            i, j = self.find_indices(first_letter)
            k, l = self.find_indices(second_letter)
            # now check for the 3 conditions, and set
            # the cipher for each letter accordingly

            if (i == k):
                # same row, so next letter to the right,
                # wrap around if it overflows
                cipher_first_letter = self.matrix[i][(j + 1) % self.matrix_size]
                cipher_second_letter = self.matrix[i][(l + 1) % self.matrix_size]
            elif (j == l):
                # same column, so next letter to the bottom,
                # wrap around if it overflows
                cipher_first_letter = self.matrix[(i + 1) % self.matrix_size][j]
                cipher_second_letter = self.matrix[(k + 1) % self.matrix_size][j]
            else:
                # they are in different columns and rows, so get
                # their diagonal elements
                cipher_first_letter = self.matrix[i][l]
                cipher_second_letter = self.matrix[k][j]
            cipher_digram = cipher_first_letter + cipher_second_letter
            self.cipher_charset.append(cipher_digram)
        self.ciphertext = "".join(self.cipher_charset)

pfc = PlayFairCipher("monarchy")
pfc.generate_matrix()
pfc.preformat_plaintext("hseaaroonmu was an idiot")
pfc.generate_cipher_text()
pfc.print_cipher()

pfc2 = PlayFairCipher("keyword")
pfc2.generate_matrix()
pfc2.preformat_plaintext("whydontyou")
pfc2.generate_cipher_text()
pfc2.print_cipher()

pfc3 = PlayFairCipher("keyword")
pfc3.generate_matrix()
pfc3.preformat_plaintext("yieaesvkez")
pfc3.generate_cipher_text()
pfc3.print_cipher()

