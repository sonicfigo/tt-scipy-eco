# coding=utf-8
"""

"""
import numpy as np

print(np.sin(90))

# 45°的几种表示方式
"""
2 * np.pi 表示 360度
360 / 45 = 8
所以
45 = 360 / 8
"""
angle45 = 2 * np.pi / 8
print(angle45)  # 45度的参数数值

"""
360 除以 360份，乘以45份
"""

print(2 * np.pi / 360 * 45)

"""
简化为
'"""
print(np.pi / 180 * 45)

print('\n===================45°的sin正弦值:')
print(np.sin(angle45))
