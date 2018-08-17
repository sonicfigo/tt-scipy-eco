# coding=utf-8
"""
semilogx，半对数坐标

半对数坐标系一个轴是分度均匀的普通坐标轴，另一个轴是分度不均匀的对数坐标轴。

该图中的横坐标轴（x轴）是对数坐标。
在此轴上，某点与原点的实际距离为该点对应数的对数值，但是在该点标出的值是真数。


"""
import matplotlib.pyplot as plt
import numpy as np

plt.figure(1, figsize=(10, 6))


# C_s = np.logspace(start=-110, stop=10, num=10)  # base=-10， 既10的负10次方 ~ 10的0次方，均分10个
# c_score_means = [0.15552937214547155, 0.15552937214547155, 0.15552937214547155,
#                  0.15552937214547155, 0.15552937214547155, 0.90260270247335728,
#                  0.9482070815179453, 0.94490714734074643, 0.94379972762867548,
#                  0.94379972762867548]
#
# plt.semilogx(C_s, c_score_means)


def plot_origin():
    """
    阅读真数，底数，指数 知识：  np_base/np_logspace.py

    图形解释：
        以e为底，x轴的对应的对数，是y轴（既是 np.log(x) ）

    直观感受：
        y小小的变动，x轴就变动很大

    """
    x = range(10, 1000)  # 真数
    y = np.log(x)  # 以 e 对底，x的对数，是y

    plt.plot(x, y)  # 原始的 对数函数图形（可以看到，是非线性的）
    plt.xlabel('0 ~ 999 real')
    plt.ylabel("0 ~ 999's Natural Logrithm")


def plot_semilogx():
    x = range(10, 1000)  # 真数
    y = np.log(x)  # 以 e 对底，x的对数，是y

    """
    对 x 轴特殊处理，图形解释：
    x轴：
    - 文本"标值"
        真数，既是x，10 ~ 1000
        
    - 真实"刻度"(与原点的距离)
        对数值（以自然数E为底，"标值"为真数，对应的对数值）
        如第二个点，X轴 "标值" 大约=20，对应的y既是 y=logE20(以E为底，20的对数，值为3) ，既刻度=3
    """
    plt.semilogx(x, y)  # 不是把原始的x，而是原x轴的对数刻度，所以与y轴就是线性关系了


# plot_origin()
plot_semilogx()
plt.show()
