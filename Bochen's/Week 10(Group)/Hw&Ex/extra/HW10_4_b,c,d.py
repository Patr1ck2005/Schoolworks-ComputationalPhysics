import numpy as np
import matplotlib.pyplot as plt
import cmath


# 定义传输函数q(u)
def q(u):
    d = 0.00002
    alpha = np.pi / d
    return np.sin(alpha * u) ** 2


# 定义被积函数f(u,x),其中x为参数，u为被积变量
def f(u, x):
    return cmath.sqrt(q(u)) * cmath.exp(2j * np.pi * u * x / 0.0000005)


# 采用simpson积分法实现积分
def simpson(u, n, x):
    result = f(u[0], x) + f(u[-1], x)
    i = 1
    j = 2
    # 利用while循环对偶数项与奇数项分别求和
    while i < len(u):
        result += 4 * f(u[i], x)
        i += 2
    while j < len(u) - 1:
        result += 2 * f(u[j], x)
        j += 2
    return result * u[-1] / (3 * (n - 1))


# 进行积分计算，并输出模方
def Integration(u, x):
    r, theta = cmath.polar(simpson(u, 49, x))
    return r ** 2


# 设置积分参数，simpson's rule 选取的点数为49，为保证图像光滑，选取1000个x的值进行计算
u = np.linspace(-0.0001, 0.0001, 49)
x = np.linspace(-0.05, 0.05, 1000)
y = np.array([])
for i in range(len(x)):
    temp = Integration(u, x[i])
    y = np.append(y, temp)

# 归一化处理
y = y / max(y)

# 绘制相对光强分布图
plt.figure()
plt.title('intensity distribution')
plt.xlabel('the distance from the central axis (m)')
plt.ylabel('relative intensity')
plt.plot(x, y)
plt.savefig(r'C:\Users\26918\Desktop\problem4_c.eps')

# 利用灰度图实现可视化
plt.figure()
y_image = np.tile(y, (1, 1))
plt.imshow(y_image, aspect='auto', extent=(-0.05, 0.05, 0.0, 1.0), cmap='gray')
plt.colorbar(label='Intensity')
plt.title('Diffraction Pattern of the Grating')
plt.xlabel('Position on Screen')
plt.savefig(r'C:\Users\26918\Desktop\problem4_d.eps')
plt.show()