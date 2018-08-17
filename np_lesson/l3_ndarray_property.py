# coding=utf-8
"""
3 numpy 属性 (教学教程)

numpy 的属性基本上有这几种常用到的,
np.size
np.shape
np.ndim
"""
import numpy as np

array1 = np.array([
    [1, 2, 3],
    [2, 3, 4]
])  # 默认就是dtype=np.int64

print(type(array1))  # <type 'numpy.ndarray'>, i.e  n-dimension array
print(array1)
print('number of dimension:', array1.ndim)  # 2
print ('shape:', array1.shape)  # (2, 3)
print('size:', array1.size)  # 6
print('itemsize:', array1.itemsize)  # 8，每个item 的 bytes
print('dtype:', array1.dtype)  # int64
# print('data:%s' % str(array1.data)) # 无法print出来

assert array1.dtype == np.int == int  # 整数默认就是 np.int == int == int64

assert np.array([[1.0]], dtype=np.float64).dtype == np.float == float  # np.float不知道是几位的
