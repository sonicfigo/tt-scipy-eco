# coding=utf-8
"""
过滤：
1. value过滤：                    用 df[df.foo == 'bar']
2. label of column index 过滤：   用 df.filter(items=['列名1', '列名2'])
3. label of row index 过滤：      用 df.filter(like='行index名1')
"""

import pandas as pd
from sklearn import datasets

iris = datasets.load_iris()

print('target对应的鸢尾名字')
iris_names = iris.target_names[iris.target]
# print(iris_names)

df_iris = pd.DataFrame(dict(column1=iris_names))

# print(df_iris.index)
# print(df_iris.sort_values(by='column1', ascending=False))

print('\nvalue 过滤')
filter_setosa = df_iris[(df_iris.column1 == 'setosa')]
print('setosa 有%s个' % len(filter_setosa))

# print('\nlabels of index 过滤')
# df_type1 = df_iris.filter(like='setosa', axis=1)
# print('labels 有%s个' % len(df_type1))

print('\nlabel of index(列label 行label) 过滤')

print('\n列label fitler ========================== ')
print(df_iris.filter(items=['column2']))  # 150行， 但是0column，因为没有 column2 这个列名

print('\n行label filter ========================== ')
print(df_iris.filter(like='33', axis=0))  # 0是一维的，既行label为33的，就2个 33/133

print('\n原数据')
# print(df_iris)
