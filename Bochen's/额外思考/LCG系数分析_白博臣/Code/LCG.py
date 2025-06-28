import matplotlib.pyplot as plt
import numpy as np


def linear_congruential_generator(X_0, a, c, m, n):
    """
    X0: 初始种子
    a: 乘数
    c: 增量
    m: 模数
    n: 生成随机数的数量
    """
    X = X_0
    results = []
    for n in range(n):
        X = (a * X + c) % m
        random_num = (X / m)
        results.append(random_num)
    return results


e = 2 ** 31 - 1
num = range(1, 3001)
mean_sample_1 = []
mean_sample_2 = []
mean_sample_3 = []
mean_sample_4 = []

for i in range(1, 3001):
    results = linear_congruential_generator(1, 16807, 1, e, i)
    mean_sample = np.mean(results)
    mean_sample_1.append(mean_sample)

# for i in range(1, 3001):
#     results = linear_congruential_generator(2, 13, 14, 482, i)
#     mean_sample = np.mean(results)
#     mean_sample_2.append(mean_sample)
#
# for i in range(1, 3001):
#     results = linear_congruential_generator(5, 26, 5, 27, i)
#     mean_sample = np.mean(results)
#     mean_sample_3.append(mean_sample)
#
# for i in range(1, 3001):
#     results = linear_congruential_generator(5, 4, 1, 9, i)
#     mean_sample = np.mean(results)
#     mean_sample_4.append(mean_sample)

plt.plot(num, mean_sample_1, label='m=2**31-1')
# plt.plot(num, mean_sample_2, label='m=482')
# plt.plot(num, mean_sample_3, label='m=27')
# plt.plot(num, mean_sample_4, label='m=9')
plt.title('Minimal Statistical Test for LCG')
plt.xlabel('Number of Samples')
plt.ylabel('Sample Mean')
plt.legend(framealpha=1)
plt.savefig("Problem_3.eps", dpi=600)
plt.show()

