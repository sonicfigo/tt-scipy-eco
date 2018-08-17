# coding=utf-8
"""
3 基本用法
"""

import matplotlib.pyplot as plt
import numpy as np

# % matplotlib inline

x = np.linspace(-1, 1, 50)  # 曲线的话，如果点num 太少，画出的图很丑
# y = 2 * x + 1
y = x ** 2
plt.plot(x, y)
plt.show()
