# Python Program - Display Calendar
		
import calendar
while True:
	print("Enter 'x' for exit.")
	y = input("Enter Year: ")
	m = input("Enter month: ")
	if y == 'x':
		break
	else:
		yy = int(y)
		mm = int(m)
		print("\n",calendar.month(yy,mm))