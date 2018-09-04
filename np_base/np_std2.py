# coding=utf-8
"""

"""

import numpy as np

a = np.array([[1, 2], [3, 4]])

print('\n===================平均值')
print(np.mean(a))

print('\n===================全局方差')
print(np.var(a))

print('\n===================计算全局标准差')
print(np.std(a))  # 1.1180339887498949

print('\n===================行/列标准差')
# print(np.std(a, axis=0))  # axis=0计算每一列的标准差
# print(np.std(a, axis=1))  # 计算每一行的标准差
