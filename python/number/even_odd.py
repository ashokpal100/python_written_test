num=int(raw_input("enter any no: "))

if(num%2==0):
	print"even"
else:
	print"odd"


# Python Program - Check Even or Odd
		
while True:
	print("Enter 'x' for exit.")
	num = input("Enter any number: ")
	if num == 'x':
		break
	try:
		number = float(num)
	except ValueError:
		print("Please, enter a number...")
	else:
		check = number%2
		if check == 0:
			print(int(number), "is even number.\n")
		elif check == 1:
			print(int(number), "is odd number.\n")
		else:
			print(number, "is strange.\n")