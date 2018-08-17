# coding=utf-8
"""
reshape vs resize
flatten vs ravel
"""

"""
reshape     返回新对象
resize      修改元对象
"""
import numpy as np

a1 = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])

print(a1.shape)
print(a1)

print('\rreshape返回新对象，不影响a1')
a1_reshape = a1.reshape(5, 2)
print(a1_reshape)
print('\na1不变')
print(a1)

print('\nresize不返回，直接操作a1')
a1.resize(5, 2)
print('\na1变了')
print(a1)

print("""
reshape(x, -1)， x行，-1表示列自己计算
""")
c1 = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
print(c1)

print('\n===================reshape -1，就是自动根据 总数/n_samples 来得到 n_features ')
print(c1.reshape(5, -1))
