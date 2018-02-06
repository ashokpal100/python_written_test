for i in range(0, 20):
	print "range="+str(i)
for i in xrange(0, 20):
	print "xrange="+str(i)


#Range returns a list while xrange returns an xrange object 
#which takes the same memory irrespective of the range size,as in this case,
#only one element is generated and available per iteration whereas in case of using range, 
#all the elements are generated at once and are available in the memory.