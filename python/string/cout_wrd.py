# Python Program - Count Word in Sentence
		
while True:
	print("Enter 'x' for exit.")
	string = raw_input("Enter any string: ")
	if string == 'x':
		break
	else:
		word_length = len(string.split())
		print("Number of words =",word_length,"\n")