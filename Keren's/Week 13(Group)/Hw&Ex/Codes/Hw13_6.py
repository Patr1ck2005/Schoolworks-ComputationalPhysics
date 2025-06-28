import random
import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', family='Times New Roman')

# 定义阶乘函数
def gamma(x):
    if x > 1:
        return (x - 1) * gamma(x - 1)
    if x == 1:
        return 1
    if x == 0.5:
        return np.sqrt(np.pi)

# 定义被积函数
def func(x):
    return 1

Value = []  # 存储MC方法计算的N维球体积
Exact = []  # 存储递推公式计算的N维球体积

Dim = 24  # 维度上限
D = np.arange(1, Dim + 1)

# 计算N维球体真实值
for dim in range(1, Dim + 1):
    Exact.append(np.pi**(dim / 2) / gamma(dim / 2 + 1))
Exact = np.array(Exact)

print('Exact:', Exact)

# 使用MC方法计算N维球体积
N = 100000  # 随机点个数
for dim in range(1, Dim + 1):
    hnit = 0  # 每个维度重新初始化击中点数
    for j in range(N):
        X = np.random.rand(dim)  # 生成N维随机点
        R = np.linalg.norm(X)  # 计算N维矢量X的模长
        if R <= 1:
            hnit += 1
    Value.append(2**dim * hnit / N)

print('MC_Value:', Value)

# 计算误差
Error_r = np.abs(Value - Exact) / Exact
Error_a = np.abs(Value - Exact)

# 绘制误差图
plt.figure()
plt.xlabel('Dimension')
plt.ylabel('Error')
plt.plot(D, Error_a, 'o:', color='red', label='Absolute Error')
plt.plot(D, Error_r, 'o:', color='darkblue', label='Relative Error')
plt.title('Absolute Error of MC Method')
plt.legend()

# 绘制体积图
plt.figure()
plt.xlabel('Dimension')
plt.ylabel('Volume')
plt.plot(D, Exact, 'o:', color='blue', label='Exact')
plt.plot(D, Value, 'o:', color='green', label='Calculated')
plt.title('Volume of Hypersphere by MC Method')
plt.legend()
plt.show()
