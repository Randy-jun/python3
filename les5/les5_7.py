#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 装饰器

def now():
    print('2015-10-17')

f = now
f()
print(now.__name__)
print(f.__name__)

'''
现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，
称之为“装饰器”（Decorator）。

本质上，decorator就是一个返回函数的高阶函数。
所以，我们要定义一个能打印日志的decorator，可以定义如下：
'''

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，
# 并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：

@log
def now1():
    print('2015-10-17')

now1()
print(now1.__name__)
# 把@log 放到 now()函数定义处，相当于执行了 now = log()

def logad(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logad('execute')
def now2():
    print('2015-10-17')

print('--------------------------')
now2()
print(now2.__name__)
# 这样的话，执行后会把now2()函数的__name__改变

import functools

def log1(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log1
def now3():
    print('2015-10-17')
print('-----------------------')
now3()
print(now3.__name__)

import functools

def log1ad(text):    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log1ad('execute')
def now4():
    print('2015-10-17')
print('----------------------')
now4()
print(now4.__name__)
