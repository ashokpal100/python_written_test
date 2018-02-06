# Python Program - Convert Decimal to Binary
		
def trans(x):
    if x == 0:
    	return [0]
    bit = []
    while x:
        bit.append(x % 2)
        x=x/2
    return bit[::-1]

print trans(12)

while True:
	print("Enter 'x' for exit.")
	dec = input("Enter number in Decimal Format: ")
	if dec == 'x':
		break
	else:
		decimal = int(dec)
		print(decimal,"in Binary =",bin(decimal),"\n")