#!/usr/bin/env python3
# -*- coding: utf-8 -*-
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
d['Jack'] = 88
print(d)
print('Tom' in d)
print('Jack' in d)
print(d.get('Tom'))
print(d.get('Jack'))
print(d)
print(d.pop('Jack'))
print(d)
