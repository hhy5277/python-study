#coding=utf-8

# 函数参数

# 默认参数

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print power(5) 

print power(5,2) # 和 print power(5)  因为power 方法的n参数默认为2

def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city

enroll('Sarah', 'F')


# 定义默认参数要牢记一点：默认参数必须指向不变对象！

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# 可变参数

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc([1, 2, 3])

# 把函数的参数改为可变参数：

def calc_1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc_1(1, 2)

# 关键字参数

# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：


def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

person('quanke',28)  # 在调用该函数时，可以只传入必选参数

person('Bob', 35, city='Beijing')  # 

# 参数组合

def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw