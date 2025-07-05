"""
File: hangman.py
Name: Ching Ching
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    TODO:This program simulates a hangman game, where players guess a hidden word character by character within a
    limited number of turns. It displays the progress with dashes, updating them as correct letters are guessed.
    """
    string = ""
    count = N_TURNS
    ans = random_word()
    for i in range(len(ans)):
        string += '-'
    print('The word looks like: ', end='')
    print(string)
    while True:
        print('You have ' + str(count) + ' wrong guesses left.')
        ch = input('Your guess: ')
        ch_upper = ch.upper()
        new_string = ""
        if not ch_upper.isalpha():
            print('Illegal format .')
        elif len(ch) > 1:
            print('Illegal format .')
        elif ch_upper not in ans:
            count = count - 1
            print("There is no " + str(ch_upper) + "'s in the word.")
        else:
            for i in range(len(ans)):
                ch_ans = ans[i]
                if ch_upper != ch_ans:
                    new_string += string[i]
                else:
                    new_string += ch_upper
            print('You are correct! ')
            string = new_string
        if '-' not in string:
            print('You win !!')
            print('The answer is:' + string)
            break
        if count == 0:
            print('You are completely hung :( ')
            print('The answer is:' + ans)
            break
        print('The word looks like: ', end='')
        print(string)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
