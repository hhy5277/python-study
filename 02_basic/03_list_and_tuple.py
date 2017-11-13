#coding=utf-8

# list是一种有序的集合，可以随时添加和删除其中的元素。

# 列出班里所有同学的名字，就可以用一个list表示：

classmates = ['Michael', 'Bob', 'Tracy']

print classmates

# 用len()函数可以获得list元素的个数
print "classmates 长度:",len(classmates)

# 用索引来访问list中每一个位置的元素，记得索引是从0开始的：

print classmates[0] # 打印的应该是Michael

# 用-1做索引，直接获取最后一个元素：

print classmates[-1] # 打印的应该是Tracy

print classmates[-2] # 打印的应该是Bob

# 可以把元素插入到指定的位置，比如索引号为1的位置：


classmates.insert(1,"ting") 

print classmates  # 打印应该是['Michael', 'ting', 'Bob', 'Tracy']

#要删除list末尾的元素，用pop()方法：

classmates.pop()

print classmates # 打印的应该是 ['Michael', 'ting', 'Bob']

#删除指定位置的元素，用pop(i)方法，其中i是索引位置：

classmates.pop(1) # 打印应该是

print classmates # ['Michael', 'Bob']

classmates[1] = 'Sarah'

print classmates

# list里面的元素的数据类型也可以不同，比如：

print ['keatingr',123,True]

# list元素也可以是另一个list，比如：

print ['keatingr',classmates,False]

################------  tuple -----####################

# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：

classmatesTuple = ('Michael', 'Bob', 'Tracy')

print classmatesTuple

# 要定义一个只有1个元素的tuple，如果你这么定义：
t = (1)
print t

# 定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
# 所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：

t = (1,)

print t


