import numpy as np
from matplotlib import pyplot as plt


def function(x):
    return 1 / (1 + x ** 2)


def calculate_sum(x, batch_size):
    sum_total = 0
    start_index = 0
    while start_index < len(x):
        end_index = min(start_index + batch_size, len(x))
        batch_x = x[start_index:end_index]
        s0 = (function(batch_x + i) + function(batch_x)) * i / 2
        sum_total += np.sum(s0)
        start_index = end_index
    return sum_total


error_ls = []

n_ls_log = np.linspace(-2, -9, 8)
n_ls_log_1 = np.linspace(-9, -9.5, 4)
n_ls_1 = 10 ** n_ls_log_1
n_ls = 10 ** n_ls_log
n_ls = np.concatenate((n_ls, n_ls_1))

batch_size = 1000  # 设置分批处理的批次大小

for i in n_ls:
    x = np.arange(0, 1, i)  # 使用向量化的方式生成 x 的取值
    sum_total = calculate_sum(x, batch_size)
    error = abs(np.pi / 4 - sum_total)
    print(error)
    error_ls.append(error)

error_ls_log = np.log10(error_ls)
plt.scatter(n_ls_log, error_ls_log)
plt.xlabel('log(n)')
plt.ylabel('log(Error)')
plt.title('Error vs. log(n)')
plt.show()
