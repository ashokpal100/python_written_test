# Python Program - Generate Random Numbers
		
from random import randint
while True:
	print("Enter 'x' for exit.")
	val1 = input("Enter lower limit: ")
	val2 = input("Enter upper limit: ")
	val3 = input("How many random numbers to print ? ")
	if val1 == 'x':
		break
	else:
		lower = int(val1)
		upper = int(val2)
		amount = int(val3)
		for i in range(0, amount):
			print(randint(lower, upper),end=" ")
		print("\n")