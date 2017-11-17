#coding=utf-8

from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}

for key in d :
    print key

# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.itervalues()，如果要同时迭代key和value，可以用for k, v in d.iteritems()。


for value in d.itervalues():
    print value

for key ,value in d.iteritems():
    print key,value


# 字符串也是可以迭代的

for ch in 'ABC':
    print ch



# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：

print  isinstance('abc',Iterable)

print isinstance(123,Iterable)

# 如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：


for index,value in enumerate([1,2,3,4]):
    print index,value


