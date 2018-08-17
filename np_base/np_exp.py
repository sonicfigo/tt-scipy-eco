# coding=utf-8
"""
用 np.exp 指数，来分配softmax 总和为1的概率
"""
from __future__ import division
import numpy as np

scores = [3.0, 1.0, 0.2]

print('指数分配softmax')
exp_of_scores = np.exp(scores)  # 常数e 3,1,2次方 [ 20.08553692   2.71828183   1.22140276]
sum_exp = np.sum(exp_of_scores, axis=0)  # 3个n次方的和, 24.0252215098
dist1 = exp_of_scores / sum_exp  # [ 0.8360188   0.11314284  0.05083836]
print(np.sum(dist1))  # 为什么不等于1？精度问题？

print('原数值分配softmax，直接除以总和')
sum_pure = np.sum(scores)  # 4.2
dist2 = scores / sum_pure  # [ 0.71428571  0.23809524  0.04761905]
assert 1.0 == np.sum(dist2)
