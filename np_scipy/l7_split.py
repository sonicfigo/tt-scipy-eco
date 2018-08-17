# coding=utf-8
"""
不等量水平分割
"""

import numpy as np

a = np.arange(24).reshape(2, 12)
print(a)

"""
等量水平分割3分"""
print(np.hsplit(a, 3))

"""
不等量
从列索引3，4分隔开"""
print(np.hsplit(a, (3, 5)))
