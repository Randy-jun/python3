#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 获取对象信息

print(type(123))
print(type('str3'))
print(type(None))
print(type(abs))

#对比两个变量type类型是否相同
print(type(123) == type(4567))
print(type(123) == int)
print(type('abc') == type('123'))
print(type('abc') == str)
print(type('abc') == type(123))

#判断基本数据类型可以直接写int, str等，但如果要判断一个对象是否是函数则可以使用types模块中定义的常量
import types

def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

class Animal(object):
    pass

class Dog(Animal):
    pass

class Husky(Dog):
    pass

a = Animal()
d = Dog()
h = Husky()

print(isinstance(h, Husky))
print(isinstance(h, Dog))
print(isinstance(h, Animal))
print(isinstance(d, Dog) and isinstance(d, Animal))

#能用type()判断的基本类型也可以用isinstance()判断
print(isinstance('a', str))


#并且还可以判断一个变量是否是某些类型中的一种

print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))
#要获得一个对象所有的属性和方法，可以使用dir(0函数，返回一个包含字符串的list
print(dir('ABC'))

print(len('2321321'))
print('2321321'.__len__())

class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog))

#配合getattr()、setattr()、以及hasattr()可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9
    
    def power(self):
        return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(getattr(obj, 'y'))
print(obj.y)

#getattr(obj, 'z')
#传入一个默认值
print(getattr(obj, 'z', 404))

