#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack'] 
print([L[0], L[1], L[2]])

r = []
n = 3
for i in range(n):
    r.append(L[i])

print(r)

print(L[0: 3])# L[a: b] 从a开始取b个元素出来，负数则表示从尾部开始算起

L = list(range(100))
print(L)
# 取前十个
print(L[:10])
# 取后十个
print(L[-10:])
# 取前11-20
print(L[10:20])
# 前十个没两个取一个
print(L[:10:2])
# 所有的，没5个取一个
print(L[::5])
# 复制List
print(L[:])


# tuple也是一种list，tuple也可以用切片操作，结果仍是tuple
print((0, 1, 2, 3, 4, 5, 6, 7, 8)[:5:2])

# 'xxx'也可以看成是一种list，每一个元素就是一个字符，结果仍是字符串
print('ABCDEFGHIGKL'[:7:3])
