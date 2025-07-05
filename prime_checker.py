"""
File: prime_checker.py
Name: Ching-Ching
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
	"""
	TODO: This program can check the number is prime number or not.
	"""
	print('Welcome to the prime checker!')
	while True:
		n = int(input('n: '))
		if n == EXIT:
			print('Have a good one!')
			break
		if n == 2:
			print(str(n) + ' is a prime number.')
		else:
			for i in range(2, n):
				if n % i == 0:
					print(str(n) + ' is not a prime number.')
					break
			if n % i != 0:
				print(str(n) + ' is a prime number.')


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == "__main__":
	main()
