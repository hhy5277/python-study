#coding=utf-8

# @log
def now():
    print '2017-11-17'

f = now

f()

# 函数对象有一个__name__属性，可以拿到函数的名字：
print f.__name__

print now.__name__


# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

# def log(func):
#     def wrapper(*args, **kw):
#         print 'call %s():' % func.__name__
#         return func(*args, **kw)
#     return wrapper


# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print '%s %s():' % (text, func.__name__)
#             return func(*args, **kw)
#         return wrapper
#     return decorator


import functools

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print 'call %s():' % func.__name__
#         return func(*args, **kw)
#     return wrapper

@log("test")
def now_1():
    print '2017-11-17'


now_1()

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator