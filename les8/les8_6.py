#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用元类
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

from les8_6 import Hello

h = Hello()
h.hello()
print(type(Hello))
print(type(h))
print('------------------------------------------------')

def fn(self, name='world'):
    print('Hello, %s.' % name)

Hello1 = type('Hello1', (object,), dict(hello1=fn))#创建Hello1 class
h1 = Hello1()
h1.hello1()
print(type(Hello1))
print(type(h1))
print('------------------------------------------------')
'''
要创建一个class对象，type()函数依次传入3个参数：

1.class的名称；
2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，
  别忘了tuple的单元素写法；
3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello1上。

通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇
到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

metaclass

除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
metaclass，直译为元类，简单的解释就是：
当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。正常情况下，你不会碰到需要
使用metaclass的情况，所以，以下内容看不懂也没关系，因为基本上你不会用到。
'''

