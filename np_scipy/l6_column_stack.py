# coding=utf-8
"""
column_stack：将一维矩阵的列，堆成行。既(1, x) 变形为 (x, 1)

1 维的时候，等同于：列堆成行，再水平合并
2 维的时候，等同于：直接水平合并
"""

import numpy as np

# from numpy import newaxis

print("""
1维的""")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a)
print(b)
print('')
print(np.column_stack((a, b)))  # With 2D arrays
# print(np.vstack((a, b)))
print(np.hstack((a, b)))

print("""
2维的""")
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
print(x)
print(y)
print('')
print(np.column_stack((x, y)))  # With 2D arrays
# print(np.vstack((x, y)))
print(np.hstack((x, y)))
