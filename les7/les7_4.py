#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 继承和多态

class Animal(object):

    def run(self):
        print('Animal is running...')

class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    
    def run(self):
        print('Cat is running...')

dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()
#cat.eat()

#判断一个变量是否是某个类型可以用isinstance()判断
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(cat, Cat))

def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Animal())
run_twice(Dog())
'''
对于静态语言来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者其它的子类，
否则将无法调用run()方法。对于Python这样的动态语言来说，则不一定需要传入Animal类型，
我们只需要保证传入的对象有一个run()方法就可以了。
这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，
一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

Python的"file-like object"就是一种鸭子类型
'''
