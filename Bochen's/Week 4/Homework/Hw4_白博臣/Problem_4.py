import numpy as np


def cal(n):
    a_0 = 2
    for i in range(3, n + 1):
        a_n = 2 ** (i - 1 - 1 / 2) * np.sqrt(1 - np.sqrt(1 - 4 ** (1 - (i - 1)) * a_0 ** 2))
        a_0 = a_n
    return a_0


for i in range(2, 51):
    print('n=', i, cal(i))
