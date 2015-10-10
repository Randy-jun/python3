#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(9))
print(my_abs(-9))
def nop():
    pass
def my_abs1(x):
    if not isinstance(x, (int, float)):
        raise TypeError('Bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs1(9))
print(my_abs1(-9))
#print(my_abs1('9'))
