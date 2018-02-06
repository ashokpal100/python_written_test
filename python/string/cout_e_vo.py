# Python Program - Count Number of Each Vowels
		
while True:
	print("Enter 'x' for exit.")
	string = raw_input("Enter any string: ")
	if string == 'x':
		break
	else:
		vowels = 'aeiou'
		string = string.casefold()
		count = {}.fromkeys(vowels,0)
		for char in string:
			if char in count:
				count[char] += 1
		print(count,"\n")