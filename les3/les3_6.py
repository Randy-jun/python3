#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(1))
print(fact(5))
print(fact(15))
print(fact(998))

#栈溢出解决方案，尾递归（和循环效果一样）
def facta(n):
    return facta_iter(n, 1)

def facta_iter(num, product):
    if num == 1:
        return product
    return facta_iter(num - 1, num * product)

print(facta(1))
print(facta(5))
print(facta(15))
print(facta(997))
#print(facta(1000))
#汉诺塔问题

import time

def move(n, a, b, c):
    if n == 1:
        print('move', a, '---->', c)
        return
    move(n - 1, a, c, b)
    print('move', a, '---->', c)
    move(n - 1, b, a, c)
t_start = time.clock()
move(20, 'A', 'B', 'C')
t_end = time.clock()
print(t_end - t_start)
