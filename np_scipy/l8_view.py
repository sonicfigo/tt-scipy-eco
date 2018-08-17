# coding=utf-8
"""
浅复制有：view 和 slice

view 是共享 data， 但拥有自己的shape。

与reshape的区别：
reshape会变形为一个不同shape的对象外，
view 也可以变形，但默认view出来的，是同样shape的，所以理解为：想要一份同shape的数据时，使用view

"""

import numpy as np

a = np.arange(12)
a.shape = 2, 6
assert a.flags.owndata is True
print(a)

print("""
view自己不拥有数据，只是指向a的数据指针""")
a_view = a.view()
assert a_view is not a  # 新的对象
assert a_view.base is a  # 新的对象的base，是a
assert a_view.flags.owndata is False
print(a_view)

print("""
a 改变，影响view""")
a[0][0] = 11
print(a)
print(a_view)

print("""
view 改变shape，不影响a的shape""")
a_view.shape = 3, 4
print(a)
print(a_view)

assert np.may_share_memory(a, a_view)

"""
切片也是返回一个a的view
"""
a_slice = a[:, 1:3]  # 每一行的 索引1，2列
print(a_slice)
a_slice[:] = 666  # 2*2的所有item，都为666
print(a)
