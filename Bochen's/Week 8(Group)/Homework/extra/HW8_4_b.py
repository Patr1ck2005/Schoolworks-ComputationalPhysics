import numpy as np


# 设置函数f(x)=x(x-1)
def f(x):
    return x * (x - 1)


# 设置求解导数的公式
def derivative_f(x, delta):
    return (f(x + delta) - f(x)) / delta


# 设置导数函数 f'(x)=2x-1
def real_df(x):
    return 2 * x - 1


# 设置不同的delta值来计算导数并输出结果
log_delta = np.linspace(-2, -18, 9)
delta = 10 ** log_delta
exact_df = real_df(1)
print('准确值为', '\n', exact_df)
for i in range(len(delta)):
    approximation_df = derivative_f(1, delta[i])
    print('当delta={}时'.format(delta[i]), '\n', approximation_df)
