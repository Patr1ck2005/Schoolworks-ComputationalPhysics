import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# 生成示例数据并进行排序
data = [(1920,106.46), (1930, 123.08), (1940, 132.12), (1950, 152.27), (1960, 180.27), (1970, 205.05), (1980,227.23),(1990,249.46)]

# 对数据按照 x 值排序
data.sort(key=lambda d: d[0])
x, y = zip(*data)

# 连续多项式插值，启用外推功能
f_poly = interp1d(x, y, kind='cubic', fill_value='extrapolate')

# 生成更密集的x值，用于绘制插值结果的曲线
x_dense = np.linspace(min(x), max(x), 100)

# 计算插值结果
y_poly = f_poly(x_dense)

# 绘制原始数据和插值结果
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'bo', label='Original data')
plt.plot(x_dense, y_poly, 'r-', label='Quadratic interpolation')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolation Comparison')
plt.grid(True)
plt.show()

future_x_list=[2000,2020]
for future_x in future_x_list:
    future_y=f_poly(future_x)
    print('年份：{}  人口总数：{:.2f}'.format(future_x, future_y))

