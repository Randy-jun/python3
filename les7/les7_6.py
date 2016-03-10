#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 实例属性和类属性

#给实例绑定属性，通过实例变量或者self变量

class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

print(s.name)
print(s.score)

class Student1(object):
    name = 'Student'

s1 = Student1()
print(s1.name)
print(Student1.name)

s1.name = 'Michael'
print(s1.name)
print(Student1.name)

del s1.name
print(s1.name)
'''
从上面的例子可以看出，在编写程序的时候，千万不要把实例属性
和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是
当删除实例属性后，再使用相同名称，访问到的将是类属性
'''
