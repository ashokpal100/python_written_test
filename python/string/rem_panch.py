# Python Program - Remove Punctuations from String
		
while True:
	print("Enter 'x' for exit.")
	string = input("Enter any string: ")
	if string == 'x':
		break
	else:
		newstr = string
		print("\nRemoving punctuations from the given string...")
		punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
		for x in string.lower():
			if x in punctuations:
				newstr = newstr.replace(x,"")
		print("New string after successfully removing all punctuations!")
		print(newstr,"\n")