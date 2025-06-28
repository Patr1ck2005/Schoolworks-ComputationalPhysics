import numpy as np
import matplotlib.pyplot as plt
import subprocess


# 定义积分函数
def func(x):
    return 2 / (1 + x)


# 精确积分值（假设我们知道精确积分值为2 * np.log(2)）
exact_integral_value = 2 * np.log(2)

# 存储误差绝对值
errors = []

# 随机数个数的范围
Log_N_values = np.linspace(2, 4, 100)  # 生成100到10000之间的100个数
# print(N_values)
N_values = 10 ** Log_N_values

for N in N_values:
    N = int(np.round(N))
    X = []
    Y = []
    O = []
    Value = []
    Error = []

    subprocess.run(['./untitled'], capture_output=True, text=True)
    # 等待C++程序执行完成，确保文件写入完成
    # 这里可能需要一些时间延迟，例如time.sleep(1)

    # 打开文件并读取第一次生成的随机数作为X值
    with open('random_numbers.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    Rdrand = [float(line.strip()) for line in lines]  # 将读取的字符串转换为浮点数

    # 清空文件
    open('random_numbers.txt', 'w').close()
    for j in range(N):
        X.append(Rdrand[j])
        O.append(0)
        # 生成因变量矩阵
        # 生成自变量矩阵
    for j in range(N):
        Y.append(func(X[j]))
    v = np.average(Y)
    Error.append(np.abs(v - 2 * np.log(2)))
    errors.append(Error)
    print("value:", v, "error:", Error)

# 绘制误差随随机数个数变化的图表
plt.figure(figsize=(10, 6))
plt.scatter(np.log10(N_values), np.log10(errors), s=3, label='Error vs N')
plt.plot(np.linspace(2, 4, 100), -0.5 * np.linspace(2, 4, 100))
plt.plot(np.linspace(2, 4, 100), -2 / 3 * np.linspace(2, 4, 100))
plt.plot(np.linspace(2, 4, 100), -1 * np.linspace(2, 4, 100))
plt.title("Monte Carlo Integration Error")
plt.xlabel("Number of Random Points (N)")
plt.ylabel("Absolute Error")
plt.legend()
plt.grid(True)
plt.show()
