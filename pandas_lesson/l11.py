# coding=utf-8
"""
我们说到了如果 numpy 是 python 中的列表的话,
那pandas 就是 python 中的字典.
numpy 是 list like
pandas 是 dict like

我们还介绍了pandas 的基本用途,包括如何创建 pandas
series
和
dataframe, 还有查看他们的一些属性。
"""

import pandas as pd
import numpy as np

print('\nSeries')
s = pd.Series([1, 3, 6, np.nan, 44, 1])
print(s)

print('\ndate_range')
dates = pd.date_range('20160101', periods=6)  # 描述行的索引
print(dates)

print('\nDataFrame 类似二维matrix')
# random 6行4列的数据
# row 是日期， column是abcd
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
print(df)

print('\n不指定row column，默认')
df1 = pd.DataFrame(np.arange(12).reshape((3, 4)))
print(df1)

print('\ndict输入DataFrame')
df2 = pd.DataFrame(dict(A=1.,
                        B=pd.Timestamp('20130102'),
                        C=pd.Series(1, index=list(range(4)), dtype='float32'),
                        D=np.array([3] * 4, dtype='int32'),
                        E=pd.Categorical(["test", "train", "test", "train"]),
                        F='foo'))
print(df2)

print('\n每一列属性')
print(df2.dtypes)

print('\n行名 列名')
print(df2.index)
print(df2.columns)  # 列名

print('\n值')
print(df2.values)

print('\n描述(只有数字型的)')
print(df2.describe())

print('\n逆矩阵')
print(df2.T)

print('\n排序index（列index），倒序')
print(df2.sort_index(axis=1, ascending=False))

print('\n排序index（行index）')
print(df2.sort_index(axis=0, ascending=False))

print('\n排序value（E列值）')
print(df2.sort_values(by='E'))

print('\n原数据')
print(df2)
