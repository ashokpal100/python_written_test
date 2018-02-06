# Python Program - Swap Two Strings
		
while True:
	print("Enter 'x' for exit.")
	string1 = raw_input("Enter First String: ")
	string2 = raw_input("Enter Second String: ")
	if string1 == 'x':
		break
	else:
		temp = string1
		string1 = string2
		string2 = temp
		print("\nString after swapping:")
		print("First String:", string1)
		print("Second String:", string2,"\n")