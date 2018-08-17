# coding=utf-8
"""
14 pandas 处理丢失数据 (教学教程tutorial)

有时候我们导入或处理数据, 会产生一些空的或者是 NaN数据,如何删除或者是填补这些 NaN 数据就是我们今天所要提到的内容.
"""
from __future__ import print_function
import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])

df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
df_origin = df.copy()

print('\n原数据')
print(df_origin)

print('\n有任一NaN的行，丢掉')
print(df.dropna(axis=0, how='any'))  # how = {'any', 'all'}

df = df_origin.copy()  # 回到原始，用于二次测试
print('\n有任一NaN的列，丢掉')
print(df.dropna(axis=1, how='any'))

df = df_origin.copy()
print('\n填空')
print(df.fillna(value=0))

df = df_origin.copy()
print('\n是否NaN')
print(df.isnull())
is_any_nan = np.any(df.isnull())
print(is_any_nan)
print(type(is_any_nan))
print(is_any_nan == True)  # 不能用is True， 类型不同

print('\n原数据')
print(df_origin)
