from __future__ import print_function
num1=int(raw_input("enter any no1: "))

a=0
b=1
print (a, b,end=" ")

while num1>0:
	c=a+b
	a=b
	b=c
	print (c,end=" ")
	num1-=1