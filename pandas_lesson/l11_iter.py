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

2018-08-07 添加遍历代码
"""

import pandas as pd
import numpy as np

print('\ndict输入DataFrame')
df2 = pd.DataFrame(dict(A=1.,
                        B=pd.Timestamp('20130102'),
                        C=pd.Series(1, index=list(range(4)), dtype='float32'),
                        D=np.array([3] * 4, dtype='int32'),
                        E=pd.Categorical(["test", "train", "test", "train"]),
                        F='foo'))

print('\n===================行遍历↓ iterrows')
for row_idx, row_series in df2.iterrows():
    print('row_idx-%s' % row_idx)
    for col_idx, row_sery in enumerate(row_series):
        print('%10s-%s: %20s' % ('col_idx', col_idx, row_sery))

print('\n===================行遍历，namedtuple 实例 itertuples')
for pandas_obj in df2.itertuples():
    print(pandas_obj)

print('\n===================列遍历→ iteritems')
for col_name, col_series in df2.iteritems():
    print('\ncol_name-%s' % col_name)
    print('%-50s' % col_series)

print('\n原数据')
print(df2)
