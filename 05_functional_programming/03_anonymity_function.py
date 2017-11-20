#coding=utf-8

# 匿名函数

f = lambda x: x * x

print f(10)

# 也可以把匿名函数作为返回值返回，比如

def build(x, y):
    return lambda: x * x + y * y