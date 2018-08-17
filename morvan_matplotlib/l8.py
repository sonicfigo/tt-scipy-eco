# coding=utf-8
"""
8 Annotation 标注
在用 matplotlib 做标注 annotation 的时候,我们其实可以用两种方法,
    一种是用 plt 里面的 annotate,
    一种就是直接用 plt 里面的 text 来写标注.
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2 * x + 1

plt.figure(num=1, figsize=(8, 5), )
plt.plot(x, y, )

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

# # 要添加的点
x0 = 1
y0 = 2 * x0 + 1
plt.scatter(x0, y0, s=50, color='b')  # plot一个点(1,3), size50
"""
画一条虚线，参数意义：
- x 轴范围是 x0 ~ x0
- y 轴范围是 0 ~ y0
- k-- 是 black 虚线
"""
plt.plot([x0, x0, ], [0, y0, ], 'k--', linewidth=2.5)

# method 1:
#####################
plt.annotate(r'$2x+1=%s$' % y0,
             xy=(x0, y0),  # 就是精准的打出 x，y（而不是 x的10%，y10%之类的）
             xycoords='data',  # xy的坐标，以data的值为基准
             xytext=(+30, -30),  # 在点的位置，+30，-30，开始打印文字描述，与 textcoords 参数有关
             textcoords='offset points',
             fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2")
             )

# method 2:
########################
plt.text(-3.7, 3, r'$This\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size': 16, 'color': 'r'})

plt.show()
