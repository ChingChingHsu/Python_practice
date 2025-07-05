"""
File: hailstone.py
Name: Ching-Ching
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    TODO: This program will show the process of a math problem, and the result will turn into 1 at the end of the
     Hailstone Sequence.
    """
    print('This program computes Hailstone sequences.')
    n = int(input('Enter a number:'))
    count = 0
    while True:
        if n == 1:
            print('It took '+str(count)+' steps to reach 1.')
            break
        elif n % 2 == 0:
            ans = n//2
            count += 1
            print(str(n) + ' is even, so I take half: ' + str(ans))
            n = ans
        elif n % 2 == 1:
            ans = (n * 3) + 1
            count += 1
            print(str(n) + ' is odd, so I make 3n+1: ' + str(ans))
            n = ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
