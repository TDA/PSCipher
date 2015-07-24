__author__ = 'saipc'
# Note to self: I always use snake_casing for Python, and camelCasing for most other languages (no pun intended)
from itertools import chain
class PlayFairCipher:
    """ Playfair Cipher using multi-dimension matrix
    """
    matrix_size = 5
    filler = 'x'
    alphabets = 'abcdefghiklmnopqrstuvwxyz' #no j, all j is considered as i
    def __init__(self, keyword = None, plaintext = None):
        # replace all j by i and store it
        if(keyword != None):
            self.keyword = keyword.replace('j', 'i')
        else:
            self.keyword = keyword
        # default constructor for other
        self.plaintext = plaintext
        self.charset = []
        self.matrix = []

    def generate_matrix(self):
        alpha_set = []
        # create a list of alphabets in the order of (keyword followed by alphabets not in keyword)
        for char in chain(self.keyword, self.alphabets):
            # prevent duplication of alphabets
            if char not in alpha_set:
                alpha_set.append(char)
        # create each row iteratively, equivalent to matrix[i][j] in
        # strongly typed languages like Java
        self.matrix = [alpha_set[i:i+5] for i in xrange(0,25,5)]

    def preformat_plaintext(self, plaintext):
        """
        :param plaintext: The plaintext to be encoded
        :return: a set of digrams that can be used to encode the plaintext
        """
        self.plaintext = plaintext.replace('j', 'i') # replace all j with i
        digram = ''
        charset = []
        i = 0
        # collect all the two letters(digrams) and store them in a list
        while(i < len(plaintext)):
            # but check if they are the same letters
            first_letter = plaintext[i]
            second_letter = plaintext[i+1]

            if(first_letter != second_letter):
                # if they are different, store them and move onto the next two letters
                digram = plaintext[i:i+2]
                i = i + 2
            else:
                # if same letters, use a filler letter and move one letter NOT two
                digram = plaintext[i] + self.filler
                i = i + 1

            # append each digram to the list
            charset.append(digram)
        self.charset = charset

    def print_cipher(self):
        # just print the matrix in a neat way
        # totally cosmetic, no need to implement if not required
        print("The PlayFair Matrix is:")
        for row in self.matrix:
            print(str('|'.join([str(i) for i in row[:]])) +"\n__________")
        print ("The plain text was '" + str(self.plaintext) + "'")
        print ("The preformatted plain text digrams were '" + str(self.charset) + "'")

    def find_indices(self, char):
        # some shenanigans for matrix traversal in python
        # this is the same as using two for loops in Java
        # this is why you should choose the best tool for any program
        # clearly python isnt suited for matrices, unless you use numPy
        # and even with numPy, not for ragged arrays
        """
        :param char: the character to be found
        :return: indices where @char is found
        The same program in Java would be as simple as(hopefully, assuming
        we have used arraylists)
        for (int i = 0; i < 5; i++) {
            int j = self.matrix[i].indexOf(char);
            }
        """
        for i, row in enumerate(self.matrix):
            for j, value in enumerate(row):
                if(char == value):
                    return i,j

    def gene

pfc = PlayFairCipher("monarchy")
pfc.generate_matrix()
pfc.preformat_plaintext("balloon")
pfc.print_cipher()

pfc2 = PlayFairCipher("world")
pfc2.generate_matrix()
#pfc2.print_matrix()