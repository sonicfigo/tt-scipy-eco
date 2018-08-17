# coding=utf-8
"""
类型自动转换，

向上： 不精确的 转为 精确的 允许  int -> float
向下： 精确的 转为 不精确的， 不允许  float -> int

a.dtype 是 int
b.dtype 是 float

b 可以 = b + a，
但
a 不可以= a + b

"""

import numpy as np

a = np.ones((2, 3), dtype=int)
a *= 3
print(a)

b = np.random.random((2, 3))
print(b)

b += a
print(b)

a += b  # b is not automatically converted to integer type
