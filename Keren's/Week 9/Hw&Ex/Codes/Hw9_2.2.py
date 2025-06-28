import numpy as np

def function(x):
    return np.sin(np.sqrt(100 * x)) * np.sin(np.sqrt(100 * x))

exact = 0.4558325323090851

def simpson(n, a, b):
    h = (b - a) / n
    sum_simpson = h / 6 * (function(a) + function(b))
    for i in range(0, n):
        sum_simpson = sum_simpson + 2 / 3 * h * function(a + (1 / 2 + i) * h)
    for j in range(1, n):
        sum_simpson = sum_simpson + 1 / 3 * h * function(a + j * h)
    return sum_simpson

def adaptive_simpson_rule(f, a, b, eps):
    n = 1
    integral_old = simpson(n, a, b)
    n *= 2
    integral_new = simpson(n, a, b)

    data = {'Number of Intervals': [n/2], 'Integral Estimate': [integral_new], 'Error Estimate': [abs(integral_new - 0.4558325323090851)]}

    while abs(integral_new - integral_old) >= eps:
        integral_old = integral_new
        n *= 2
        integral_new = simpson(n, a, b)
        data['Number of Intervals'].append(n/2)
        data['Integral Estimate'].append(integral_new)
        data['Error Estimate'].append(abs(integral_new - 0.4558325323090851))
        print("切片数:", n)
        print("积分估计值:", integral_new)
        print("积分误差估计:", abs(integral_new - 0.4558325323090851))

    return integral_new, n, data

a = 0
b = 1
epsilon = 10 ** (-10)
approx_integral, num_intervals, results = adaptive_simpson_rule(function, a, b, epsilon)

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(results)

plt.figure(figsize=(10, 6))
table = plt.table(cellText=df.values,
                  colLabels=df.columns,
                  cellLoc='center',
                  loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.25, 1.4)
plt.axis('off')
plt.title('Adaptive Simpson Rule Results', fontsize=14)
plt.savefig('./src/Problem2.2.eps', dpi=600)
