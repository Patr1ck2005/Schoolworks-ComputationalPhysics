import numpy as np
from matplotlib import pyplot as plt


def function(x):
    return 1 / (1 + x ** 2)


b = 1  # upper_limit
a = 0  # lower_limit
exact = np.pi / 4
epsilon = 10 ** (-16)


def simpson(n):
    h = (b - a) / n
    sum_simpson = h / 6 * (function(a) + function(b))
    for i in range(0, n):
        sum_simpson = sum_simpson + 2 / 3 * h * function(a + (1 / 2 + i) * h)
    for j in range(1, n):
        sum_simpson = sum_simpson + 1 / 3 * h * function(a + j * h)
    error_simpson_rate = abs(sum_simpson - exact) / exact
    return error_simpson_rate, sum_simpson, h


# 建立空列表
log_h = []
log_error = []

for i in range(200):
    n = 2 * (i + 1)
    error_rate_sim, sum_simpson, h = simpson(n)
    log_h.append(np.log10(h))
    log_error.append(np.log10(error_rate_sim))
    print('N=', i + 1, 'n=', n, 'Integration=', sum_simpson, 'Fractional error=', error_rate_sim)

plt.scatter(log_h, log_error,s=5)
plt.ylabel('Log10(Error)')
plt.xlabel('Log10(h)')
plt.title('Simpson error')
plt.savefig('./src/Problem3.2.eps', dpi=600)
# plt.show()


