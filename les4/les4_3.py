#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 列表生成 List Comprehensions
l = list(range(1, 11))
print(l)

L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

L1 = [x * x for x in range(1, 11)]
print(L1)

L2 = [x * x for x in range(1, 11) if x % 2 == 0]
print(L2)

L3 = [m + n for m in 'ABCD' for n in 'XYZT']
print(L3)

import os
L4 = [d for d in os.listdir('.')]
print(L4)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)

d1 = {'x': 'A', 'y': 'B', 'z': 'C'}
L5 = [k + '=' + v for k, v in d1.items()]
print(L5)

L6 = ['Hello', 'World', 'IBM', 'Apple']
L7 = [s.lower() for s in L6]
print(L7)

L8 = ['Hello', 'World', 18, 'IBM', 'Randy-Jun', 'Apple']
L9 = [s.lower() for s in L8 if isinstance(s, str)]
print(L9)
