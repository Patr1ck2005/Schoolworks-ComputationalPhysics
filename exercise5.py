import math

# 定义目标函数
def f(x):
    return 2 - x - math.exp(-x)

# 二分法
def bisection_method(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("区间端点函数值符号相同，无法使用二分法。")
    for _ in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        if abs(fc) < tol:  # 根足够接近零时终止
            return c
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    return (a + b) / 2  # 返回最后一次迭代的中点

# 割线法
def secant_method(x0, x1, tol=1e-6, max_iter=100):
    for _ in range(max_iter):
        f0, f1 = f(x0), f(x1)
        if abs(f1) < tol:  # 直接满足条件时终止
            return x1
        if abs(f1 - f0) < 1e-12:  # 防止除以零
            raise ValueError("割线法分母为零，无法继续迭代。")
        x_next = x1 - f1 * (x1 - x0) / (f1 - f0)
        if abs(x_next - x1) < tol:  # 两次迭代差小于容差时终止
            return x_next
        x0, x1 = x1, x_next
    return x1  # 返回最后一次迭代的结果

# 调用二分法，假设根在区间 [0, 2] 内
root_bisect = bisection_method(0, 2)
print(f"二分法求得的根: {root_bisect:.6f}")

# 调用割线法，初始猜测为 x0=1, x1=2
root_secant = secant_method(1, 2)
print(f"割线法求得的根: {root_secant:.6f}")
