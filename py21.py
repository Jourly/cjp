def add(a,b):
	print "Adding %d + %d"%(a,b)
	return a+b
	
def substract(a,b):
	print "Substracting %d - %d:"%(a,b)
	return a-b
	
def multiply(a,b):
	print "Multiplying %d * %d:"%(a,b)
	return a*b
	
def divide(a,b):
	print "Dividing %d / %d:"%(a,b)
	return a/b
	
print "Let's do some math with just functions!"

age = add (20,5)
print age
height = substract(160,5)
print height
weight = multiply(10,2)
print weight
iq = divide (100,2)
print iq

print "Here are :age:%d,height:%d,weight:%d,iq:%d"%(age,height,weight,iq)

what =add(age,substract(height,multiply(weight,divide(iq,2))))

print what