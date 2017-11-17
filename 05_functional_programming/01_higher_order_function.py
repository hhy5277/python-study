#coding=utf-8

# 高阶函数英文叫Higher-order function。

# 函数本身也可以赋值给变量，即：变量可以指向函数。

f = abs

print f(-10)


# 函数名也是变量

# 那么函数名是什么呢？函数名其实就是指向函数的变量！对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数！


# 传入函数

def add(x, y, f):
    return f(x) + f(y)

print add(-5, 6, abs)

