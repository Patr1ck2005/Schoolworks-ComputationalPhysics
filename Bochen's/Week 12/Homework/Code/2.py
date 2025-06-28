import random
import numpy as np
from scipy.stats import chisquare
import matplotlib.pyplot as plt

# 进行1000次卡方检验
chi_square_values = []

for _ in range(1000):
    # 生成一组随机数
    random_numbers = [random.random() for _ in range(100)]
    # 将随机数分组，这里假设是10个区间
    observed_frequencies, _ = np.histogram(random_numbers, bins=10, range=(0, 1))
    # 计算期望频率，均匀分布下每个区间的期望频率是10
    expected_frequencies = [10] * 10
    # 进行卡方检验
    chi_square, p = chisquare(observed_frequencies, f_exp=expected_frequencies)
    # 保存卡方检验值
    chi_square_values.append(chi_square)

# 绘制卡方值的频数分布图
plt.figure(figsize=(10, 6))
plt.hist(chi_square_values, bins=10, alpha=0.75, color='blue', edgecolor='black')
plt.title('Frequency Distribution of Chi-square Values')
plt.xlabel('Chi-square value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
