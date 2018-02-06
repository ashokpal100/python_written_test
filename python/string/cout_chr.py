# Python Program - Count Character in String
		
while True:
	print("Enter 'x' for exit.")
	string = raw_input("Enter any string: ")
	if string == 'x':
		break
	else:
		char = raw_input("Enter a character to count: ")
		val = string.count(char)
		print(val,"\n")