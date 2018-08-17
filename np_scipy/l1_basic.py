# coding=utf-8
"""
slice出来的 ndarray2， 与原ndarray指针共享
"""

import numpy as np

x2 = np.array([1, 2, 3, 4])
print(x2)

y2 = x2[:-1]
assert (np.array([1, 2, 3]) == y2).all()

x2[0] = 9
assert (np.array([9, 2, 3]) == y2).all()
