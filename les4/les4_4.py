#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 生成器

L = [x * x for x in range(10)] # 列表生成式，一次性就全部得到了
print(L)

g = (x * x for x in range(10)) # 生成器，创造了一个算法（占内存少）
print(g)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


g1 = (x * x for x in range(10)) # 生成器，创造了一个算法（占内存少）
for n in g1:
    print(n)

    def fib(max):
        n, a, b = 0, 0, 1
        while n < max:
            print(b)
            a, b = b, a + b
            n = n + 1
        return 'Done'
fib(10)

def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'Done'
print(fib1(10))

for n in fib1(10):
    print(n)
# 上面无法取到 return 的返回值

g = fib1(10)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

def odd():
    print('Step 1')
    yield 1
    print('Step 2')
    yield(3)
    print('Step 3')
    yield(5)

o = odd()
print(next(o))
print(next(o))
print(next(o))

# 杨辉三角

def triangles():
    L = [1]
    yield(L)
    L.append(1)
    yield(L)
    while True:
        L1 = tuple(L)
        for n in range(len(L1) - 1):
            L[n + 1] = L1[n] + L1[n + 1]
        L.append(1)
        yield(L)

# 上面这个方法法不是空间最优的会消耗2倍左右内存
# l如果是个list，L = l后，如果改变l的值，L也会一起改变

tri = triangles()
for x in range(15):
    print(next(tri))

