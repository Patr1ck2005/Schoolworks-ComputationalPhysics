import numpy as np
from decimal import Decimal, getcontext
from matplotlib import pyplot as plt

getcontext().prec = 17  # 设置精度


def function(x):
    return Decimal(1) / (Decimal(1) + x ** 2)


def d(x):
    return Decimal(-2) * x / ((Decimal(1) + x * x) ** 2)


def trapezoid(n):
    h = (b - a) / n
    sum_trapezoid = h / 2 * (function(a) + function(b))
    for i in range(1, n):
        sum_trapezoid = sum_trapezoid + h * function(a + i * h)
    error_rate_tra = abs(sum_trapezoid - exact) / (exact + Decimal('1e-15'))
    return sum_trapezoid


b = Decimal(1)  # upper_limit
a = Decimal(0)  # lower_limit
exact = Decimal(np.pi) / Decimal(4)
epsilon = Decimal('1e-16')
Error = []
H = []
Integration = np.zeros((10, 10), dtype=object)  # 指定dtype为object

for i in range(1, 11):
    k = 2
    H.append(1 / (2 ** (i - 1)))
    Integration[i - 1][0] = trapezoid(2 ** (i - 1))
    if i == 1:
        continue
    while k <= i:
        Integration[i - 1][k - 1] = Integration[i - 1][k - 2] + (
                Integration[i - 1][k - 2] - Integration[i - 2][k - 2]) / (
                                            Decimal('4') ** (k - Decimal('1')) - Decimal('1'))
        k += 1
    error = abs(Integration[i - 1][i - 1] - exact)
    Error.append(error)

plt.scatter(H, Error)
plt.show()
