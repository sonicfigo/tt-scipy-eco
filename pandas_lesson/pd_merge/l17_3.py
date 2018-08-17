# coding=utf-8
"""
indicator 用来说明详情
"""
from __future__ import print_function
import pandas as pd

df1 = pd.DataFrame({'key1': [0, 1], 'left': ['a', 'b']})
df2 = pd.DataFrame({'key1': [1, 2, 2], 'right': [2, 2, 2]})

print('\n说明merge详情')
print(pd.merge(df1, df2, on='key1', how='outer', indicator='为啥合并成这样的原因^.^',))

print('\n原数据')
print(df1)
print(df2)
