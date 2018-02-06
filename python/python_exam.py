print("Python Tutorial at codescracker.com");#simple out put


#str = input("Enter your name please: ")
str = raw_input("Enter your name please: ")
print "Hello,", str, "\nWelcome to Python Tutorial from codescracker.com"

while True:
	print("Enter 'x' for exit.")
	codescracker = raw_input("Enter your name: ")
	Codescracker = raw_input("Enter your friend's name: ")
	if codescracker == 'x':
		break
	else:
		print(Codescracker,"is your friend.\n")




# Python Program - Get Input from User - Complete Version
while True:
	print("Enter '0' for exit.")
	val = int(raw_input("Enter any Number: "))
	flt = float(raw_input("Enter any Floating-point Number: "))
	strg = raw_input("Enter any String: ")
	print type(val)
	print type(flt)
	print type(strg)
	if val == 0:
		break
	else:
		print val
		print flt
		print strg
	print()

