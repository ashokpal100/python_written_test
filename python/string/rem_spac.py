# Python Program - Remove Spaces from String
		
while True:
	print("Enter 'x' for exit.")
	string = input("Enter any string: ")
	if string == 'x':
		break
	else:
		new_string = string.replace(" ","")
		print("\nNew string after removing all spaces:")
		print(new_string,"\n")