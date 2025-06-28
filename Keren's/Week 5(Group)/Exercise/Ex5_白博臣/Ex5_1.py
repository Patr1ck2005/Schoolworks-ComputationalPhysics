import numpy as np


def f(x):
    return 2 - x - np.exp(-x)


def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None

    iter = 0
    while (b - a) / 2 > tol and iter < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iter += 1

    return c


# 设置初始区间[a, b]
a = -2
b = 0
root_1 = bisection_method(f, a, b)
a = 1
b = 3
root_2 = bisection_method(f, a, b)
if root_1 is not None:
    print(f"Root found at x = 第一个根：{root_1},第二个根：{root_2}")
