# coding=utf-8
"""

"""

import numpy as np

x = '1234'

y = np.frombuffer(x, dtype=np.int8)
print(y.data)
print(y.base is x)
print(y)

print ('\n======')
print(y.flags)
