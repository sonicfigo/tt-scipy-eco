# coding=utf-8
"""
11 bar 柱状图
matplotlib 中的 bar 条形图, 柱状图是如何使用的呢. 这就是一个简单好玩的例子.
"""
import matplotlib.pyplot as plt
import numpy as np

n = 12  # 12个向上，12个向下 柱状图
X = np.arange(n)  # 0 ~ 11 数字

Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)  # 0.5 ~ 1.0, 12个
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)  # 再次随机，以便区分Y1

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='k')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='k')

for x, y in zip(X, Y1):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')  # 位置 x右0.4，y上0.05

for x, y in zip(X, Y2):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x + 0.4, -y - 0.05, '-%.2f' % y, ha='center', va='top')

plt.xlim(-.5, n)
# plt.xticks(())
plt.ylim(-1.25, 1.25)
# plt.yticks(())

plt.show()
