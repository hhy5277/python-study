#coding=utf-8

# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>

age = 3

if age == 0:
    print 'your age is', age
elif age == 1:
    print 'your age is', age
else:
    print 'your age is', age

# Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来，看例子：

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name


# 如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，比如range(101)生成的序列是从0开始小于100的整数：



sum = 0
for x in range(101):
    sum = sum + x
print sum


# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现：


sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
else:
    print sum
print sum