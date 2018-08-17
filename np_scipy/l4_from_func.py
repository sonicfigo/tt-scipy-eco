# coding=utf-8
"""
使用函数，创建ndarray

"""

import numpy as np

"""
shape(5,4)，等于传入的参数 x, y 依次是
0,0
0,1
0,2
0,3

1,0
1,1
...

4,2
4,3
"""


def f(x, y):
    return 10 * x + y


b = np.fromfunction(f, (5, 4), dtype=int)
print(b)

print('\n索引1、2的行，所有的列')
print(b[1:3, :])

print('\n索引2、3的行，索引1,2列')
print(b[2:4, 1:3])
