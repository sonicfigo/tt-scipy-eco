# coding=utf-8
"""
5 numpy的基础运算 (教学教程)

numpy 中的加减乘除和 python 的类似.
但矩阵的运算可能就不太一样.
矩阵的乘法是以 np.dot() 的形式.

axis=0 垂直
axis=1 水平
"""

import numpy as np

a = np.array([10, 20, 30, 40])
b = np.arange(4)  # [0 1 2 3]
print('原a')
print(a)
print('原b')
print(b)
print(a, b)

print('')
print('a - b')
print(a - b)
print('a + b')
print(a + b)
print('b ** 2')
print(b ** 2)  # b的平方

print('\n三角函数')
print(10 * np.sin(a))  # 对a的每个值求sin，再乘以10
print(10 * np.cos(a))
print(10 * np.tan(a))

print('\n比较')
print(b < 3)  # b里的哪些值是小于3的
print(b == 3)

print('\narray/矩阵1(a2)')
a2 = np.array([[1, 1], [0, 1]])
print(a2)
print('array/矩阵2(b)')
b = np.arange(4).reshape((2, 2))
print(b)

print('array相乘a2 * b（python方式）')
print(a2 * b)

print('矩阵相乘np.dot(a2, b)（数学矩阵方式）')
print(np.dot(a2, b))
print('矩阵相乘第二种写法')
print(a2.dot(b))

print('\n随机')
a3 = np.random.random(size=(2, 4))  # 随机0 ~ 1的2 * 4矩阵
print(a3)

print('所有和')
print(np.sum(a3))  # 所有的和， axis=1行求和，axis=0列求和
print('垂直求和')
print(np.sum(a3, axis=0))
print('水平求和')
print(np.sum(a3, axis=1))

print('min')
print(np.min(a3))  # axis同理，不举例
print(np.min(a3, axis=0))  # 垂直最小
print(np.min(a3, axis=1))  # 水平最小

print('max')
print(np.max(a3))
print(np.max(a3, axis=0))
print(np.max(a3, axis=1))


