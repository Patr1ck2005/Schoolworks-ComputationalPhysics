# 设置函数f(x)=x(x-1)
def f(x):
    return x * (x - 1)


# 设置求解导数的公式
def derivative_f(x, delta):
    return (f(x + delta) - f(x)) / delta


# 设置导数函数 f'(x)=2x-1
def real_df(x):
    return 2 * x - 1


# 计算并且输出结果
approximation_df = derivative_f(1, 1e-2)
exact_df = real_df(1)

print('近似值：', '\n', approximation_df)
print('准确值：', '\n', exact_df)
