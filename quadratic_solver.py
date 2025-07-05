"""
File: quadratic_solver.py
Name: Ching-Ching
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	TODO: User can use the program to know the answer of the equation and how many roots does the equation have.
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	x = (b * b) - (4 * a * c)
	if x < 0:
		print('No real roots')
	elif x == 0:
		ans = (-1 * b) / (2 * a)
		print('One root:  ' + str(ans))
	elif x > 0:
		y = math.sqrt(x)
		ans_1 = (-1 * b + y) / (2 * a)
		ans_2 = (-1 * b - y) / (2 * a)
		print('Two roots: ' + str(ans_1) + ',' + str(ans_2))
# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == "__main__":
	main()
