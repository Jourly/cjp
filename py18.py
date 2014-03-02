#coding=utf-8
def print_two(*args):
	arg1,arg2 = args
	print "arg1:%s,arg2:%s"%(arg1,arg2)
	print "this is the first def"

def print_two_again(arg1,arg2):
	print "arg1:%s,arg2:%s"%(arg1,arg2)
	
def print_one (arg1):
	print "arg1:%r"%arg1
	
def print_one_again(arg2):
	print "arg2:%r"%arg2
	
print_two("aaa","bbb")
print_two_again("ni","hao")
print_one("this is the one def")
print_one_again("this is the second def")
	

