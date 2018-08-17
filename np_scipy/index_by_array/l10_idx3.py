# coding=utf-8
"""
a[i,j]
    - i，j是数字时，就是 第i行，第j个
    - i，j是矩阵时，就是 i 矩阵表示1维， j矩阵表示2维， elementwise 相拼，组成某个索引，找到原数据的[ix,jx]
"""
import numpy as np

a = np.arange(12).reshape(3, 4)

"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
"""
print(a)
print(a[0][1])
print(a[0, 1])

print("""
i,j 是二维index
a[i,j]既
i   1维的索引
j   2维的索引

[i,j]就是
0,2     1,1
1,3     2,3
""")
i = np.array([[0, 1],  # indices for the first dim of a
              [1, 2]])
j = np.array([[2, 1],  # indices for the second dim
              [3, 3]])
print(a[i, j])

print("""
i,2
1维为i， 2维全部为2""")
print(a[i, 2])
