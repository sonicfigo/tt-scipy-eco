# coding=utf-8
"""
指定索引，然后操作
"""

import numpy as np

a = np.arange(10) ** 3
print(a)
print(a[2])
print(a[2:5])

"""
从 0 到 6 ， 每隔两个，设值为-1000
"""
print('\n设置1000')
#  from start to position 6, exclusive, set every 2nd element to -1000
a[:6:2] = -1000  # equivalent to a[0:6:2] = -1000
print(a)

"""
开三次方根
"""

for i in a:
    print('对 %5s 开三次方:%s' % (i, i ** (1 / 3.)))
