import numpy as np


def secant_method(f, a, b, tol=1e-6, max_iter=100):
    """

    :param f: 所需求解的函数
    :param a: a是指的p_(n-1)
    :param b: b是指的p_(n) c指的是p_(n+1)
    :param tol: 最小精度
    :param max_iter:最大迭代次数
    :return:
    """
    iter = 0
    while abs(b - a) > tol and iter < max_iter:
        c = b - f(b) * (b - a) / (f(b) - f(a))
        a, b = b, c
        iter += 1

    return c


# 定义要求解根的函数
def f(x):
    return 2 - x - np.exp(-x)


# 设置初始猜测值 a 和 b
a = -2
b = 0

root_1 = secant_method(f, a, b)

a = 0
b = 3
root_2 = secant_method(f, a, b)
print(f"Root found at x = 第一个根：{root_1},第二个根：{root_2}")
