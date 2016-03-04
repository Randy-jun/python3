#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 访问限制
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

bart = Student('Bart Simpson', 98)
#print(bart.__name)
'''
要让内部属性不被外部访问，可以把属性的名称前加上双下划线__,在
Python中，实例的变量名如果以__开头，就变成一个私有变量(private),只有
内部可以访问，外部不能访问。

在Python中，变量名类似__xxx__的，也就是以双下划线开头的，
并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，
不是private变量，所以不能用__name__、__score__这样的变量名

有些时候，会看到以一个下划线开头的实例变量名，比如_name，这样的
实例变量外部是可以访问的，但是，按照约定俗成的规定，当看到这样的
变量时请视为私有变量，不要随意访问
###  双下划线开头的实例变量是不是一定不能从外部访问呢？ 其实不是。
不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name,
所以，仍然可以通过_Studetn__name来访问__name变量
（不同版本的解释器可能改成不同的名字）
'''
print(bart._Student__name)

