
while True:
	ch=raw_input("enter any char: ")
	print ch
	if((ch>="a" and ch<="z") or (ch>="A" and ch<="Z")):
		print ch, "is an alphabet"
	else:
		print ch, "is not an alphabet."

	