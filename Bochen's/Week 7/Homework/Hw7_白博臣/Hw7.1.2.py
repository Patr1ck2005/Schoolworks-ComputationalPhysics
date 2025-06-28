# 三次样条插值
import numpy as np
from matplotlib import pyplot as plt

''' 
定义插值函数为: S_i(x_i) = y_i + b_i(x - x_i) + c_i(x - x_i)^2 + d_i(x - x_i)^3
'''

#  输入需要插值的点
ls = [(-1.00, -14.58), (0.00, 0.00), (1.27, 0.00), (2.55, 0.00), (3.82, 0.00), (4.92, 0.88), (5.02, 11.17)]
x_1 = [tuple_[0] for tuple_ in ls]  # 插值点的横坐标
y_1 = [tuple_[1] for tuple_ in ls]  # 插值点的纵坐标
delta = np.zeros(len(ls) - 1)
Delta = np.zeros(len(ls) - 1)

for i in range(len(ls) - 1):
    delta[i] = ls[i + 1][0] - ls[i][0]
    Delta[i] = ls[i + 1][1] - ls[i][1]

v_1 = Delta[0] / delta[0]  # 固定第一个插值函数的一阶导
v_n = Delta[len(ls) - 2] / delta[len(ls) - 2]

A = np.zeros([len(ls), len(ls)])
B = np.zeros(len(ls))

# n个方程求解n个未知变量c_i

# 列出系数矩阵A

for i in range(len(ls)):
    if i == 0:
        A[i][0] = 2 * delta[i]
        A[i][1] = delta[i]
        continue
    if i == len(ls) - 1:
        A[i][i - 1] = delta[i - 1]
        A[i][i] = 2 * delta[i - 1]
        continue
    A[i][i - 1] = delta[i - 1]
    A[i][i] = 2 * (delta[i - 1] + delta[i])
    A[i][i + 1] = delta[i]

# 常数矩阵B

for i in range(len(ls)):
    if i == 0:
        B[i] = 3 * (Delta[i] / delta[i] - v_1)
        continue
    if i == len(ls) - 1:
        B[i] = 3 * (v_n - Delta[i - 1] / delta[i - 1])
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
plt.show()
