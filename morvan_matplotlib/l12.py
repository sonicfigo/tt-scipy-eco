# coding=utf-8
"""
12 contours 等高线图
等高线：俯视的2d地图
"""
import matplotlib.pyplot as plt
import numpy as np


def get_height(x, y):
    """
    the height function ， 根据输入的 x，y，计算出高度。
    无需care这个函数的细节，只需知道是计算高度即可
    """
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

# x,y 绑定为网格的输入值
X, Y = np.meshgrid(x, y)  # 底图，是一个mesh，网格。高度是指网格上的一个点的高度

print(X.shape)
print(Y.shape)
"""
1. 画底色 contourf
contour filling color
X, Y and value for (X,Y) point

参数：
- X为mesh过的x
- Y为mesh过的y
- z为高度
- 8: 等高线要分为多少份，最少为2份（至少，1高1低）
- alpha：0.75 透明度
- cmap：hot 的 color map，每一个z的值，对应cmap-hot里的一个颜色(可以改为'cool'看变化)
"""
plt.contourf(X, Y, get_height(X, Y), 7, alpha=.75, cmap=plt.cm.hot)

"""
2. 画轮廓线 contour
"""
C = plt.contour(X, Y, get_height(X, Y), 8, colors='black', linewidth=.5)

"""
3. 写文字
contour label

参数
inline:画在线里面 
"""
# plt.clabel(C, inline=True, fontsize=10)

plt.xticks(())
plt.yticks(())
plt.show()
