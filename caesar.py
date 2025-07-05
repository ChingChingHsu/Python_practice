"""
File: caesar.py
Name: Ching Ching
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    TODO:This program illustrates the Caesar cipher by shifting the alphabet based on user input, and then changing
    text using that shifted alphabet.
    """
    x = int(input('Secret number: '))
    string = str(input("What's the ciphered string? "))
    new_alphabet = replace_alphabet(x)
    new_string = re_string(new_alphabet, string)
    print('The deciphered string is:'+str(new_string))


def replace_alphabet(x):
    new_alphabet = ""
    for i in range(-x, 26-x, 1):
        ch = ALPHABET[i]
        new_alphabet += ch
    return new_alphabet


def re_string(new_alphabet, string):
    new_string = ""
    for i in range(len(string)):
        ch_old = string[i]
        ch_old = ch_old.upper()
        if ch_old in ALPHABET:
            x = new_alphabet.find(ch_old)
            ch_new = ALPHABET[x]
            new_string += ch_new
        else:
            new_string += ch_old
    return new_string



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
