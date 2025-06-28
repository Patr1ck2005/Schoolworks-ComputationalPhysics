import numpy as np
from matplotlib import pyplot as plt


def function(x):
    return 1 / (1 + x ** 2)


b = 1  # upper_limit
a = 0  # lower_limit
exact = np.pi / 4
epsilon = 10 ** (-16)

'''
trapezoids:
'''


def trapezoid(n):
    h = (b - a) / n
    sum_trapezoid = h / 2 * (function(a) + function(b))
    for i in range(1, n):
        sum_trapezoid = sum_trapezoid + h * function(a + i * h)
    error_rate_tra = abs(sum_trapezoid - exact) / (exact + 10 ** (-15))
    return error_rate_tra, sum_trapezoid, h


# 建立空列表
log_h = []
log_error = []

for i in range(20):
    n = 3 ** (i + 1)
    error_rate_tra, sum_trapezoid, h = trapezoid(n)
    error_rate_tra = error_rate_tra + 10 ** (-15)
    log_h.append(np.log10(h))
    log_error.append(np.log10(error_rate_tra))
    print('N=', i + 1, 'n=', n, 'Integration=', sum_trapezoid, 'Fractional error=', error_rate_tra)
plt.scatter(log_h, log_error)
plt.ylabel('Log10(Error)')
plt.xlabel('Log10(h)')
plt.title('Trapezoid error')
plt.savefig('./src/Problem3.1.eps', dpi=600)
