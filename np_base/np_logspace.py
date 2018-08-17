# coding=utf-8
"""
底数，真数，对数
"""

import math
import numpy as np

"""
python 自带match，log是求对数
"""
print(math.log(81, 9))  # 底数9，真数81， 求得对数2
print(math.log(10, 10))  # 底数10, 真数0，求得对数1

"""
而numpy 的 log space，
是均分一个范围，这个范围起终点是
10的x次方， 10的y次方
"""
s = np.logspace(2, 3, 5)  # 10的2次方， 10的3次方，既是 100 ~ 1000，等比选2个
print(s)

print(np.logspace(-4, -1, 6))  # 10 的 -4次方

print("""
np.log(x), 返回的是x的自然对数 ( natural_logarithm )
既是求一个指数/对数 natural_logrithm，使得自然常数（E）有：
10 = E 的 natural_logrithm 次方
""")

na_log = np.log(10)  # na_log，既结果是，10 的自然对数
print('10的自然对数 %s' % na_log)  # natural_logarithm

# 验证一下
print('自然常数e    %s' % math.e)
print('自然常数e的 na_log 次方，是不是等于10？验证通过')
print(math.pow(math.e, na_log))  # 10


print(math.pow(math.e, 0))
