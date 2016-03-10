#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 面向对象高级编程
# 使用__slots__

class Student(object):
    pass

s = Student()
s.name = 'Michael'
print(s.name)

#绑定方法

def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

s2 = Student()
#s2.set_age(42)

def set_score(self, score):
    self.score = score

Student.set_score = MethodType(set_score, Student)

s.set_score(99)
print(s.score)

s2.set_score(88)
print(s2.score)

#再定义class的时候，定义一个特殊的__slots__变量，可以限制该class实例能添加的属性

class Student1(object):
    __slots__ = ('name', 'age') #用tuple定义允许绑定的属性名称

s1 = Student1()
s1.name = 'Michael'
print('s1.name' + s1.name)
s1.age = 22
print('s1.age',s1.age)
#s1.score = 99
#print('s1.score' + s1.score)
# __slots__定义的属性仅对当前类实例起作用，对继承的子类不起作用

class GraduateStudent(Student1):
    pass

g = GraduateStudent()
g.score = 999
print(g.score)
#在子类中定义__slots__，这样子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
