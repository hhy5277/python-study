#coding=utf-8

# 函数的调用

print help(abs)  # help(abs)查看abs函数的帮助信息。

print abs(-2) # abs(-2) -2的绝对值

# 比较函数cmp(x, y)就需要两个参数，如果x<y，返回-1，如果x==y，返回0，如果x>y，返回1：

print cmp(1,0)

# 数据类型转换

print int('123') # 转换为int类型

print int(12.34)  # 转换为int类型,结果为12

print float("12.34")

print str(123)

print unicode(100)

print bool(1)

print bool(0)

print bool('')

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：

a = abs


print a(-1)