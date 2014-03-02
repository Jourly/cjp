#coding=utf-8
from sys import argv
from os.path import exists
script,from_file,to_file = argv
print "Copying from %s to %s"%(from_file,to_file)
in_file = open(from_file)
in_data = in_file.read()
print "the input file is %d bytes long"%len(in_data)
print "does the output file exist?%r"%exists(to_file)
print "Ready,hit RETURN to continue,CTRL-C to abort."
raw_input()
to_file = open(to_file,"w")
to_file.write(in_data)
print "All right,all done."
in_file.close()
to_file.close()
#len(Str)字符串长度
#exists（file）判断文件是否存在


print u"你好"
print "你好吗？".decode("utf-8").encode('gb2312')
#import sys
#print sys.getdefaultencoding()
#u方法：pythonn内部编码为unicode，写成u’Str‘，中文可以正常打印
#转码方法：或者将utf-8的中文decode成unicode，在用encode方法将unicode变成gb2312