# coding=utf-8
"""
7 numpy的索引 (教学教程)

我们了解了如何对 numpy array 进行索引, 可以用到一下各种形式:
A[2, 3]
A[:, 1]
A[1] = A[1, :]
for row in A: print(row)
for column in A.T: print(column)
for element in A.flat: print(element)
"""

import numpy as np

A_flat = np.arange(3, 15)
print(A_flat)
print(A_flat[3])

A = np.arange(3, 15).reshape(3, 4)
print('\n原数据')
print(A)

print('\n索引整行')
print(A[2])  # 行2

print('\n索引单个')
print(A[1][1])  # 行1列1的那个数
print(A[2, 1])  # 第二种写法

print('\nlist cut A[行，列]')
print(A[2, :])  # 行2所有
print(A[:, 1])  # 列1所有
print(A[1, 1:3])  # 行1，列1~2的数

print('\n迭代行')
for row in A:
    print(row)

print('\n迭代列')
for column in A.T:
    print(column)

print('\n迭代item')
for item in A.flat:  # A.flat是迭代器
    print(item)

print('\n原矩阵')
print(A)


print('\n打平flatten')
print(A.flatten())
