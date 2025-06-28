import numpy as np
from matplotlib import pyplot as plt


def function(x):
    return 1 / (1 + x ** 2)


'''
trapezoids:
'''

error_ls = []

n_ls_log = np.linspace(-2, -8, 100)
n_ls = 10 ** n_ls_log
for i in n_ls:
    x = 0
    s1 = 0
    while x <= 1:
        s0 = (function(x + i) + function(x)) * i / 2
        s1 += s0
        x = x + i
    error = abs(np.pi / 4 - s1)
    error_ls.append(error)
error_ls_log = np.log10(error_ls)
plt.scatter(n_ls_log, error_ls_log)
plt.show()
