#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc([1, 2, 3, 4]))
print(calc([1, 2, 3]))
print(calc([1, 2, 3, 4, 5, 6]))

def calca(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
nums = [1, 2, 3]
print(calca(nums[0], nums[1], nums[2]))
print(calca(*nums))

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city = 'Beijing')
person('Adma', 435, gender = 'M', city = 'Beijing')

extra = {'city': 'Beijing', 'job': 'Engineer'}

person('Jack', 34, city = extra['city'], job = extra['job'])
person('Jack', 34, **extra)


def persona(name, age, **kw):
    if 'city' in kw:
        #有city参数
        pass
    if 'job' in kw:
        #有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

def personb(name, age, *, city, job):
    print(name, age, city, job)

personb('Jack', 24, city = 'Beijing', job = 'Teacher' )
#personb('Jack', 24, city = 'Beijing', dsa = 'dsad', job = 'Teacher' )
#personb('Jack', 24, dsad = 'dsads', city = 'Beijing', job = 'Teacher' )
#参数定义的顺序必须是：必选参数，默认参数，可变参数/命名关键字参数和关键字参数
def f1(a, b, c = 0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c = 0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, c = 3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x = 99)
f2(1, 2, d = 88, ext = None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}

f1(*args, **kw)

args1 = (2, 3, 4)
f2(*args1, **kw)
'''
*args是可变参数，args接收的是一个tuple
**kw是关键字参数，kw接收的是一个dict
'''
