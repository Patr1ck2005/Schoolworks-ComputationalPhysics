# 三次样条插值
import numpy as np
from matplotlib import pyplot as plt
import natural_cubic_splines  # 求求你把该文件放在同一文件夹内

''' 
定义插值函数为: S_i(x_i) = y_i + b_i(x - x_i) + c_i(x - x_i)^2 + d_i(x - x_i)^3
'''

#  输入需要插值的点
x_1 = [2.5, 1.3, -0.25, 0, 0.25, -1.3, -2.5, -1.3, 0.25, 0, -0.25, 1.3, 2.5]  # 插值点的横坐标
y_1 = [0, -0.25, 1.3, 2.5, 1.3, -0.25, 0, 0.25, -1.3, -2.5, -1.3, 0.25, 0]  # 插值点的纵坐标
# 参数t
t = np.zeros(len(x_1))
for i in range(len(t)):
    if i == 0:
        t[i] = 0
        continue
    t[i] = t[i - 1] + np.sqrt((x_1[i] - x_1[i - 1]) ** 2 + (y_1[i] - y_1[i - 1]) ** 2)

# 调用本地！本地！本地！文件夹内的函数（该函数只返回插值函数的函数值！）
x = natural_cubic_splines.natural_cubic_splines(t, x_1)
y = natural_cubic_splines.natural_cubic_splines(t, y_1)

# 绘图
plt.scatter(x_1, y_1)
plt.plot(x, y)
plt.show()
