# Python Program - Concatenate String
		
while True:
	print("Enter 'x' for exit.")
	string1 = raw_input("Enter first string: ")
	string2 = raw_input("Enter second string: ")
	if string1 == 'x':
		break
	else:
		string3 = string1 + string2
		print("String after concatenation =",string3,"\n")