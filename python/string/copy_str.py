# Python Program - Copy String
		
while True:
	print("Enter 'x' for exit.")
	string = raw_input("Enter any string: ")
	if string == 'x':
		break
	else:
		print("Copying string1 into string2...")
		cstring = string
		print("String 2 after successfully copied..!!")
		print(cstring,"\n")