# coding=utf-8
"""
ndarray 基础操作
"""

import numpy as np

a = np.array([20, 30, 40, 50])
b = np.arange(4)
print('\n===================原始数据a')
print(type(a))
print(a)
print('\n===================原始数据b')
print(type(b))
print(b)  # [0 1 2 3]

print('\n===================a - b')
c = a - b
print(c)  # [20 29 38 47]

print('\n=================== b ** 2')
print(b ** 2)  # [0 1 4 9]

print('\n===================sin')
print(10 * np.sin(a))

print('\n===================a < 35')
print(a < 35)  # [ True  True False False]

print('\n===================')
print(np.hstack((a, b)))
