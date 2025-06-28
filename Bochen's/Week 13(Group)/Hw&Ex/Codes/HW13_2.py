import numpy as np
import matplotlib.pyplot as plt
import random

plt.rc('font', family='Times New Roman')


# 定义被积分函数
def fun(x):
    return 2 / (1 + x)


n = np.linspace(10, 1000000, 50)

Value = []
Error = []
for N in n:
    N = int(N)
    X = []
    Y = []
    O = []
    # 生成自变量矩阵
    for j in range(N):
        X.append(random.random())
        O.append(0)
    # 生成因变量矩阵
    # 生成自变量矩阵
    for j in range(N):
        Y.append(fun(X[j]))

    # 计算平均值
    Mean = np.average(Y)
    v = Mean
    Value.append(v)
    Error.append(np.abs(v - 2 * np.log(2)))
    print('N:', N, "value:", v, "error:", np.abs(v - 2 * np.log(2)))

log_n = np.log10(n)
error = np.log10(Error)
plt.figure(figsize=(6, 6))
plt.scatter(log_n, error, s=5, c='b')
plt.show()

# plt.figure(figsize=(6, 6))
# X_l = np.arange(0, 1, 0.01)
# Y_E = 1 / (np.sqrt(X_l) + X_l)
# Y_l = 2 / (1 + X_l)
# plt.plot(X_l, Y_l, 'g', linestyle='-', linewidth=2, label='Function')
# for i in range(N):
#     # plt.axvline(x=X[i], ls='--', c='black')
#     if i == 0:
#         plt.plot(X, Y, '+', color='red', label='Points')
#     else:
#         plt.plot(X, Y, '+', color='red')
# plt.plot(X, O, '+-', color='black')
# # plt.figure(figsize=(6,6))
# # plt.scatter(Dart,Error)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.xlim(0, 1)
# plt.ylim(0, 2)
# plt.title('Sample mean method of single experiment (N=200)')
# plt.legend(loc='upper right')
#
# plt.figure(figsize=(6, 6))
# plt.title('Function with Variable Substitution')
# plt.xlabel("x")
# plt.ylabel("y")
# plt.plot(X_l, Y_l, '-', color='blue', label='2/(x+x^2)')
# plt.fill_between(X_l, Y_l, 0, facecolor="lightgray")
# plt.legend(loc='upper right')
plt.show()
