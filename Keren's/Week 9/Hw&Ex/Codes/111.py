import numpy as np
from matplotlib import pyplot as plt


def function(x):
    return 1 / (1 + x ** 2)


b = 1  # upper_limit
a = 0  # lower_limit
exact = np.pi / 4


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

for i in range(20):
    n = 2 * (i + 1)
    error_rate_sim, sum_simpson, h = simpson(n)
    log_h.append(np.log10(h))
    log_error.append(np.log10(error_rate_sim))
    print('N=', i + 1, 'n=', n, 'Integration=', sum_simpson, 'Fractional error=', error_rate_sim)

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
