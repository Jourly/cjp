#-*-coding:utf-8-*-
x = "There are %d types of people"%10
binary = "binary"
do_not = "don't"
y = "Those who know %s and who %s"%(binary,do_not)
print x
print y
print "I said :%s."%x
#%r会把原来的格式也带进来
print "I also said:%r."%y
hilarious = False
joke_evaluation = "Isn't that joke so funny? %r"
print joke_evaluation % hilarious
w = "This is the left side of..."
e = "a string with a right side."
#+号表示把两个字符串连接起来显示
print w+e



'''    
三个单引号里面是多行注释
三个单引号里面是多行注释
三个单引号里面是多行注释
'''

