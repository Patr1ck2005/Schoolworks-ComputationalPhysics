import numpy as np


def cal(n):
    a_0 = 1 / np.exp(1) * (np.exp(1) - 1)
    for i in range(1, n+1):
        a_n = 1 - (i) * a_0
        a_0 = a_n
    return a_n


# n = eval(input('n='))
# value = cal(n)
# print(value)
for i in range(2, 30):
    print('n=', i, cal(i))
