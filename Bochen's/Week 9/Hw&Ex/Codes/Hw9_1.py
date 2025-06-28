import matplotlib.pyplot as plt
import numpy as np


def function_1(t):
    return 9 * 10 ** (-3) * 6.022 * 10 ** 28 * 1.380649 * 10 ** (-23) * (t / 428) ** 3


def integration(t):
    def function(x):
        return x ** 4 * np.exp(x) / ((np.exp(x) - 1) ** 2 + np.spacing(1))

    b = 428 / t
    a = 0

    def simpson(n):
        h = (b - a) / n
        sum_simpson = h / 6 * (function(a) + function(b))
        for i in range(0, n):
            sum_simpson = sum_simpson + 2 / 3 * h * function(a + (1 / 2 + i) * h)
        for j in range(1, n):
            sum_simpson = sum_simpson + 1 / 3 * h * function(a + j * h)
        return sum_simpson, h

    sum_simpson, h = simpson(50)
    return sum_simpson


t = np.arange(5, 501)
Simpson = []
for i in t:
    Simpson.append(integration(i) * function_1(i))

plt.scatter(t, Simpson)
plt.title('Function Cv-T')
plt.xlabel('T')
plt.ylabel('Cv')
plt.savefig('Problem1.eps', dpi=600)
