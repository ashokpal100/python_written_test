

# while True:
# 	num=int(raw_input("enter any no: "))
# 	for x in range(2,num):
# 		if num%x==0:
# 			print "not"
# 			break

# 	else:
# 		print "prime"


for num in range(2,101):
    for i in range(2,num):
        if (num%i==0):
            break
    else:
        print(num)
	
# Python Program - Check Prime Number or Not
		
while True:
	print("Enter 'x' for exit.")
	num = input("Enter any number: ")
	if num == 'x':
		break
	try:
		number = int(num)
	except ValueError:
		print("Please, enter a number...")
	else:
		for i in range(2, number):
			if number%i == 0:
				print number, "is not a prime"
				break
		else:
			print number, "is a prime number"