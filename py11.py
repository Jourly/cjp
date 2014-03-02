#-*-coding:UTF-8-*-
print "How old are you?",
#age = int(raw_input("Please enter your name"))
age = Boolean(raw_input("Please enter your name"))
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()
print "So,you're %d old,%s tall and %s heavy."%(age,height,weight)

#知识点总结
#1.print 后面有，则，后面的东西也会被输出来，即便写在两行里
#2.raw_input(),接收用户的一个输入，并将结果返回，返回值可以用一个变量进行接收
#3.raw_input("提示信息")，可以在括号里写上提示信息
#4.可以在前面加上int
#5.这样接收的都是字符串