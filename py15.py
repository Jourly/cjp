#-*-coding:UTF-8-*-
from sys import argv
script,filename = argv
txt = open(filename)
print "Here's your file %r"%filename
print txt.read()
txt.close()

print "Type the file name again '>'"
file2 = raw_input()
txt2 = open(file2)
print txt2.readline()
print txt2.readline()
txt2.close()

#文件路径，如果和脚本在一个目录下，则可以只写文件名
#如果指定文件路径，则可以直接拷贝文件路径，一个右斜杠即可
#open（String name）方法，打开一个文件
#readline(),读取文件内的一行