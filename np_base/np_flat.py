# coding=utf-8
"""
flatten 和 ravel 区别
- flatten     独立指针, copy一个新对象, owndata=True
- ravel       共享指针, owndata=False

ravel 更快，更轻
"""

import numpy as np

b1 = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
print('\n===================b1')
print(b1)

b1_flatten = b1.flatten()
print('\n===================b1_flatten')
print(b1_flatten)

b1[0][1] = 111
print(b1_flatten)
assert b1_flatten.flags.owndata is True
assert id(b1) != id(b1_flatten)

print('\nravel 会受源对象 data的影响, 虽然确实是不同实例（id不一样）')

b2 = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
b2_ravel = b2.ravel()

print('===================原来b2 与 b2_ravel')
print(b2)
print(b2_ravel)

b2[0][2] = 222

print('\n===================b2变了, =b2_ravel也跟着变了')
print(b2)
print(b2_ravel)

assert b2_ravel.flags.owndata is False
assert id(b2) != id(b2_ravel)
