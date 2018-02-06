# Python Program - One Dimensional Array
from __future__ import print_function	
while True:
	print("Enter 'x' for exit.")
	nval = input("How many element you want to store in the array ? ")
	if nval == 'x':
		break
	else:
		n = int(nval)
		arr = []
		for i in range(1, n+1):
			arr.append(i)
		print("\nElements in Array are:")
		for i in range(0, n):
			print(arr[i], end=" ")
		print("\n")