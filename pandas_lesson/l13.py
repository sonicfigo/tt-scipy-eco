# coding=utf-8
"""
13 pandas 设置值 (教学教程tutorial)

我们可以根据自己的需求, 用 pandas 进行更改数据里面的值, 或者加上一些空的,或者有数值的列.
"""

import numpy as np
import pandas as pd

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
df_origin = df.copy()

print('\n基于 index 和 label')
df.iloc[1, 2] = 1111
df.loc['20130101', 'B'] = 2222
print(df)

print('\n条件修改, A>4的行，B置为0')
df.B[df.A > 4] = 0
print(df)

print('\n增加一新列,值为空nan')
df['E'] = np.nan
print(df)

print('\n增加一新列，对齐到原行的index，若没有就NaN')
df['F'] = pd.Series(data=[1, 2, 3, 4, 5, 6], index=pd.date_range('20130101', periods=6))
df['G'] = pd.Series(data=[1, 2, 3, 4, 5, 6], index=pd.date_range('20130103', periods=6))
print(df)

print('\n原数据')
print(df_origin)
