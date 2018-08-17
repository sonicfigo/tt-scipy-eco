# coding=utf-8
"""
4 numpy 的创建 array (教学教程)
创建 array 有很多形式, 文档：
https://docs.scipy.org/doc/numpy-dev/user/quickstart.html

高精度：用64位
省空间：用16/32位
"""

import numpy as np

print('\n一维数组')
a1 = np.array([2, 23, 4], dtype=np.int)  # np.int 默认就是  int64
print(a1)
print(a1.dtype)
print(a1.shape)

print('\n二维，矩阵')
a2 = np.array([[2, 23, 4],
               [2, 23, 4]])
print(a2)

print('\n二维，矩阵，写法2')
a22 = np.array([(2, 23, 4),
                (2, 23, 4)])
print(a22)

print('\n0矩阵')
a0 = np.zeros((3, 4))
print(a0)

print('\n1矩阵3*4')
a11 = np.ones((3, 4))
print(a11)

print('3d')
a3d = np.ones((3, 4, 5))  # 大于2d的，每次debug里只能看最后两个维度，如 a3d[0] 的 4*5的矩阵
print(a3d)

print('4d')
a4d = np.ones((3, 4, 5, 6))  # 大于2d的，每次debug里只能看最后两个维度，如 a4d[0] 的 5*6的矩阵
print(a4d)

print('\nempty随机数')
"""
array([[ -2.31584178e+077,  -2.31584178e+077,   2.25005508e-314,
          2.24636165e-314],
       [  2.24578814e-314,   2.24638294e-314,   0.00000000e+000,
          0.00000000e+000],
       [  2.24338559e-314,   0.00000000e+000,  -2.32035340e+077,
          1.29073943e-231]])
"""
a_empty = np.empty((3, 4))
print(a_empty)

print('\n从10 ~ 19, step 2')
a_arange1 = np.arange(10, 20, 2)
print(a_arange1)

print('\n从0 ~ 11， 且变形为3行4列')
a_range2 = np.arange(12).reshape((3, 4))
print(a_range2)

print('\n线段')
a_line = np.linspace(1, 10, 6).reshape((2, 3))  # 1 ~ 10, 分6段， 第一段为1，其余5段均分
print(a_line)
