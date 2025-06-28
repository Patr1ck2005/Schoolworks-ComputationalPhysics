import numpy as np
import matplotlib.pyplot as plt

# 生成示例数据并进行排序
data = [(1960, 6.67), (1970, 8.18), (1980, 9.81), (1990, 11.35), (2000, 12.63), (2010, 13.38)]

# 对数据按照 x 值排序
data.sort(key=lambda d: d[0])
x, y = zip(*data)

# 多项式拟合
coefficients = np.polyfit(x, y, deg=len(data)-1)  # 使用所有数据进行拟合，这里使用了len(data)-1次多项式
f_poly = np.poly1d(coefficients)

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

future_x_list = [2020]
for future_x in future_x_list:
    future_y = f_poly(future_x)
    print('年份：{}  人口总数：{:.2f}'.format(future_x, future_y))
