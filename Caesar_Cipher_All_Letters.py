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
        if(97 <= plaintext_ascii_no <= 122 or 65 <= plaintext_ascii_no <= 90):
            cipher_ascii_no = plaintext_ascii_no + key
            if (97 <= plaintext_ascii_no <= 122 and cipher_ascii_no > 122)\
                    or (65 <= plaintext_ascii_no <= 90 and cipher_ascii_no > 90):
                # if the numbers ran out, wrap them
                cipher_ascii_no = cipher_ascii_no + shift
            # otherwise they can be just written back
            char = chr(cipher_ascii_no)
            new_string += char
        else:
            new_string += char
    return new_string

if __name__ == "__main__":
    no = int(raw_input())
    string = raw_input()
    key = int(raw_input())
    print Caesar_Cipher(string, key, "enc")

