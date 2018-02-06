# for i in 3: error
#     print i

for i in "hello":
    print i


#So there are many types of objects which can be used with a for loop. These are called iterable objects.
my_list = [1,2,3]
for i in my_list:
    print i

for line in open("a.txt"):
	print line,

print("\n")
#There are many functions which consume these iterables.
print ",".join(["a", "b", "c"])

print

print ",".join({"x": 1, "y": 2})

print

print list("python")

print

print list({"x": 1, "y": 2})

#The Iteration Protocol
#The built-in function iter takes an iterable object and returns an iterator.

x = iter([1, 2, 3])
print x
print x.next()
it = reversed([1, 2, 3, 4])
print it.next()

y = iter((1, 2, 3))
z = iter({"a":1, "b":2, "c":3})

print x.next()
print y
print z


#The return value of __iter__ is an iterator. It should have a next method and raise StopIteration when there are no more elements.


#Generators
def yrange(n):
    i = 0
    while i < n:
        yield i  #Each time the yield statement is executed the function generates a new value.
        i += 1
y = yrange(3)
print y
print y.next()

#So a generator is also an iterator
#Generator Expressions
print "sum"
print sum((x*x for x in range(10)))
sum((x*x for x in range(10)))
print sum
#print sum(x)




#yield
print "yield"

def f123():
    yield 1
    yield 2
    yield 3

for item in f123():
    print item