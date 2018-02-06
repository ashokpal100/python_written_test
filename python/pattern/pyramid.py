from __future__ import print_function

print ("sfsf")
print ("df\n")
print ("ki\r")
print ("dfsdf")

print ("Python Program - Pattern Program 1")
for i in range(0,5):
	#str1=""
	for j in range(0,i):
		#str1=str1+"*"
		print ("* " , end="")
	print ("\n")

#out put
#*

#* *

#* * *

#* * * *
print ("Python Program - Pattern Program 2")
for i in range(0,5):
    for j in range(0,i):
        print(i, end="")
    print("\n")

print ("Python Program - Pattern Program 3")
for i in range(0,5):
    for j in range(0,i):
        print(j, end="")
    print("\n")

print ("Python Program - Pattern Program 4")
k=1
for i in range(0,5):
    for j in range(0,i):
        print(k, end="")
        k=k+1
    print("\n")

print ("Python Program - Pattern Program 5")
k=1
for i in range(0,5):
    for j in range(0,k):
        print("* ", end="")
    k=k+2
    print("\n")

print ("Python Program - Pattern Program 6")
num = 1
for i in range(0, 5):
	num = 1
	for j in range(0, i+1):
		print(num, end="")
		num = num + 1
	print()

print ("Python Program - Pattern Program 7")
val = 65
for i in range(0, 5):
	for j in range(0, i+1):
		ch = chr(val)
		print(ch, end="")
		val = val + 1
	print()

print ("Python Program - Pattern Program 8")
val = 65
for i in range(0, 5):
	for j in range(0, i+1):
		ch = chr(val)
		print(ch, end="")
	val = val + 1
	print()
print ("Python Program - Pattern Program 9 triangle")
# Function to demonstrate printing pattern triangle

def triangle(n):
     
    p=1
    k = 2*n - 2
    for i in range(0, n):
     
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end="  ")
     
        # decrementing k after each loop
        k = k - 1
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, p):
         
            # printing stars
            print("* ", end="")
        p=p+2
        # ending line after each row
        print()
 
# Driver Code
n = 5
triangle(n)

print ("Python Program - Pattern Program 10 triangle")
def triangle1(n):
     
    k = 2*n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i):
            print("* ", end="")
        print()
n = 5
triangle1(n)