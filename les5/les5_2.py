#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# map/reduce

def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(list(r))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce

def add1(x, y):
    return x + y

print(reduce(add1, [1, 3, 5, 7, 9]))

def fn(x, y):
    return x * 10 + y

print(reduce(fn, [1, 3, 5, 7, 9]))

def fn1(x, y):
    return x * 10 + y

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print(reduce(fn1, map(char2num, '123456')))

# 整理一下
def str2int(s):
    def fn0(x, y):
        return x * 10 + y
    def char2num0(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num0, s))

print(str2int('12381247839'))

# 使用lambda函数进一步简化

def char2num1(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int1(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num1, s))

print(str2int1('64738264'))
