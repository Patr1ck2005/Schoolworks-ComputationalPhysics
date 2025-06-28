import numpy as np
from matplotlib import pyplot as plt

b = 1  # upper_limit
a = 0  # lower_limit
exact = np.pi / 4
Integration = np.zeros((25, 25))
H = []
Error = []
np.set_printoptions(precision=16)  # 设置输出精度为16位小数


def function(x):
    return 1 / (1 + x ** 2)


def d(x):
    return -2 * x / ((1 + x * x) ** 2)


def trapezoid(n):
    h = (b - a) / n
    sum_trapezoid = h / 2 * (function(a) + function(b))
    for i in range(1, n):
        sum_trapezoid = sum_trapezoid + h * function(a + i * h)
    error_rate_tra = abs(sum_trapezoid - exact) / exact
    return sum_trapezoid


for i in range(1, 26):
    k = 2
    Integration[i - 1][0] = trapezoid(2 ** (i - 1))
    if i == 1:
        continue
    while k <= i:
        Integration[i - 1][k - 1] = Integration[i - 1][k - 2] + (
                Integration[i - 1][k - 2] - Integration[i - 2][k - 2]) / (4.0 ** (k - 1.0) - 1.0)
        k += 1
    error = abs(Integration[i - 1][i - 1] - exact)
    H.append(np.log10(1 / (2 ** (i - 1))))
    Error.append(np.log10(error))
    print('n=', i, 'error=', error)
plt.scatter(H, Error)
plt.xlabel('Log10(h)')
plt.ylabel('Log10(error)')
plt.title('Romberg Integration Error')
plt.savefig('./src/Problem3.3.eps', dpi=600)
