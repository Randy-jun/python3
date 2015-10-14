#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {'a': 4, 'b': 2, 'c': 3 }

for key in d:
    print(key)

for value in d.values():
    print(value)

for k, v in d.items():
    print(k, v)

for ch in 'ABCDEFGH':
    print(ch)

# 通过collections的Iterable类型判断来确定对象是否可以迭代
from collections import Iterable

print(isinstance('abcdefg', Iterable))
print(isinstance([1, 2, 3, 4], Iterable))
print(isinstance(123, Iterable))

# Python内置的enumerate函数可以把一个list变成索引-元素对

for i, value in enumerate(['A', 'B', 'C']):
    print(i ,value)
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
