#coding=utf-8
# python 基础 类型和变量

# 以#开头的语句是注释

a = 100

# 当语句以冒号“:”结尾时，缩进的语句视为代码块。

if a >= 0:
    print a
else:
    print -a

# 注意，Python程序是大小写敏感


# -------------------------数据类型-------------------------- #

# 1.整数 ：包括负整数 
# 2.浮点数：就是小数
# 3.字符串：字符串是以''或""括起来的任意文本，比如'abc'，"xyz"等等

# 如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识，比如：

i_m_ok = 'I\'m \"OK\"!'

print i_m_ok

# 转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\

print 'I\'m learning\nPython.' # Python 这个字符应该换换了

print '\\\n\\'

# Python允许用r''表示''内部的字符串默认不转义

print '\\\t\\'

print r"\\\t\\"

# Python允许用'''...'''的格式表示多行内容

print '''ting1
ting2
ting3
'''

# 多行字符串'''...'''还可以在前面加上r使用

print r'''ting_r_1
ting_r_2\n
ting_r_3\n
'''


# 4.布尔值：True、False表示布尔值（请注意大小写）

print True
print False

print '\n'

print 3>2
print 3<2

# 布尔值可以用and、or和not运算

print 'and运算是与运算，只有所有都为True，and运算结果才是True:'

print True and True

print True and False

print False and False

print 'or运算是或运算，只要其中有一个为True，or运算结果就是True：'

print True or True
print True or False
print False or False

print 'not运算是非运算，它是一个单目运算符，把True变成False，False变成True：'

print not True
print not False

# 5.空值：空值是Python里一个特殊的值，用None表示。None不能理解为0
# 5.列表
# 6.字典
