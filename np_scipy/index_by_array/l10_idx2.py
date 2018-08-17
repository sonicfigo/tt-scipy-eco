# coding=utf-8
"""
多维的原数据 +  多维的索引
"""
import numpy as np

palette = np.array([[0, 0, 0],  # black
                    [255, 0, 0],  # red
                    [0, 255, 0],  # green
                    [0, 0, 255],  # blue
                    [255, 255, 255]])  # white
print("""
原数据 5 * 3""")
print(palette)
print(palette.shape)

print("""
索引shape是2 * 4，结果shape 就是 2*4，

每个item又是原对象的 [x, x, x]
""")
image = np.array([[0, 1, 2, 0],  # each value corresponds to a color in the palette
                  [0, 3, 4, 0]])
print(palette[image])  # the (2,4,3) color image
