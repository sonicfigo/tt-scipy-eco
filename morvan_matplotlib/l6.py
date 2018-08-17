# coding=utf-8
"""
6 设置坐标轴2
这次会说到在我们如何移动matplotlib 中 axis 坐标轴的位置.
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
plt.xlim((-1, 2))
plt.ylim((-2, 3))

# set new ticks 设置刻度
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)

# set tick labels 说明文字，可以使用转义字符
plt.yticks([-2, -1.8, -1, 1.22, 3],
           ['$really\ bad$', '$bad$', '$normal$', '$good$', '$really\ good$'])
# to use '$ $' for math text and nice looking, e.g. '$\pi$'

ax = plt.gca()  # gca = 'get current axis'

# 隐藏右和上的脊柱(边框)，既保留了左和下脊柱
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 声明x,y轴(既会标上刻度)
ax.xaxis.set_ticks_position('bottom')  # 下脊柱做x轴
# ACCEPTS: [ 'top' | 'bottom' | 'both' | 'default' | 'none' ]
ax.yaxis.set_ticks_position('left')  # 左脊柱做y轴
# ACCEPTS: [ 'left' | 'right' | 'both' | 'default' | 'none' ]

# 移动xy轴
ax.spines['bottom'].set_position(('data', 0))  # x轴绑定在data( 既是y轴的0数值位置 )
ax.spines['left'].set_position(('data', 0))  # y轴绑定在data( 既x轴的0的数值位置 )
# the 1st is in 'outward' | 'axes' | 'data'
# outward: 未知，还不确定
# axes: percentage of y axis
# data: depend on y data


plt.show()
