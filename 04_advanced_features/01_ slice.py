#coding=utf-8

# 切片

# 对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。

# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# print L[0:3]

# print L[1:3]

# print L[-2:]

# print L[-2:-1]

L = range(100)

print L[:10:2]

print L[10:50:5]

print "abcdefghijklmno"[0:1]

