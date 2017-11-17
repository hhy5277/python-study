# coding=utf-8

import os
# 生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用range(1, 11)：

print range(1, 11)

# 生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：

L = []
for x in range(1, 11):
    L.append(x * x)

print L


# 列表生成式则可以用一行语句代替循环生成上面的list：

print [x * x for x in range(1, 11)]

# 还可以使用两层循环，可以生成全排列：

print [m+n for m in 'ABC' for n in 'XYZ']

# 列出当前目录下的所有文件和目录名，可以通过一行代码实现：
print [d for d in os.listdir(".")]

