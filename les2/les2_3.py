#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#tuple can not be redefine               
classmate_t = ('Machael', 'Bob', 'Tracy')
print(classmate_t)
print(classmate_t[1], classmate_t[2])
#只有一个元素的tuple，用:
t = (1,)
print(t)
#而不用
t1 = (1)
print(t1)
#空的tuple
t2 = ()
print(t2)
#“可变”的tuple
tl = ('a', 'b', ['A', 'B'])
print(tl)
tl[2][0] = 'X'
tl[2][1] = 'Y'
print(tl)
