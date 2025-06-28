# 二次样条插值
import numpy as np
from matplotlib import pyplot as plt

''' 
定义插值函数为: S_i(x_i) = y_i + b_i(x - x_i) + c_i(x - x_i)^2 + d_i(x - x_i)^3
'''
ls = [(0, 0), (10, 227.04), (15, 362.78), (20, 517.35), (22.5, 602.97), (30, 901.67)]
x_1 = [tuple_[0] for tuple_ in ls]  # 插值点的横坐标
y_1 = [tuple_[1] for tuple_ in ls]  # 插值点的纵坐标

#  输入需要插值的点
ls = [(x, y) for x, y in zip(x_1, y_1)]
delta = np.zeros(len(ls) - 1)
Delta = np.zeros(len(ls) - 1)

for i in range(len(ls) - 1):
    delta[i] = ls[i + 1][0] - ls[i][0]
    Delta[i] = ls[i + 1][1] - ls[i][1]

A = np.zeros([len(ls) - 1, len(ls) - 1])
B = np.zeros(len(ls) - 1)

# n个方程求解n个未知变量c_i

# 列出系数矩阵A

for i in range(len(ls) - 1):
    if i == 0:
        A[i][0] = 1
        continue
    if i == len(ls) - 1:
        A[i][i] = 1
        continue
    A[i][i - 1] = 1
    A[i][i] = 1

# 常数矩阵B

for i in range(len(ls) - 1):
    if i == 0:
        B[i] = Delta[i] / delta[i]
        continue
    if i == len(ls) - 2:
        B[i] = 2 * Delta[i] / delta[i]
    B[i] = 2 * Delta[i - 1] / delta[i - 1]

# 求解线性方程组，得到系数c_i
b = np.linalg.solve(A, B)

c = np.zeros(len(ls) - 1)

# 求解b_i,d_i
for i in range(len(ls) - 2):
    if i == len(ls) - 2:
        c[i] = -b[i] / (2 * delta[i])
    c[i] = (b[i + 1] - b[i]) / (2 * delta[i])

y_values = []
# 绘制散点图
for i in range(len(ls) - 1):
    plt.scatter(x_1[i], y_1[i], color='red')
    x = np.linspace(x_1[i], x_1[i + 1], 100)
    y = y_1[i] + b[i] * (x - x_1[i]) + c[i] * (x - x_1[i]) ** 2
    y_values.extend(y)  # 将当前区间的y值添加到一维数组中
    plt.plot(x, y, color='blue')

plt.show()


def function(x):
    return 362.78 + b[2] * (x - 15) + c[2] * (x - 15) ** 2


print(b)
print(c)

print(function(16))
