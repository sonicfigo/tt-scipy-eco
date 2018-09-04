# coding=utf-8
"""
searchsorted(a, v)
Find indices where elements should be inserted to maintain order.

排序好的a，v插入时，应该插在那个 index ？
"""
import numpy as np

array1 = np.searchsorted([1, 2, 3, 4, 5], 3)

array2 = np.searchsorted([1, 2, 3, 4, 5], 3, side='right')

"""
达到一个效果
参数2的个数及位置不变，所有值，都变成了参数1范围内的, 1 ~ 5
"""
array3 = np.searchsorted([1, 2, 3, 4, 5], [-10, 10, 2, 3])

print(array1)  # 2

print(array2)  # 3

print(array3)  # [0 5 1 2]

a = np.linspace(0, 256, 6)
print(a)

print(np.searchsorted(a, [-1, 1, 200, 300]))

print(np.mean(a))
