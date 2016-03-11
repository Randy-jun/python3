#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#多重继承

class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass
'''
MixIn
在设计类的继承关系时，通常，主线都是单一继承下来的，如果要“混入”额外的
功能，通过多重继承就可以实现。
MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑
通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。

Python自带的很多库也使用了MixIn。举个例子，Python自带了TCPServer和
UDPServer这两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，
这两种模型由ForkingMixIn和ThreadingMixIn提供。通过组合，我们就可以创造出合适的服务来。
'''
