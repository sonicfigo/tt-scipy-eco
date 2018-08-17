# coding=utf-8
"""
reshape 会生成一个新对象，拥有了自己的shape，
但data是共享源头，源对象和reshape对象，任一改变，都会影响对方。
"""

import numpy as np

a = np.floor(10 * np.random.random((3, 4)))
print(a)
assert a.flags.owndata is True

print("""
reshape 生成一个新对象，有自己的shape，但data 与 源对象共享""")
a_reshape = a.reshape(2, 6)
print(a_reshape)
assert a is not a_reshape
assert a_reshape.flags.owndata is False

print("""
改变源对象a 的 data""")
a[0][0] = 999
print(a)
print(a_reshape)

print("""
改变新对象a_reshape 的 data""")
a_reshape[0][1] = 888
print(a)
print(a_reshape)

assert np.may_share_memory(a, a_reshape)
