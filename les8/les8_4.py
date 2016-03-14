#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 定制类

class Student(object):
    
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__

print(Student('Michael'))

'''
直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()
返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，
__repr__()是为调试服务的。
-----------------------------------------------------------------------
如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现
一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环
就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到
StopIteration错误时退出循环。
'''
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration();
        return self.a

for n in Fib():
    print(n)

class Fib1(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

print('----------------------------------------')
f = Fib1()

print(f[0])
print(f[19])
print(f[25])
print(f[64])
print(f[100])

print('----------------------------------------')
print(list(range(100))[5:11])

print('----------------------------------------')

class Fib2(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
f2 = Fib2()
print(f2[0:6])
print(f2[:4])
print(f2[6:11])
print(f2[0:22:3])
print('----------------------------------------')
class Student1(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
s1 = Student1()
print(s1.name)
print(s1.score)
print('----------------------------------------')
class Student2(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 55

s2 = Student2()
print(s2.age())
'''
注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，
比如name，不会在__getattr__中查找'''
print('-----------------2----------------------')
'''
此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。
要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
'''
class Student3(object):

    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 66
        raise AttributeError('\'Student3\' object has no attribute \'%s\'' % attr)
s3 = Student3()
print(s3.age())
#print(s3.name())
print('----------------------------------------')
class Chain(object):
    def __init__(self, path=''):
        print('********')
        self._path = path
        print(self._path)
        print('********')

    def __getattr__(self, path):
        print(path)
        print(self._path)
        print('===')
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list.name.tom)
print('----------------------------------------')
class Student4(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s4 = Student4('Michael')
s4()
print('----------------------------------------')
'''
一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。
能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
__call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以
把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期
创建出来的，这么一来，我们就模糊了对象和函数的界限。
那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被
调用，能被调用的对象就是一个Callable对象。
'''
print(callable(Student4))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('str'))
