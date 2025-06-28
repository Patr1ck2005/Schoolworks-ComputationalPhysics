import matplotlib.pyplot as plt
import numpy as np


# 设置函数f(x)=sin(x)
def f(x):
    return np.sin(x)


# 设置求解导数的公式
def derivative_f(x, delta):
    return (f(x + delta) - f(x)) / delta


# 设置导数函数 f'(x)=cos(x)
def real_df(x):
    return np.cos(x)


# 设置h
log_h = np.linspace(0, -20, 200)
h = 10 ** log_h

# 机器精度
c = 6 * 10 ** -16


# 计算截断误差
def e_tru(h, x):
    return h * f(x) / 2


# 计算舍入误差
def e_rou(h, x):
    return c * 2 * f(x) / h


# 计算总误差
def g(h, x):
    return e_rou(h, x) + e_tru(h, x)


# 计算h的最佳取值
def h_best(x):
    return np.sqrt(4 * c)


# 计算各种误差
e_truncation = e_tru(h, 0.5)
e_roundoff = e_rou(h, 0.5)
e = g(h, 0.5)

# 绘制图像与输出结果
plt.figure()
plt.plot(log_h, np.log10(e_truncation), label='truncation error')
plt.plot(log_h, np.log10(e_roundoff), label='round-off error')
plt.plot(log_h, np.log10(e), label='total error')
plt.xlabel('log10(h)')
plt.legend()
plt.show()

# 计算并输出h_best
print('h的最佳取值为：', '\n', h_best(0.5))
