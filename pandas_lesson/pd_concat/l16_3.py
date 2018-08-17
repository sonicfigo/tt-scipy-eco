# coding=utf-8
"""
axis=1， 水平合并

join_axes = 谁的index，就以谁的index为主
"""

from __future__ import print_function
import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])

print('\naxis=1水平合并, index 全出现。')
print(pd.concat([df1, df2], axis=1))

print('\naxis=1水平合并, 以df1为主')
print(pd.concat([df1, df2], axis=1, join_axes=[df1.index]))

print('\n原数据')
print(df1)
print(df2)
