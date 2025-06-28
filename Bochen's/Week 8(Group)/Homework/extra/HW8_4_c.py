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


# 设置g(h)=h*sin(0.5)/2+2c*sin(0.5)/h
def g(h, x):
    return h * f(x) / 2 + c * 2 * f(x) / h


# 设置h
log_h = np.linspace(0, -20, 200)
h = 10 ** log_h

# 机器精度
c = 6 * 10 ** -16

# 计算误差值
error = np.array([])
for i in range(len(h)):
    temp = abs(derivative_f(0.5, h[i]) - real_df(0.5))
    error = np.append(error, np.log10(temp))

# 绘制图像
plt.figure()
plt.plot(log_h, np.log10(g(h, 0.5)))
plt.scatter(log_h, error, s=5, color='red')
plt.show()

# 计算最佳的h，等价于g'(h)=0时的h的值
h0=np.sqrt(4*c)
print(h0)