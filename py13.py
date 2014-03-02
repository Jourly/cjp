#-*-coding:UTF-8-*-
from sys import argv

script1 ,first,second, third = argv

print "The script  is called:",script1
print "Your first variable is:",first
print "Your second variable is:",second
print "Your third variable is:",third


#import 导入一个功能
#argv 必须是这个,或者argvs，不能换成别的
# argv 解包，将所有变量解压出来
#运行程序时必须有对应的这几个参数
#python py13.py one two three ,中间用空格隔开