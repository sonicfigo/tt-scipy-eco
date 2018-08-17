# coding=utf-8
"""
13 image 图片
x，y两个轴上的每个点，对应cmap里的某个颜色，最后显示成一个图片
"""

import matplotlib.pyplot as plt
import numpy as np

# image data
a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3, 3)

print(a)
"""
参数：
for the value of "interpolation", check this:
http://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html

for the value of "origin"= ['upper', 'lower'], check this:
http://matplotlib.org/examples/pylab_examples/image_origin.html
origin: lower or upper ,黑白的位置会相反

"""
plt.imshow(a, interpolation='nearest', cmap='bone', origin='upper')
plt.colorbar()  # shrink=.92，压缩到92大小

# plt.xticks(())
# plt.yticks(())
plt.show()
