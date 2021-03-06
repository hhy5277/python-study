#coding=utf-8
# 递归函数

# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。


def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print fact(1)

print fact(5)

print fact(100)

# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

def fact_1(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print fact_1(10000)