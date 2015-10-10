#!/usr/bin/env python3
# -*- coding: utf-8 -*-
age = 20
if age >= 18:
    print('Your age is', age)
    print('Adult')

age = 3
if age >= 18:
    print('Your age is', age)
    print('Adult')
else:
    print('Your age is', age)
    print('Teenager')

age = 3
if age >= 18:
    print('Adult')
elif age >=6:
    print('Teenager')
else:
    print('Kid')
