# coding=utf-8
"""
5 设置坐标轴 axis setting
在 matplotlib 中如何设置坐标轴的范围, 单位长度, 替代文字等等.

http://www.scipy-lectures.org/intro/matplotlib/matplotlib.html
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure()
plt.plot(x, y2)
# plot the second curve in this figure with certain parameters
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

# set x limits
# 坐标轴范围
plt.xlim((-1, 2))
plt.ylim((-2, 3))
# 文字
plt.xlabel('I am x')
plt.ylabel('I am y')

# region ticks 设置单位小标

# x单位小标
new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)

# y单位小标
# set tick labels
plt.yticks([-2, -1.8, -1, 1.22, 3],
           ['$really\ bad$', r'$bad\ \alpha$', r'$normal$', r'$good$',
            r'$really\ good$'])

# endregion
plt.show()
