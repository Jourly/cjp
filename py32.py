the_count = [1,2,3,4,5]
fruits = ['apples','orange','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
	print "this is count:%d"%number
	
for fruit in fruits:
	print "a fruit of type:%s"%fruit
	
for i in change:
	print "I got %r"%i
	
elements = []

for i in range(0,6,3):
	print "Adding %d to the list:"%i
	elements.append(i)
	
for i in elements:
	print "element is %d"%i
	
	
