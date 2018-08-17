# coding=utf-8
"""
深度复制

"""

import numpy as np

a = np.arange(12)
a.shape = 2, 6
print(a)

print("""
copy""")

a_copy = a.copy()
assert a_copy is not a  # 新的一个对象
assert a_copy.base is not a  # base 也不是 a
a_copy[0][0] = 111
print(a_copy)

print(a)
