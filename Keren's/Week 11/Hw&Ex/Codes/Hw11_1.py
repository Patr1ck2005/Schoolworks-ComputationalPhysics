import matplotlib.pyplot as plt
import numpy as np


def buffon(n, l, a):
    # 生成随机角度和位置
    theta = np.random.uniform(0, np.pi, n)
    x = np.random.uniform(0, a / 2, n)

    # 统计成功次数
    k = np.sum(x <= l * np.sin(theta))

    # 计算估计的π值
    if k == 0:
        pi_estimate = np.nan  # 如果 k 为 0，将估计的π值设为 NaN
    else:
        pi_estimate = (2 * l * n) / (a * k)

    return pi_estimate


# 设定参数和范围
l_values = np.linspace(0, 1, 101)
a = 1
n = 1000000

# 计算估计的π值
pi_estimates = np.array([buffon(n, l, a) for l in l_values])

plt.scatter()
