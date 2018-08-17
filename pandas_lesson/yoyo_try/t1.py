# coding=utf-8
"""
scikit learn 的 digits.target 是一维的，要改成二维的，匹配tf的shape(n_sample,10)
"""
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits

digits = load_digits()

digits_X = digits.data
digits_y = digits.target
digits_images = digits.images


def convert_target2d():
    target2d = np.zeros((1797, 10))
    # print(target2d.shape)

    for num, matrix_row in zip(digits_y, target2d):
        matrix_row[num] = 1
    # print(zip(digits_y[:20], target2d[:20]))
    return target2d


print(type(digits_y))  # <type 'numpy.ndarray'>
print(digits_y.shape)  # (1797,)
print(digits_y[0])

X_train, X_test, y_train, y_test, img_train, img_test = train_test_split(digits_X,
                                                                         convert_target2d(),
                                                                         digits.images,
                                                                         test_size=0.4)
print(type(y_train))  # <type 'numpy.ndarray'>
print(y_train.shape)  # (1797,)
print(y_train[0])
