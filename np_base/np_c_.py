# coding=utf-8
"""

"""

import numpy as np

foo = np.c_[.5, 1]  # 链接 2个 (1, )

print('\n=================== ')
print('np.c_是按行连接两个矩阵，就是把两矩阵左右相加，要求行数相等，类似于pandas中的merge()。')
print(foo)
print(foo.shape)  # (1, 2)

print('\n===================foo.T')
foo_T = foo.T
print(foo_T)
print(foo_T.shape)  # (2, 1)
