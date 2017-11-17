#coding=utf-8


def f(x):
    return x * x


# “把f(x)作用在list的每一个元素并把结果生成一个新的list”

print map(f, range(10))

print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])

# reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# 序列求和


def add(x, y):
    return x + y


print reduce(add,range(10))

print reduce(add, [1, 3, 5, 7, 9])

