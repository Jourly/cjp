def cheese_and_crackers(cheese_count,boxes_of_crackers):
	print "You have %d cheeses!"%cheese_count
	print "You have %d boxes of crackers!"%boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
print "We can just give the function numbers directly"
cheese_count=20
cracker_count=30
cheese_and_crackers(cheese_count,cracker_count)

print "We can also do math inside too:"
cheese_and_crackers(1+2,3+4)
cheese_and_crackers(cheese_count+2,cracker_count+3)
