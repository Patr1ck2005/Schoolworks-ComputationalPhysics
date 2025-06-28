# 定义需求解的函数
def func(x):
    G = 6.674e-11
    M = 5.974e24
    m = 7.348e22
    R = 3.844e8
    w = 2.662e-6
    y = G * M / (x * x) - G * m / ((R - x) * (R - x)) - w * w * x
    return y


# 实现二分法求解
def func1(x, y, z):
    while (y - x) > z:
        mid = (x + y) / 2.0
        if func(mid) == 0:
            return mid
        elif func(x) * func(mid) < 0:
            y = mid
        else:
            x = mid
    return (x + y) / 2.0


# 实现截断法求解
def func2(x, y, z):
    while abs(x - y) > z:
        temp = y - func(y) * (y - x) / (func(y) - func(x))
        x = y
        y = temp
    return y


# 代入预设初始范围
x1 = 1.9e8
y1 = 3.8e8
root1 = func1(x1, y1, 0.000001)
root3 = func2(x1, y1, 0.000001)
print('Bisection Method求得根为：', '\n%.6e' % root1)
print('Secant Method求得根为：', '\n%.6e' % root3)
