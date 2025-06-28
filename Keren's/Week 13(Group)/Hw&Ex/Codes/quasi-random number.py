import numpy as np
import matplotlib.pyplot as plt
import random


def halton_seq(index, base):
    result = 0.0
    fractional = 1.0 / base
    i = index
    while i > 0:
        result += fractional * (i % base)
        i //= base
        fractional /= base
    return result


def generate_halton_points(num_points, dimensions, bases):
    points = np.zeros((num_points, dimensions))
    for i in range(num_points):
        for j in range(dimensions):
            points[i][j] = halton_seq(i + 1, bases[j])
    return points


def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


# 选择一些质数作为基数，这里生成了足够多的素数
bases = generate_primes(10)  # 可以根据需要生成更多素数

# 现在可以生成任意数量的Halton点
num_points = 10000000  # 例如，生成100个点
dimensions = 1  # 例如，生成3维的Halton序列

halton_points = generate_halton_points(num_points, dimensions, bases)
Halton_points_List = []
for i in range(len(halton_points)):
    Halton_points_List.append(halton_points[i][0])


# 定义积分函数
def func(x):
    return 2 / (1 + x)


# 精确积分值（假设我们知道精确积分值为2 * np.log(2)）
exact_integral_value = 2 * np.log(2)

# 存储误差绝对值
errors = []

# 随机数个数的范围
Log_N_values = np.linspace(2, 7, 100)  # 生成100到10000之间的100个数
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
            X.append(Halton_points_List[j])
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
plt.plot(np.linspace(2, 5, 100), -0.5 * np.linspace(2, 5, 100))
plt.plot(np.linspace(2, 5, 100), -2 / 3 * np.linspace(2, 5, 100) - 1)
plt.plot(np.linspace(2, 5, 100), -1 * np.linspace(2, 5, 100))
plt.title("Monte Carlo Integration Error")
plt.xlabel("Number of Random Points (N)")
plt.ylabel("Absolute Error")
plt.legend()
plt.grid(True)
plt.show()
