import numpy as np

# 定义级数项数和精度
num_terms = 500000
precision = 10

# 计算正序级数和
series = 4 * np.sum((-1) ** (np.arange(num_terms+1)) / (2 * np.arange(num_terms+1) + 1))
sum_value_01 = np.around(series, precision)

print('正序计算Pi值：\n' + '{:.{}f}'.format(sum_value_01, precision))

# 计算级数和（倒序）
series_reverse = 4 * np.sum((-1) ** (np.arange(num_terms, -1, -1)) / (2 * np.arange(num_terms, -1, -1) + 1))
sum_value_reverse = np.around(series_reverse, precision)

print('逆序计算Pi值：\n' + '{:.{}f}'.format(sum_value_reverse, precision))



