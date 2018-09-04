# coding=utf-8
"""
6 numpy的基础运算2 (教学教程)

np.argmax()
np.argmin()
np.average()
np.mean()
np.median()
np.cumsum()
np.diff()
np.nonzero()
np.sort()
np.transpose() or a.T
np.clip()
"""
import numpy as np

# A = np.arange(2, 14).reshape(3, 4)
A = np.arange(-14, -2).reshape(3, 4)
A_REVERSE = np.arange(14, 2, -1).reshape(3, 4)
print('\n===================原值A')
print(A)

print('\n大小值')
print(np.min(A))  # 最小值2
print(np.argmin(A))  # 最小值2的索引indices 0

print(np.max(A))
print(np.argmax(A))

print('\n平均值')
print(np.mean(A))
print(A.mean())
print(np.average(A))  # average 与mean一样

print('\n平均值axis')
print(np.mean(A, axis=0))  # col平均值
print(np.mean(A, axis=1))  # row平均值

print('\n中位数')
print(np.median(A))

print('\n之前逐个项累加')
print(np.cumsum(A))

print('\n累差')
print(np.diff(A))

print('\n非零的行数(array1) 与 列数(array2)')
print(np.nonzero(A))

print('\n逐行排序')
print(A_REVERSE)
print(np.sort(A_REVERSE))

print('\n逆矩阵')
print(np.transpose(A))
print('\n逆矩阵第二种写法')
print(A.T)

print('\n裁剪数据')
print(np.clip(A, a_min=5, a_max=9))

print('\naxis参数')
print(np.mean(A))
print('axis参数 0/列-垂直方向')
print(np.mean(A, axis=0))
print('axis参数 1/行-水平方向')
print(np.mean(A, axis=1))

print('\nunique')
print(np.unique(A))


print('\n=====================原数据')
print(A)
