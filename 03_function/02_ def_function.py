#coding=utf-8

# 定义函数
tol = 51

suc = 20

fal = 30

print "总共测试%s条数据，成功%s条，失败%s条！" %(tol , suc , fal)


# 1. def + 函数名（参数）：
#2 . 返回值

def testApi(x,y=2):
    print "test api %s %s" % (x,y)

testApi(1)



def my_abs(x):
    print "x value is %s" % x
    if x > 0:
        return x
    else:
        return -x


print my_abs(-10)

# 定义一个什么事也不做的空函数，可以用pass语句：



def nop():
    pass


# 参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance实现：


def my_abs_2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x


# my_abs_2(1)

# 返回多个值

import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


print move(100, 100, 60, math.pi / 6)

x, y = move(100, 100, 60, math.pi / 6)

print x, y
