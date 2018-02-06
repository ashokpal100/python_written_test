# Python Program - Remove Word from Sentence
		
while True:
	print("Enter 'x' for exit.")
	string = raw_input("Enter any string: ")
	if string == 'x':
		break
	else:
		word = raw_input("Enter word to be delete: ")
		print("\nDeleting given word from the given string...")
		print("New String after successfully deleted the given word:")
		word_list = string.split()
		print ' '.join([i for i in word_list if i not in word])
		print 
		print("\n")