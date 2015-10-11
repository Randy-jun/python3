#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def power(x):
    return x * x
print(power(7))

def powern(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(powern(2, 3))
print(powern(2, 5))
print(powern(2, 7))
print(powern(2, 10))

def powerdn(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(powerdn(4))
print(powerdn(4, 1))
print(powerdn(4, 2))
print(powerdn(4, 3))
'''必选参数放在前面，默认参数放在后面，否则Python解释器会报错。当多个参数时，变化大的放在前面，变化小的放在后面，就可以作为默认参数。
    有多个参数，调用时，既可以按照顺序提供默认参数，比如enroll('Bob', 'M', 7)，也可以不按顺序提供不认默认参数。当不按顺序提供部分参数时，需要把参数名写上。比如enroll('Adam', 'M', city = 'Tianjin')
'''
#默认参数的坑，所以默认参数必须使用不变对象
def add_end(L = []):
    L.append('END')
    return L

print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))
print(add_end())
print(add_end())
print(add_end())
print(add_end())
print(add_end())
print(add_end())
def add_endc(L = None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_endc([1, 2, 3]))
print(add_endc(['x', 'y', 'z']))
print(add_endc())
print(add_endc())
print(add_endc())
print(add_endc())
print(add_endc())
