#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @property的使用

class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value

s = Student()
s.set_score(88)
print(s.get_score())
#s.set_score(888)

#使用@property装饰器
class Student1(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s1 = Student1()
s1.score =68
print(s1.score)
#s1.score = 888

class Student2(object):

    @property
    def birth(self):
        return self._birth
    
    @birth.setter
    def birth(self, value):
        if not isinstance(value, int):
            raise ValueError('birth must be an integer!')
        if value < 1900 or value > 2016:
            raise ValueError('birth must between 1991 ~ 2016!')
        self._birth = value

    @property
    def age(self):
        return 2016 - self._birth
s2 = Student2()
s2.birth = 1993
print(s2.birth)
print(s2.age)

#s2.birth = '1991'
#s2.birth = 3991
