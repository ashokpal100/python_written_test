# Python Program - Reverse String
from __future__ import print_function		
while True:
	print("Enter 'x' for exit.")
	string = raw_input("Enter any string: ")
	revStr =string.split(' ');
	#print revStr[::-1]
	re1=""
	for x in revStr[::-1]:
		print (x,end=" ")

	print ("=======================")
	if string == 'x':
		break
	else:
		revstring = string[::-1]
		print("Reverse String =",revstring,"\n")

