# coding=utf-8
"""
合并的join用法
类似 sql语句的 outer join , inner join

concat 默认是axis=0， 垂直合并
"""

from __future__ import print_function
import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])

print('\n默认是outer join')
res = pd.concat([df1, df2])
print(res)

print('\ninner join')
res = pd.concat([df1, df2], join='inner', ignore_index=True)
print(res)

print('\n原数据')
print(df1)
print(df2)
