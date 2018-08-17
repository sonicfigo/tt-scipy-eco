# coding=utf-8
"""
名字重复的column， 如何在合并后显示
"""
from __future__ import print_function
import pandas as pd

boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})

print('\nage是重名的column')
print(pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner'))

print('\n原数据')
print(boys)
print(girls)
