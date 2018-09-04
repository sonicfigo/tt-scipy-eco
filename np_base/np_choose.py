# coding=utf-8
"""
np.choose(a, choices)
    - a ，       index
    - choices，  用来选取的源数据

按 a，既index 的shape，从choices里挑来数据
"""
import numpy as np

a1 = [[1, 0, 1],
      [0, 1, 0],
      [1, 0, 1]]
choices1 = [-10, 10]

merged_array = np.choose(a1, choices1)
print(merged_array)

print('\n===================原list')
print(a1)

print('\n===================')
a2 = [2, 3, 1, 0]
choices2 = [[0, 1, 2, 3],
            [10, 11, 12, 13],
            [20, 21, 22, 23],
            [30, 31, 32, 33]]

foo = np.choose(a2, choices2)

"""
2，[2][0]，第 [2] list，第 [0] 个item
3，[3][1]，第 [3] list，第 [1] 个item
1，[1][2]，第 [1] list，第 [2] 个item
0，[0][3]，第 [0] list，第 [3] 个item
"""
print(foo)
