# coding=utf-8
"""
10 scatter 散点图
当然, matplotlib 是可以做散点图 scatter 的.
而且还可以做散点图很多特效, 我们来看看吧.
"""
import matplotlib.pyplot as plt
import numpy as np

n = 1024  # data size
X = np.random.normal(0, 1, n)  # 1024 个随机点，Mean 是0，Standard deviation 是 1
Y = np.random.normal(0, 1, n)

T = np.arctan2(Y, X)  # for color later on，用于颜色

# plt.figure()  # figure1
# plt.scatter(X, Y, s=75, c=T, alpha=.5)  # size 75， 透明度 50%
#
# plt.xlim(-1.5, 1.5)  # 限制在 -1.5 , 1.5范围
# plt.xticks(())  # ignore xticks
# plt.ylim(-1.5, 1.5)
# plt.yticks(())  # ignore yticks

# 一条线的散点图
plt.figure()  # figure2

# x轴是 (5, )
# y轴是 (5, )
# 两者1-1对应画出 5 个点
plt.scatter(np.arange(0, 5), np.arange(100, 105), s=3)

plt.show()
