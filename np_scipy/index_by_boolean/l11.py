# coding=utf-8
"""

"""
import numpy as np

a = np.arange(12).reshape(3, 4)
print(a)

b1 = np.array([False, True, True])  # first dim selection
b2 = np.array([True, False, True, False])  # second dim selection

print("""
过滤1维""")
print(a[b1, :])  # selecting rows
print('写法2')
print(a[b1])  # same thing

print("""
过滤2维""")
print(a[:, b2])  # selecting columns

print("""
奇怪的过滤，还未搞懂""")
print(a[b1, b2])  # a weird thing to do


