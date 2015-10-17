#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# sorted

print(sorted([36, 5, -12, 9, -21]))

print(sorted([36, 5, -12, 9, -21], key = abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit']))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower, reverse = True))

def by_name(n):
    return n[0]

def by_score(n):
    return n[1]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(L, key = by_name))
print(sorted(L, key = by_score, reverse = True))
