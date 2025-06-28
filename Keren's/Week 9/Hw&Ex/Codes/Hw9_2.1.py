import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def function(x):
    return np.sin(np.sqrt(100 * x)) * np.sin(np.sqrt(100 * x))

def trapezoid_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    sum_trapezoid = h * (np.sum(y) - 0.5 * (y[0] + y[n]))
    return sum_trapezoid

def adaptive_trapezoid_rule(f, a, b, eps):
    n = 1
    integral_old = trapezoid_rule(f, a, b, n)
    n *= 2
    integral_new = trapezoid_rule(f, a, b, n)

    data = {'Number of Intervals': [n/2], 'Integral Estimate': [integral_new], 'Error Estimate': [abs(integral_new - 0.4558325323090851)]}

    while abs(integral_new - integral_old) >= eps:
        integral_old = integral_new
        n *= 2
        integral_new = trapezoid_rule(f, a, b, n)
        data['Number of Intervals'].append(n/2)
        data['Integral Estimate'].append(integral_new)
        data['Error Estimate'].append(abs(integral_new - 0.4558325323090851))

    df = pd.DataFrame(data)
    return df

a = 0
b = 1
epsilon = 10 ** (-10)
exact_integral = 0.4558325323090851
results = adaptive_trapezoid_rule(function, a, b, epsilon)

plt.figure(figsize=(10, 6))
table = plt.table(cellText=results.values,
                  colLabels=results.columns,
                  cellLoc='center',
                  loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.25, 1.4)
plt.axis('off')
plt.title('Adaptive Trapezoid Rule Results', fontsize=14)
plt.savefig('./src/Problem2.1.eps', dpi=600)
