# coding=utf-8
"""
17 pandas 合并 merge (教学教程tutorial)

pandas 中的 merge 和 concat 类似,但主要是用于两组有 key column 的数据,统一索引的数据.
通常也被用在 database 的处理当中.
"""
from __future__ import print_function
import pandas as pd
import numpy as np

# merging two df by key/keys. (may be used in database)
# simple example
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

print('\n使用key合并(单主键)')
res = pd.merge(left, right, on='key')
print(res)

print('\n原数据')
print(left)
print(right)

print('\n===================numpy 的c_用法')
print('np.c_是按行连接两个矩阵，就是把两矩阵左右相加，要求行数相等，类似于pandas中的merge()。\n')
print(np.c_[left, right])
print(np.c_[left, right].shape)  # (4, 6)
