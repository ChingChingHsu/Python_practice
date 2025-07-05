"""
File: complement.py
Name: Ching Ching
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    TODO: This program will build complement of a strand of a DNA sequence.
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    ans = ""
    if dna == '':
        return 'DNA strand is missing.'
    for i in range(len(dna)):
        ch = dna[i]
        if ch == 'A':
            ans += 'T'
        elif ch == 'T':
            ans += 'A'
        elif ch == 'C':
            ans += 'G'
        elif ch == 'G':
            ans += 'C'
    return ans





# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
