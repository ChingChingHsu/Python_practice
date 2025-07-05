"""
File: similarity.py (extension)
Name:
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    TODO:
    """
    sequence1 = input('Please give me a DNA sequence to search: ').upper()
    sequence2 = input('What DNA sequence would you like to match? ').upper()
    maximum = 0
    l1 = len(sequence1)
    l2 = len(sequence2)
    best_match = 0
    for i in range(l1-(l2-1)):
        count = 0
        for j in range(l2):
            if sequence1[i+j] == sequence2[j]:
                count += 1
        if count > maximum:
            maximum = count
            best_match = i
    print('The best match is ' + sequence1[best_match:best_match+l2])
















# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
