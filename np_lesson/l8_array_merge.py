# coding=utf-8
"""
8 numpy的 array 拼接 (教学教程)

numpy array 都可以进行两个或多个 array 的横向或纵向的合并.

我们可以用到:
np.vstack((A,B)) # 纵向合并
np.stack((A,B)) # 横向合并
或者:
np.concatenate((A,B,B,A), axis=1) # 选择你要合并的 axis
"""

import numpy as np

A = np.array([1, 1, 1])  # shape (3,)，既不是一个矩阵
B = np.array([2, 2, 2])
print('\n原数据A')
print(A)
print('\n原数据B')
print(B)

print('\n上下合并（A占第一行，B占第二行）')
C = np.vstack((A, B))  # (2, 3)
print('\nvstack 合并后为C')
print(C)  # vertical stack
print('\nshape')
print(C.shape)


print('\n水谁平/左右合并 （变成一整行）')
D = np.hstack((A, B))  # (6, )
print(D.shape)  # horizontal stack
print(D)

print('\nA 3个item分布成3列')
E = A[np.newaxis, :]  # [行，列]
print(E)
print(E.shape)  # (1, 3)，一行三列， 原数据A作为列，一行则是人为增加的维度

print('\nA 3个item分布到3行')
F = A[:, np.newaxis]  # [行，列]
print(F)
print(F.shape)  # 3 * 1, 三行一列， 原数据A作为行，一列则是人为增加的维度

print('\n转一维AB成为二维，且是翻转的，而后左右合并（目的是想要 A占第一列，B占第二列）')
AA = A[:, np.newaxis]
BB = B[:, np.newaxis]
AA_BB = np.hstack(tup=(AA, BB))
print(AA_BB)
print(AA_BB.shape)

print('\n指定维度合并-上下')
G = np.concatenate((AA, BB), axis=0)
print(G)
print(G.shape)  # 6, 1

print('\n指定维度合并-左右')
H = np.concatenate((AA, BB), axis=1)
print(H)
print(H.shape)  # 3, 2

print('\n原数据A B')
print(A)
print(B)

print('\n原数据AA BB')
print(AA)
print(BB)
