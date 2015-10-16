#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 迭代器

from collections import Iterable

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# 生成器

from collections import Iterator

print(isinstance((x for x in range(10)),Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable,但缺不是Iterator
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数

print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))
