# coding=utf-8
"""
14 3D 数据

要点：x，y mesh 出来的 ndarray，shape 是 (y数， x数)
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax3d = Axes3D(fig)  # 添加3d坐标轴, x,y,z

# X, Y value
X = np.arange(-3, 1, 0.5)  # -4 ~ 4，每隔0.25取一个值，共 32 个
Y = np.arange(-1, 1, 0.5)
print('\n===================mesh前')
print(X.shape)  # (8, ) 既(x_shape1, )
print(X)
print(Y.shape)  # (4, ) 既(y_shape1, )
print(Y)
print('\n===================mesh后')
X, Y = np.meshgrid(X, Y)  # mesh 到底面
print(X.shape)  # (y_shape1, x_shape1)
print(X)
print(Y.shape)  # (y_shape1, x_shape1)
print(Y)

R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)  # 对应每一个x，y，都有一个高度值z，height value

ax3d.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))

ax3d.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))

ax3d.set_zlim(-2, 2)  # 限制z的高度 2 ~ -2

plt.xlabel('I am x')
plt.ylabel('I am y')

print(X)
print(Y)
print(R)
plt.show()
