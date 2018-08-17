# coding=utf-8
"""
合并 by index

index既左边的0，1，2，3，4，5...
"""
from __future__ import print_function
import pandas as pd

left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                    index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])

print('\n左右两个index都考虑了')
print(pd.merge(left, right, left_index=True, right_index=True, how='outer',
               indicator=True))

print('\n原数据')
print(left)
print(right)
