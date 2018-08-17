# coding=utf-8
"""
print 一个 ndarray

太大的ndarry，会缩略打印，如果想完整用：
np.set_printoptions(threshold='nan')
"""

import numpy as np

a = np.arange(6)  # 1d array
print('a')
print(a)

b = np.arange(12).reshape(4, 3)  # 2d array
print('b')
print(b)

"""
[[[ 0  1  2  3]

  [ 4  5  6  7]

  [ 8  9 10 11]]



 [[12 13 14 15]

  [16 17 18 19]

  [20 21 22 23]]]

"""
print('\n===')
c = np.arange(24).reshape(2, 3, 4)  # 3d array
print(c)

"""
[[[[ 0  1  2  3]
   [ 4  5  6  7]
   [ 8  9 10 11]]

  [[12 13 14 15]
   [16 17 18 19]
   [20 21 22 23]]]


 [[[24 25 26 27]
   [28 29 30 31]
   [32 33 34 35]]

  [[36 37 38 39]
   [40 41 42 43]
   [44 45 46 47]]]]
"""
print('\n===')
d = np.arange(48).reshape(2, 2, 3, 4)  # 3d array
print(d)
