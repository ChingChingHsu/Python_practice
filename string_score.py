"""
File: string_score.py
Name: Ching Ching
------------------------------
This program calculates a score for a given string based on 
the types of characters it contains. It assigns points as follows: 
digits are worth 1 point, uppercase letters are worth 2 points, 
and lowercase letters are worth 3 points. The score() function 
goes through each character in the string, adds up the points 
according to its type, and then prints out the total score.
"""


def main():
    """
    TODO: This program scores a string by assigning points to its characters: digits (1), uppercase (2), and lowercase
    (3).It calculates the points, and outputs the total score.
    """
    score('1aB4rC')  # digit->1 ; upper->2; lower->3
    # 12
    score('aaaaA3')
    # 15


def score(string):
    ans = 0
    for i in range(len(string)):
        ch = string[i]
        if ch.isdigit():
            ans += 1
        elif ch.isupper():
            ans += 2
        elif ch.islower():
            ans += 3
    print(ans)


if __name__ == '__main__':
    main()