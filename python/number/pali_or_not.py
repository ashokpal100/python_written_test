num=int(raw_input("enter any no: "))

number = int(num)
orig = number
rev = 0

while number > 0:
	rm=number%10
	rev=(rev*10)+rm
	number=number/10
	print rev

if orig==rev:
	print "pli",rev
else:
	print "not",rev


# Python Program - Check Palindrome Number or Not
		
# while True:
# 	print("Enter 'x' for exit.")
# 	num = input("Enter any number: ")
# 	if num == 'x':
# 		break
# 	else:
# 		number = int(num)
# 		orig = number
# 		rev = 0
# 		while number > 0:
# 			rev = (rev*10) + number%10
# 			number = number/10
# 		if orig == rev:
# 			print(orig, "is a Palindrome Number.\n")
# 		else:
# 			print(orig, "is not a Palindrome Number.\n")

	