# coding=utf-8
"""
Return evenly spaced values within a given interval.
按顺序和间隔，生成ndarray
"""

import numpy as np

print(np.arange(20))  # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
print(np.arange(1, 20))  # [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
print(np.arange(1, 20, 2))  # [ 1  3  5  7  9 11 13 15 17 19]
print(np.arange(2, 20, 2))  # [ 2  4  6  8 10 12 14 16 18]

"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]

 取
[[5 6]]
"""
arr = np.arange(12).reshape((3, 4))
print ('array is:')
print (arr)
# 取第一维的索引 1 到索引 2 之间的元素，也就是第二行
# 取第二维的索引 1 到索引 3 之间的元素，也就是第二列和第三列
print (arr[1:2, 1:3])


print(np.arange(2, 3, .02))
