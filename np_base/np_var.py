# coding=utf-8
"""

"""

import numpy as np

a1 = np.array([1, 2, 7])
print('\n===================a1')
print('平均值')
print(np.mean(a1))
print('方差')
"""
方差：(每个值 - 平均值)的平方，求和，除以3

2.33333333333 平方 = 5.444444444428889
1.33333333333 平方 = 1.777777777768889
3.66666666667 平方 = 13.444444444468889
3个合 除以3
得方差：6.888888888888889
"""
print(np.var(a1))

print('方差开方 = 标准差，2.62466929133727')
print(np.std(a1))

print('\n===================a2')
a2 = np.array([1, 2, 2, 7, 8])
print('平均值')
print(np.mean(a2))
print('方差')
print(np.var(a2))
print('标准差')
print(np.std(a2))
