num=int(raw_input("enter any no: "))

number = int(num)
orig = number
rev = 0

while number > 0:
	rm=number%10
	rev=rev+(rm*rm*rm)
	number=number/10
	print rev

if orig==rev:
	print "arm",rev
else:
	print "not",rev
