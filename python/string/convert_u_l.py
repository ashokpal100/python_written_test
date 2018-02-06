# Python Program - Convert Uppercase to Lowercase
		
while True:
	print("Enter 'x' for exit.")
	string = raw_input("Enter any string: ")
	if string == 'x':
		break
	else:
		string_in_lowercase = string.lower()
		print("String in Lowercase =",string_in_lowercase,"\n")