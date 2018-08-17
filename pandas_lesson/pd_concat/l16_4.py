# coding=utf-8
"""
append
"""

from __future__ import print_function
import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])

print('\ndf1为主，把df2, df3加在df1屁股后面')
print(df1.append([df2, df3], ignore_index=True))

print('\n单行添加Series')
s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(df1.append(s1, ignore_index=True))

print('\n原数据')
print(df1)
print(df2)
print(df3)
