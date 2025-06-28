import numpy as np
import matplotlib.pyplot as plt
import random


# 定义积分函数
def func(x):
    return 2 / (1 + x)


# 精确积分值（假设我们知道精确积分值为2 * np.log(2)）
exact_integral_value = 2 * np.log(2)

# 存储误差绝对值
errors = []

# 随机数个数的范围
Log_N_values = np.linspace(2, 6, 100)  # 生成100到10000之间的100个数
# print(N_values)
N_values = 10 ** Log_N_values

for N in N_values:
    N = int(np.round(N))
    X = []
    Y = []
    O = []
    Value = []
    Error = []
    for k in range(10):
        for j in range(N):
            X.append(random.random())
            O.append(0)
            # 生成因变量矩阵
            # 生成自变量矩阵
        for j in range(N):
            Y.append(func(X[j]))
        Mean = np.average(Y)
        v = Mean
        Value.append(v)
        Error.append(np.abs(v - 2 * np.log(2)))
    v = np.mean(Value)
    errors.append(np.mean(Error))
    print("value:", v, "error:", np.mean(Error))

# 绘制误差随随机数个数变化的图表
plt.figure(figsize=(10, 6))
plt.scatter(np.log10(N_values), np.log10(errors), s=3, label='Error vs N')
plt.plot(np.linspace(2, 6, 100), -0.5 * np.linspace(2, 6, 100) - 0.5)
plt.title("Monte Carlo Integration Error")
plt.xlabel("Number of Random Points (N)")
plt.ylabel("Absolute Error")
plt.legend()
plt.grid(True)
plt.show()
