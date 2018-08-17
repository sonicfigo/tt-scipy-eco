# coding=utf-8
"""
用y的条件true，false
来取对应的X位置
"""
import numpy as np

X = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])

print([y != 7])
print(X[y != 7])
print(y[y != 7])
