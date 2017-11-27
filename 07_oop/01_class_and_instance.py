#coding=utf-8

class Student(object):
    
    def __init__(self,name,score):
        self.name = name
        self.score = score

# bart = Student()

# bart.name="quanke"

# print bart.name

bart = Student('Bart Simpson', 59)

print bart.name

