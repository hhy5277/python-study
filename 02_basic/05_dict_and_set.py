#coding=utf-8

# 使用键-值（key-value）存储，具有极快的查找速度。

d = {"quanke":1,"ting":2}

print d

print d["quanke"] # 取值

d['ting'] = 21

print  d["ting"]

# 通过in判断key是否存在：

print 'quanke' in d

# 删除一个key，用pop(key)方法，对应的value也会从dict中删除：

d.pop("quanke")

print d

######################set#################

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

s = set([1, 2, 3])

print s

s.add(4)

print s

s.remove(4)

print s

