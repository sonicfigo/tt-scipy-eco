# coding=utf-8
"""
12 pandas 选择数据 (教学教程tutorial)

pandas 中选择数据的方法有很多种,一般我们会用到这4种.
    1. 根据标签: loc   label-location
    2. 根据序列: iloc  index-location
    3. 根据混合的这两种: ix
    4. 条件筛选
"""

from __future__ import print_function
import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])

print("\ndf['A']")
print(df['A'])

print('\ndf.A')
print(df.A)

print('\n第0~3行')
print(df[0:3])

print('\n根据标签，选择两个日期内的行')
print(df['20130102':'20130104'])

print('\n=========label location')
print('\n根据标签，选择行 20130102')
print(df.loc['20130102'])

print('\n根据标签，选择所有行，列A, B')
print(df.loc[:, ['A', 'B']])

print('\n根据标签，选择行 20130106，列A, B')
print(df.loc['20130102', ['A', 'B']])

print('\n========index location')
print('\n根据位置，第3行')
print(df.iloc[3])
print('\n根据位置，第3行第1列')
print(df.iloc[3, 1])
print('\n根据位置，第3~4行第1~2列')
print(df.iloc[3:5, 1:3])
print('\n根据位置，逐个，如1,3,5')
print(df.iloc[[1, 3, 5], 1:3])

print('\n混合 index 和 label')
print(df.ix[:3, ['A', 'C']])

print('\n条件筛选')
print(df[df.A > 8])

print('\n输出是Series')
print(type(df.iloc[3]))

print('\n原数据')
print(df)
