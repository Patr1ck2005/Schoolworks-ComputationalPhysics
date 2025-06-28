import matplotlib.pyplot as plt
import numpy as np
import random


def fun(x):
    return np.exp(x)


Value = []
Ty = []
Tx = []
Tx2 = []
Ty2 = []
Value2 = []

n = 10000
for i in range(n):
    X = []
    Y = []
    N = 1000
    for i in range(N):
        X.append(random.random())
    for j in range(N):
        Y.append(fun(X[j]))
    Mean = np.mean(Y)
    v = (Mean)
    Value.append(v)
print('值矩阵：', Value)
print('值矩阵长度：', len(Value))
Value = np.array(Value)

for i in range(100):
    temp1 = len(np.where(Value > 1.62 + 0.002 * i)[0])
    temp2 = len(np.where(Value > 1.62 + 0.002 * (i + 1))[0])
    Ty.append((temp1 - temp2) / n)
print('分布：', Ty)

for i in range(100):
    x = 0.5 * (1.62 + 0.002 * (i) + 1.62 + 0.002 * (i + 1))
    Tx.append(x)
print('where', Tx)

X_l = np.linspace(1.62, 1.82, 100)
sigma = 0.491 / np.sqrt(1000)
mean = np.exp(1) - 1
Y_l = 0.002 / (np.sqrt(2 * np.pi) * sigma) * np.exp(-(X_l - mean) ** 2 / (2 * sigma ** 2))

n = 10000  # 获得n个积分值
# 重复进行n次，每次N采样

for i in range(n):
    X = []
    Y = []
    N = 1000  # 在x轴上随机撒N个点
    # 生成自变量矩阵
    for j in range(N):
        X.append(random.random())
    # 生成因变量矩阵
    for j in range(N):
        Y.append(fun(X[j]))
    # 计算平均值
    Mean = np.average(Y)
    v = Mean
    Value2.append(v)
print(Value2)
print(len(Value2))
Value2 = np.array(Value2)


plt.plot(Tx, Ty, color='g', label='10000 I calcs')
plt.plot(X_l, Y_l, 'blue', linestyle='--', linewidth=2, label='Limiting Normal Distribution')
plt.plot(Tx2, Ty2, '*:', color='r', label='100000 I calcs')
plt.xlim(1.62, 1.82)
plt.legend()
plt.ylabel('Probability')
plt.xlabel('MC estimate of Integral')
plt.show()
