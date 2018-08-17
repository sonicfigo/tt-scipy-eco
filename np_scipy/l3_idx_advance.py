# coding=utf-8
"""
三个点的用法

"""

import numpy as np

print('\na 3D array (two stacked 2D arrays)')
c = np.array([[[0, 1, 2],
               [10, 12, 13]],
              [[100, 101, 102],
               [110, 112, 113]]])

assert (2, 2, 3) == c.shape

print('\n第一维的索引1 的全部')
print(c[1])

print('\n写法2')
print(c[1, ...])

print('\n最后一维的索引2，之前维度为全部')
print(c[..., 2])
