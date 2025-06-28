import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# 生成示例数据并进行排序
data = [(-1.00, -14.58), (0.00, 0.00), (1.27, 0.00), (2.55, 0.00), (3.82, 0.00), (4.92, 0.88), (5.02,11.17)]

# 对数据按照 x 值排序
data.sort(key=lambda d: d[0])
x, y = zip(*data)

# 连续多项式插值
f_poly = interp1d(x, y, kind='cubic')

# 低阶多项式分段插值
f_piecewise = interp1d(x, y, kind='linear')

# 生成更密集的x值，用于绘制插值结果的曲线
x_dense = np.linspace(min(x), max(x), 100)

# 计算插值结果
y_poly = f_poly(x_dense)
y_piecewise = f_piecewise(x_dense)

# 绘制原始数据和插值结果
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'bo', label='Original data')
plt.plot(x_dense, y_poly, 'r-', label='Quadratic interpolation')
plt.plot(x_dense, y_piecewise, 'g-', label='Piecewise linear interpolation')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolation Comparison')
plt.grid(True)
plt.show()
