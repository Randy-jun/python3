#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用枚举类

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',\
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
#value属性则是自动赋给成员的int常量，默认从1开始计数。

from enum import Enum, unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(day1 == Weekday.Mon)
print(day1 == Weekday.Tue)
print(Weekday(1))
print(day1 == Weekday(1))
#print(Weekday(7))
for name, member in Weekday.__members__.items():
    print(name, '=>', member)

