# 三次样条插值
import numpy as np
from matplotlib import pyplot as plt

''' 
定义插值函数为: S_i(x_i) = y_i + b_i(x - x_i) + c_i(x - x_i)^2 + d_i(x - x_i)^3
'''


def function(x):
    return x * np.sin(2 * np.pi * x + 1)


#  输入需要插值的点
num_point = eval(input('请输入插值点的个数：'))
x_1 = np.linspace(-1, 1, num_point)  # 插值点的横坐标
y_1 = function(x_1)
ls = [(x, y) for x, y in zip(x_1, y_1)]
delta = np.zeros(len(ls) - 1)
Delta = np.zeros(len(ls) - 1)

for i in range(len(ls) - 1):
    delta[i] = ls[i + 1][0] - ls[i][0]
    Delta[i] = ls[i + 1][1] - ls[i][1]

A = np.zeros([len(ls), len(ls)])
B = np.zeros(len(ls))

# n个方程求解n个未知变量c_i

# 列出系数矩阵A

for i in range(len(ls)):
    if i == 0:
        A[i][0] = 1
        continue
    if i == len(ls) - 1:
        A[i][i] = 1
        continue
    A[i][i - 1] = delta[i - 1]
    A[i][i] = 2 * (delta[i - 1] + delta[i])
    A[i][i + 1] = delta[i]

# 常数矩阵B

for i in range(len(ls)):
    if i == 0:
        B[i] = 0
        continue
    if i == len(ls) - 1:
        B[i] = 0
        continue
    B[i] = 3 * (Delta[i] / delta[i] - Delta[i - 1] / delta[i - 1])

# 求解线性方程组，得到系数c_i
c = np.linalg.solve(A, B)

b = np.zeros(len(ls))
d = np.zeros(len(ls))

# 求解b_i,d_i
for i in range(len(ls) - 1):
    b[i] = Delta[i] / delta[i] - delta[i] / 3 * (2 * c[i] + c[i + 1])
    d[i] = (c[i + 1] - c[i]) / (3 * delta[i])

# 绘制散点图
plt.scatter(x_1, y_1, color='blue')
for i in range(len(ls) - 1):
    x = np.linspace(x_1[i], x_1[i + 1], 100)
    y = y_1[i] + b[i] * (x - x_1[i]) + c[i] * (x - x_1[i]) ** 2 + d[i] * (x - x_1[i]) ** 3
    plt.plot(x, y, color='green')

# 绘制真实的函数图像
x = np.linspace(-1, 1, 10000)
y = function(x)
plt.plot(x, y, color='red', linestyle=':')
plt.show()
