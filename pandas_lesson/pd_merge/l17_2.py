# coding=utf-8
"""
how = ['left', 'right', 'outer', 'inner']
"""
from __future__ import print_function
import pandas as pd

left = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'key1': ['K0', 'K0', 'K1', 'K2'],
    'key2': ['K0', 'K1', 'K0', 'K1'],
})
right = pd.DataFrame({
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3'],
    'key1': ['K0', 'K1', 'K1', 'K2'],
    'key2': ['K0', 'K0', 'K0', 'K0'],
})

print('\ninner-key合并(复合主键)')
print(pd.merge(left, right, on=['key1', 'key2'], how='inner'))  # default for how='inner'

print('\nleft-key合并(复合主键)')
print(pd.merge(left, right, on=['key1', 'key2'], how='left'))

print('\nright-key合并(复合主键)')
print(pd.merge(left, right, on=['key1', 'key2'], how='right'))

print('\nouter-key合并(复合主键)')
print(pd.merge(left, right, on=['key1', 'key2'], how='outer'))

print('\n原数据')
print(left)
print(right)
