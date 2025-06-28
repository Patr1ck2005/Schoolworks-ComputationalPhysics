# 自适应梯形算法
import numpy as np

b = 1  # upper_limit
a = 0  # lower_limit
exact = np.pi / 4
epsilon = 10 ** (-16)


def function(x):
    return np.sin(np.sqrt(100 * x)) * np.sin(np.sqrt(100 * x))


def trapezoid(a, b):
    h = (b - a)
    sum_trapezoid = h / 2 * (function(a) + function(b))
    return sum_trapezoid


def adaptive_trapezoid(a, b, eps):
    c = (a + b) / 2
    sum_full = trapezoid(a, b)
    sum_half = trapezoid(a, c) + trapezoid(c, b)

    if abs(sum_full - sum_half) < eps:
        return sum_half

    left_sum = adaptive_trapezoid(a, c, eps / 2)
    right_sum = adaptive_trapezoid(c, b, eps / 2)

    return left_sum + right_sum


