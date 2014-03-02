#-*-coding:UTF-8-*-
from sys import argv
script , filename = argv
print "we're going to erase %r."%filename
print "If you don't want that ,hit CTRL-C(^C)."
print "If you want to do that ,hit RETURN."
raw_input("?")
print "Opening the file..."
target = open(filename,'w+')
print target.read()
print "Truncating the file.Goodbye!"
target.truncate()
print "Now I'm going to ask you for three lines."
line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")
print "Now I'm going to write these to the file."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\t")
target.write(line3)

print "And finally ,we close it."
target.close()
target = open(filename)
print target.read()

#ctrl+c 将退出程序的执行。Enter继续执行
#写入时，写"\n"写入一个换行符
#truncate（），清空函数
#open（）方法，默认以只读方式打开
#w+，r+，a+方式，以读写方式打开