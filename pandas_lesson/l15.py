# coding=utf-8
"""
15 pandas 导入导出 (教学教程tutorial)

使用 pandas 进行文件的导入导出是一件非常简单的事情.
具体信息和各种使用方法可以查看 pandas 的网站: http://pandas.pydata.org/pandas-docs/...
"""

import pandas as pd

# read from
data = pd.read_csv('student.csv')
print(data)

# save to
data.to_pickle('student.pickle')
