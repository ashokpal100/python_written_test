
number=int(raw_input("enter any no: "))
sum = 0
temp = number
while number > 0:
	rem = number % 10
	sum += rem
	number //= 10
print("Sum of all digits of", temp, "is", sum, "\n")