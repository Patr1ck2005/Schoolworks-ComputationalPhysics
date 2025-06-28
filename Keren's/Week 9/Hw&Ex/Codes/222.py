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

for i in range(10):
    n = 3 ** (i + 1)
    error_rate_tra, sum_trapezoid, h = trapezoid(n)
    error_rate_tra = error_rate_tra + 10 ** (-15)
    log_h.append(np.log10(h))
    log_error.append(np.log10(error_rate_tra))
    print('N=', i + 1, 'n=', n, 'Integration=', sum_trapezoid, 'Fractional error=', error_rate_tra)

# 线性插值拟合
coefficients = np.polyfit(log_h, log_error, deg=1)
slope = coefficients[0]  # 取负数作为斜率

# 输出斜率
print("斜率为：", slope)

# 绘制散点图和拟合曲线
plt.scatter(log_h, log_error)
x_fit = np.linspace(min(log_h), max(log_h), 100)
y_fit = np.polyval(coefficients, x_fit)
plt.plot(x_fit, y_fit, 'r', label='Fit')
plt.legend()
plt.show()

print(log_h, log_error)
