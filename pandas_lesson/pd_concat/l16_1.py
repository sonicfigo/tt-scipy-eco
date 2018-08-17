# coding=utf-8
"""
16 pandas 合并 concat (教学教程tutorial)

pandas 处理多组数据的时候往往会要用到数据的合并处理,使用 concat 是一种基本的合并方式.
而且 concat 中有很多参数可以调整,合并成你想要的数据形式.
"""
from __future__ import print_function
import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])

print('\n垂直合并')
res1 = pd.concat([df1, df2, df3], axis=0)
print(res1)
print('\n有重复的三个label为0的， 用ignore_index解决')
print(res1.loc[0])

print('\n垂直合并，忽略index， 自动变为0~8')
res2 = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(res2)

print('\n原数据')
print(df1)
print(df2)
print(df3)
