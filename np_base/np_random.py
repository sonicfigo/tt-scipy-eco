# coding=utf-8
"""
random模块
"""

import numpy as np

print("""
======================rand
Random values in a given shape.

输出一个shape为（d0, d1, …, dn）的矩阵。
""")
print(np.random.rand(3, 2))  # 值0~1，shape(3, 2)的矩阵

print("""
======================randn
Return a sample (or samples) from the "standard normal" distribution.

输出标准正太分布的矩阵。""")
print(np.random.randn(3, 2))

print("""
======================randint
Return random integers from `low` (inclusive) to `high` (exclusive).

生产一定范围内的元素为整数的array。""")
print(np.random.randint(low=3, size=(2, 4)))  # 0~2 (2,4)矩阵
print(np.random.randint(low=3, high=16, size=(2, 4)))  # 3~15 (2,4)矩阵

print("""
======================normal
Draw random samples from a normal (Gaussian) distribution.
""")
# 平均值=2， 标准差=1, 6个数据
print(np.random.normal(loc=2, scale=1, size=6))

print("""
RandomState随机数""")
random_state = np.random.RandomState(seed=0)  # 种子=0，就是每次都不固定
print(random_state.rand(2, 2))

print("""
随机分割list
""")
list1 = np.arange(10)
print(list1)

indices = np.random.permutation(len(list1))  # 与list个数一样的，index，随机打乱
print(indices)
print(list1[indices[:-5]])  # 可以作为train数据的index
print(list1[indices[-5:]])  # 可以作为test数据的index

print('\n===================np.random.normal')
# loc=0.0, scale=1.0, size=(2, 1)
print(np.random.normal(size=2))

# loc=0.0, scale=1.0, size=(2, 1)
print(np.random.normal(size=(2, 1)))
