import numpy as np
import matplotlib.pyplot as plt


# 定义函数
def f(x):
    return x*np.sin(2*np.pi*x+1)


# 在[-1, 1]范围内生成更密集的x值，用于绘制原始函数的曲线
x_dense = np.linspace(-1, 1, 1000)
y_dense = f(x_dense)

# 在[-1, 1]范围内生成不同数量点的情况
num_points_list = [7, 9, 17, 19, 21]

for num_points in num_points_list:
    # 创建新的图
    plt.figure(figsize=(8, 6))

    # 绘制原始函数
    plt.plot(x_dense, y_dense, 'b-', label='Original function')

    # 生成划分点并计算插值结果
    x_points = np.linspace(-1, 1, num_points)
    y_points = f(x_points)
    coefficients = np.polyfit(x_points, y_points, num_points - 1)
    f_interp = np.poly1d(coefficients)
    y_interp = f_interp(x_dense)

    # 绘制插值结果
    plt.plot(x_dense, y_interp, label='Interpolation')

    # 添加划分点
    plt.scatter(x_points, y_points, color='red', label='Interpolation points')

    # 添加标题、标签和图例
    plt.title(f'Interpolation with {num_points} points')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()

    # 显示网格
    plt.grid(True)

    # 显示图
    plt.show()
