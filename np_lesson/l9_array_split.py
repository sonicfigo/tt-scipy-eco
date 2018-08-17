# coding=utf-8
"""
9 numpy的 array分裂 (教学教程)

numpy array 同样是可以进行分割的,
包括横向和纵向分割:
A = np.arange(12).reshape((3,4))

print(np.split(A, 4, axis=1))
print(np.vsplit(A,3))
print(np.array_split(A, 3, axis=1)) # 不等分割
"""

import numpy as np

A = np.arange(12).reshape((3, 4))

"""
可以理解为分割后的效果，是水平的。
如何理解'horizontal/水平'？因为分开的两块在维度上是水平的，通过水平合并可以复原。

如 A变成
A1→ ←A2
"""
print('\naxis=1 左右、水平分割(左右断成2块，维度上是相互水平的)。')
list1 = np.split(A, 2, axis=1)
print(list1)
print('写法2')
print (np.hsplit(A, 2))

"""如 A变成
A1
↓
↑
A2
"""
print('\naxis=0 等量上下、垂直分裂(上下分裂3块，维度上是相互垂直的)。')
print (np.split(A, 3, axis=0))
print('写法2')
print (np.vsplit(A, 3))

print('\n左右分裂，不等量')
print (np.array_split(A, 3, axis=1))

print('\n=============原数据')
print (A)
