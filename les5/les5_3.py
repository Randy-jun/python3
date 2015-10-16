#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filter

def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15])))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

# 用filter求素数
'''
计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
首先，列出从2开始的所有自然数，构造一个序列：
2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
不断筛下去，就可以得到所有的素数。
用Python来实现这个算法，可以先构造一个从3开始的奇数序列：
'''
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 1000:
        print(n)
    else:
        break
# 上面这个程序再python3之前不能，因为python3之前的filter不是惰性计算

# 回数，从左向右或者从右向左都一样
print('-----------------------------------')

def is_palindrome(n):
    strl = str(n)
    l = len(strl)
    n = l // 2
    #str1 = str[:: -1] # 这种切片可以反转
    str1 = strl[: n]
    if (l % 2) == 1:
        str2 = strl[: n: -1]
    else:
        str2 = strl[: n - 1: -1] # 字符转str[:b:-1]除去str[0]到str[b]剩下的反转
    return str1 == str2

print(list(filter(is_palindrome, range(1, 10000000))))
