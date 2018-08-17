# coding=utf-8
"""
14 3D 数据

"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax3d = Axes3D(fig)  # 添加3d坐标轴, x,y,z

# X, Y value
X = np.arange(-4, 4, 0.25)  # -4 ~ 4，每隔0.25取一个值，共 32 个
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)  # mesh 到底面
R = np.sqrt(X ** 2 + Y ** 2)

Z = np.sin(R)  # 对应每一个x，y，都有一个高度值z，height value

"""
============= ================================================
        Argument      Description
        ============= ================================================
        *X*, *Y*, *Z* Data values as 2D arrays
        
        row/column 每一格跨度
        *rstride*     Array row stride (step size), defaults to 10
        *cstride*     Array column stride (step size), defaults to 10
        
        *color*       Color of the surface patches
        
        *cmap*        A colormap for the surface patches.
        
        *facecolors*  Face colors for the individual patches
        *norm*        An instance of Normalize to map values to colors
        *vmin*        Minimum value to map
        *vmax*        Maximum value to map
        *shade*       Whether to shade the facecolors
        ============= ================================================
"""

ax3d.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))

"""
==========  ================================================
        Argument    Description
        ==========  ================================================
        *X*, *Y*,   Data values as numpy.arrays
        *Z*

        等高线是从哪个轴，压扁下去，既 3d 变 2d
        *zdir*      The direction to use: x, y or z (default)
        
        从所选zdir的那个坐标轴的0点，压到哪个位置，既这个2d要显示在那个 zdir 的位置，就是方便查看而已
        *offset*    If specified plot a projection of the filled contour
                    on this position in plane normal to zdir
        ==========  ================================================
"""
ax3d.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))

ax3d.set_zlim(-2, 2)  # 限制z的高度 2 ~ -2

plt.xlabel('I am x')
plt.ylabel('I am y')
plt.show()
