"""
File: weather_master.py
Name: Ching-Ching
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100


def main():
	"""
	TODO: This program can find the maximum temperature, minimum temperature, average temperature,and the amount of day
	that lower than 16 degrees.
	"""
	print('1. This program finds the max. ')
	data = int(input('Next Temperature: (or -100 to quit ) ? '))
	if data == EXIT:
		print('No data.')
	else:
		maximum = data
		minimum = data
		counter = 1
		total = data
		if data > 16:
			cold = 0
		else:
			cold = 1

		while True:
			data = int(input('Next Temperature: (or -100 to quit ) ? '))
			if data == EXIT:
				break
			if data > maximum:
				maximum = data
			if data < minimum:
				minimum = data
			counter += 1
			total = total + data
			average = total/counter
			if data < 16:
				cold += 1
		print('Max:' + str(maximum))
		print('Min:' + str(minimum))
		print('Average:'+str(average))
		print('Cold weather:' + str(cold))


		data = float(line)
		maximum = data
		minimum = data
		counter = 0
		total = data


		while data.isdigit():
			if data > maximum:
				maximum = data
			if data < minimum:
				minimum = data
			counter += 1
			total = total + data
			average = total/counter
		if counter == 0:
			print('No data in this file')
		else:
			print('Max:' + str(maximum))
			print('Min:' + str(minimum))
			print('Avg:'+str(average))





# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
