#coding=utf-8

# list
print [x * x for x in range(10)]

a = dict({"a":1,"b":2})

for s in a:
    print s

# generator

g = (x * x for x in range(10))
print g


print g.next()

for n in g:
    print n


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

fib(6)


# def f(x,l=[]):
#     for i in range(x):
#         l.append(i*i)
#     print l
 

# f(3)