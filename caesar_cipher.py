__author__ = 'saipc'

def Caesar_Cipher(string, key, enctype):
    # @string: the string to be converted
    # @key: the value of shifting, an integer (0-25, wraps around 26)
    # @enctype: 'enc' for testing, 'dec' for decrypting
    new_string = ''
    shift = 0
    # check if test or decrypt and set the key and shift(wrap around)
    if enctype == 'dec':
        key = - (key % 26)
        shift = 26
    elif enctype == 'enc':
        key = key % 26
        shift = -26

    # iterate through the string and set letters accordingly
    for char in string:
        plaintext_ascii_no = ord(char)
        if(plaintext_ascii_no == 32 or plaintext_ascii_no == 39):
            # do not encode/decode spaces or single quotes
            new_string += char
            continue
        cipher_ascii_no = plaintext_ascii_no + key
        if (97 <= plaintext_ascii_no <= 122 and (cipher_ascii_no > 122 or cipher_ascii_no < 97))\
                    or (65 <= plaintext_ascii_no <= 90 and (cipher_ascii_no > 90 or cipher_ascii_no < 65)):
                # if the numbers ran out, wrap them
                cipher_ascii_no = cipher_ascii_no + shift
        # otherwise they can be just written back
        char = chr(cipher_ascii_no)
        new_string += char
    return new_string


def test(string, enctype):
    words = string.split(' ')

    print("\nA Simple Caesar Cipher")
    for i in xrange(1,27):
        cc = Caesar_Cipher(string, i, enctype)
        print(string)
        print(" is ")
        print(cc)
        print "\n"

#test("Hey love, what's up?", "enc")
#test("meet me after the toga party", "enc")
test("oggv og chvgt vjg vqic rctva", "dec")
#test("i love you", "enc")
print Caesar_Cipher("middle-Outz", 2, "enc")

#test("EOY XF, AY VMU M UKFNY TOY YF UFWHYKAXZ EAZZHN. UFWHYKAXZ ZNMXPHN. UFWHYKAXZ EHMOYACOI. VH'JH EHHX CFTOUHP FX VKMY'U AX CNFXY FC OU. EOY VH KMJHX'Y EHHX IFFQAXZ MY VKMY'U MEFJH OU.",'dec')

