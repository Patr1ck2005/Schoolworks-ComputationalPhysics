import random

import numpy as np


def f(x):
    return 2 * x / (x ** 2 + x)  # 举例：积分函数 f(x) = x^2


def monte_carlo_stratified_integration(a, b, num_samples_per_stratum, num_strata):
    total_integral = 0.0
    stratum_width = (b - a) / num_strata

    for i in range(num_strata):
        # 确定当前子区间的边界
        a_i = a + i * stratum_width
        b_i = a + (i + 1) * stratum_width

        # 在当前子区间内进行抽样
        samples = [random.uniform(a_i, b_i) for _ in range(num_samples_per_stratum)]

        # 计算当前子区间内部分积分的估计值
        sum_f = sum(f(x) for x in samples)
        integral_i = stratum_width * (sum_f / num_samples_per_stratum)

        # 将当前子区间的积分估计值加到总积分中
        total_integral += integral_i

    return total_integral


# 示例：计算 f(x) = x^2 在区间 [0, 1] 上的积分
a = 0
b = 1
num_samples_per_stratum = 5000  # 每个子区间的样本数量
num_strata = 10  # 子区间的数量

estimated_integral = monte_carlo_stratified_integration(a, b, num_samples_per_stratum, num_strata)
error = abs(estimated_integral - 2 * np.log(2))
print("估计的积分值:", estimated_integral, '误差值：', error)
