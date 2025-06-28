import numpy as np


# 给出变量代换后的积分函数
def f(x):
    return 1


# 采用simpson积分法实现积分
def simpson(x, n):
    I = f(x[0]) + f(x[-1])
    i = 1
    j = 2

    # 利用while循环对奇数项与偶数项分别求和
    while i < len(x):
        I += 4 * f(x[i])
        i += 2
    while j < len(x) - 1:
        I += 2 * f(x[j])
        j += 2
    return I * x[-1] / (3 * (n - 1))


# 对变化变量后所得的两个积分分别求积并计算误差，其中simpson积分法取得点数为49
x1 = np.linspace(0, 2 * np.pi, 49)
x2 = np.linspace(0, 1, 49)
I1 = simpson(x1, 49)
I2 = 0.5 * simpson(x2, 49)
I = np.sqrt(I1 * I2)
error = abs(I - np.sqrt(np.pi)) / np.sqrt(np.pi)

# 输出结果
print('计算所得积分值为：', I)
print('误差为：', error)
