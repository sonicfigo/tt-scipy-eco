# coding=utf-8
"""
高级索引方式：根据array来索引

1维原数据 + 1维索引/多维索引
将原一维数据，指定index，变形为多维矩阵，index是矩阵形式。
"""

import numpy as np

a = np.arange(12) ** 2
i = np.array([1, 1, 3, 8, 5])

print(a)

print("""
1维index，结果还是1维""")
print(a[i])

print("""
2维index，结果就是2维""")
j = np.array([[3, 4],
              [9, 7]])
print(a[j])


