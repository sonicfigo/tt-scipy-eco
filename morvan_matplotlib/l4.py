# coding=utf-8
"""
4 figure 图像
matplotlib 的 figure 就是一个 单独的 figure 小窗口, 小窗口里面还可以有更多的小图片(axis).
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

# 按顺序 1，2设置 每个 plt.figure()
plt.figure()  # figure1
plt.plot(x, y1)

plt.figure(num=6, figsize=(8, 5))  # 6号figure，figure2
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

plt.show()
