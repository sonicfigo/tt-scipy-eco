# coding=utf-8
"""
ndarray 默认类型

整形：int64
浮点：float64
"""

import numpy as np

array_int64 = np.array([2, 3, 4])
assert int == array_int64.dtype
print('\n===================', array_int64.dtype)

array_float64 = np.array([2.1, 3.1, 4.1])
assert float == array_float64.dtype
print('\n===================', array_float64.dtype)
