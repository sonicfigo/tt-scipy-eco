# coding=utf-8
"""

"""
from __future__ import division
import numpy as np

A = np.arange(-14, -2).reshape(3, 4)

print('\n===================原值A')
print(A)

print('\n===================平均值')
print(np.mean(A))

print('\n===================方差')
print(np.var(A))

print('\n===================std函数')
print(np.std(A))

print('\n===================std手工')
mean_is_85 = np.full((3, 4), -8.5)
print(mean_is_85)

print('每个值-平均值')
print(A - mean_is_85)

print('(每个值-平均值)平方')
print((A - mean_is_85) ** 2)

print('(每个值-平均值)平方的和')
print(np.sum((A - mean_is_85) ** 2))

print('(每个值-平均值)平方的和 / 12 ，既是var 方差')
variance = np.sum((A - mean_is_85) ** 2) / 12
print(variance)

print('std 标准差：方差，开方')
print(np.power(variance, 1 / 2))
