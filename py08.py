formatter = "%r%r%r%r"
#print formatter (1,2,3,4)
print 1,2,3,4
#print formatter % ("one","two","three","four")
print "one","two","three","four"

print formatter % (True,False,True,False)
#there must have four characters
#print formatter % (True,False,True)
print formatter % (formatter,formatter,True,False)
print formatter % (
	"I had this thing",
	"That you could type up right",
	"But it didn't sing",
	"So I said goodnight"
)