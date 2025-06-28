import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare

# 设置随机种子以获得可重现的结果
np.random.seed(0)

# 参数设置
num_trials = 1000  # 操作次数
num_samples = 100000  # 每次操作生成的随机数个数
num_bins = 20  # 用于卡方检验的区间数量

# 存储每次操作的卡方值
chi_square_values = []

# 进行1000次卡方检验
for _ in range(num_trials):
    # 生成随机数
    data = np.random.rand(num_samples)

    # 执行卡方检验并存储卡方值
    observed, _ = np.histogram(data, bins=num_bins, density=False)
    expected = np.full(num_bins, num_samples / num_bins)
    # chi2_stat, _ = chisquare(observed, f_exp=expected)
    chi2_stat = np.sum((observed - expected) ** 2 / expected)
    chi_square_values.append(chi2_stat)

# 对1000次操作的卡方值进行频数统计
plt.hist(chi_square_values, bins=30, alpha=0.75, color='blue', edgecolor='black')

# 绘制卡方值与频数值的关系图
plt.ylabel('Frequency function', fontsize=14)
plt.xlabel(r'$\chi^2$ values', fontsize=14)
plt.title('Frequency Distribution of Chi-square Values over 1000 Trials', fontsize=14)

# 在直方图上绘制卡方分布的理论均值
plt.axvline(x=num_bins, color='red', linestyle='--',
            label='Theoretical mean of Chi-square distribution for df=100')
plt.legend()
plt.grid(True)
plt.show()
# 打印出卡方值的一些统计信息
print(f"Minimum Chi-Square Value: {np.min(chi_square_values)}")
print(f"Maximum Chi-Square Value: {np.max(chi_square_values)}")
print(f"Mean Chi-Square Value: {np.mean(chi_square_values)}")
