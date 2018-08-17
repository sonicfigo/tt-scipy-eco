# coding=utf-8
"""
如何对比两个ndarray:

(A==B).all()
"""

import numpy as np

nd1 = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])

nd2 = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])

print(type(nd1))

print("""
(nd1 == nd2).all()""")
print((nd1 == nd2).all())

print("""
elementwise 执行每个函数:""")

print("""
或查看每个element是否相等""")
print(nd1 == nd2)

print("""
nd1+nd2""")
print(nd1 + nd2)

print("""
""")
print((nd1 + nd2) > 10)
