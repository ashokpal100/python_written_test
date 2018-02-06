# Python Program - Sort String in Alphabetical Order
		
while True:
	print("Enter 'x' for exit.")
	string = raw_input("Enter any string: ")
	if string == 'x':
		break
	else:
		print ''.join(sorted(string))
		print()