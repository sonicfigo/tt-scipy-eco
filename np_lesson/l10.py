# coding=utf-8
"""
10 numpy的 copy & deep copy (教学教程)

如果直接把 numpy array赋值给另一个变量,
改变任意的一个变量都会影响到其他变量.
比如:
a = np.arange(4)
b = a
a[0] = 11
那这是b[0] 也会变成11

如果不想这样,
我们就会要用到 deep copy 的概念:
b = a.copy()来只附加 a 的值给 b, 并没有关联 a 去 b.
"""

import numpy as np

a = np.arange(4)

print (a)
b = a  # b就是a
c = a.copy()  # c不是a, deep copy

print (id(a))
print (id(b), b is a)
print (id(c), c is a)
