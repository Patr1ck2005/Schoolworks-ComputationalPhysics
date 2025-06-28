import numpy as np
from matplotlib import pyplot as plt


def f(x):
    return x * np.exp(x ** 3)


def f1_derivative(x):
    return (3 * x ** 3 + 1) * np.exp(x ** 3)


def f2_derivative(x):
    return (9 * x ** 5 + 12 * x ** 2) * np.exp(x ** 3)


def f3_derivative(x):
    return (27 * x ** 7 + 81 * x ** 4 + 24 * x) * np.exp(x ** 3)


h_log = np.linspace(-1, -20, 200)

ls = 10 ** (h_log)
delta_f1_logs_1 = []
delta_f2_logs_1 = []
delta_f3_logs_1 = []
delta_f1_logs_2 = []
delta_f2_logs_2 = []
delta_f3_logs_2 = []
delta_f1_logs_4 = []
delta_f2_logs_4 = []
delta_f3_logs_4 = []

for h in ls:
    x_0 = 1.0
    y_0 = f(x_0)
    y_1 = f(x_0 + h)
    y_2 = f(x_0 + 2 * h)
    y_11 = f(x_0 - h)
    y_12 = f(x_0 - 2 * h)

    f1_val = (y_1 - y_11) / (2 * h)
    delta_f1 = abs(f1_val - f1_derivative(x_0))
    delta_f1_log = np.log10(delta_f1)
    delta_f1_logs_2.append(delta_f1_log)

    f2_val = (y_1 - 2 * y_0 + y_11) / (h * h)
    delta_f2 = abs(f2_val - f2_derivative(x_0))
    delta_f2_log = np.log10(delta_f2)
    delta_f2_logs_2.append(delta_f2_log)

    f3_val = (y_2 - 2 * y_1 + 2 * y_11 - y_12) / (2 * h ** 3)
    delta_f3 = abs(f3_val - f3_derivative(x_0))
    delta_f3_log = np.log10(delta_f3)
    delta_f3_logs_2.append(delta_f3_log)

    print('h={}时的一阶导函数值:'.format(h) + str(f1_val) + '，误差为：' + str(delta_f1))
    print('h={}时的二阶导函数值:'.format(h) + str(f2_val) + '，误差为：' + str(delta_f2))
    print('h={}时的三阶导函数值:'.format(h) + str(f3_val) + '，误差为：' + str(delta_f3))
    print('**********************************************')

for h in ls:
    x_0 = 1.0
    y_0 = f(x_0)
    y_1 = f(x_0 + h)
    y_2 = f(x_0 + 2 * h)
    y_3 = f(x_0 + 3 * h)
    y_11 = f(x_0 - h)
    y_12 = f(x_0 - 2 * h)

    f1_val = (y_1 - y_0) / h
    delta_f1 = abs(f1_val - f1_derivative(x_0))
    delta_f1_log = np.log10(delta_f1)
    delta_f1_logs_1.append(delta_f1_log)

    f2_val = (y_2 - 2 * y_1 + y_0) / (h ** 2)
    delta_f2 = abs(f2_val - f2_derivative(x_0))
    delta_f2_log = np.log10(delta_f2)
    delta_f2_logs_1.append(delta_f2_log)

    f3_val = (y_3 - 3 * y_2 + 3 * y_1 - y_0) / (h ** 3)
    delta_f3 = abs(f3_val - f3_derivative(x_0))
    delta_f3_log = np.log10(delta_f3)
    delta_f3_logs_1.append(delta_f3_log)

    print('h={}时的一阶导函数值:'.format(h) + str(f1_val) + '，误差为：' + str(delta_f1))
    print('h={}时的二阶导函数值:'.format(h) + str(f2_val) + '，误差为：' + str(delta_f2))
    print('h={}时的三阶导函数值:'.format(h) + str(f3_val) + '，误差为：' + str(delta_f3))
    print('**********************************************')

for h in ls:
    x_0 = 1.0
    y_0 = f(x_0)
    y_1 = f(x_0 + h)
    y_2 = f(x_0 + 2 * h)
    y_3 = f(x_0 + 3 * h)
    y_11 = f(x_0 - h)
    y_12 = f(x_0 - 2 * h)
    y_13 = f(x_0 - 3 * h)

    f1_val = (y_12 - 8 * y_11 + 8 * y_1 - y_2) / (12 * h)
    delta_f1 = abs(f1_val - f1_derivative(x_0))
    delta_f1_log = np.log10(delta_f1)
    delta_f1_logs_4.append(delta_f1_log)

    f2_val = (16 * y_11 - y_12 - 30 * y_0 + 16 * y_1 - y_2) / (12 * h ** 2)
    delta_f2 = abs(f2_val - f2_derivative(x_0))
    delta_f2_log = np.log10(delta_f2)
    delta_f2_logs_4.append(delta_f2_log)

    f3_val = (13 * y_11 - 8 * y_12 + y_13 - 13 * y_1 + 8 * y_2 - y_3) / (8 * h ** 3)
    delta_f3 = abs(f3_val - f3_derivative(x_0))
    delta_f3_log = np.log10(delta_f3)
    delta_f3_logs_4.append(delta_f3_log)

    print('h={}时的一阶导函数值:'.format(h) + str(f1_val) + '，误差为：' + str(delta_f1))
    print('h={}时的二阶导函数值:'.format(h) + str(f2_val) + '，误差为：' + str(delta_f2))
    print('h={}时的三阶导函数值:'.format(h) + str(f3_val) + '，误差为：' + str(delta_f3))
    print('**********************************************')

plt.figure()
plt.scatter(h_log, delta_f1_logs_1, label='1st Order')
plt.scatter(h_log, delta_f1_logs_2, label='2nd Order')
plt.scatter(h_log, delta_f1_logs_4, label='4th Order')
plt.legend()
plt.show()

plt.figure()
plt.scatter(h_log, delta_f2_logs_1, label='1st Order')
plt.scatter(h_log, delta_f2_logs_2, label='2nd Order')
plt.scatter(h_log, delta_f2_logs_4, label='4th Order')
plt.legend()
plt.show()

plt.figure()
plt.scatter(h_log, delta_f3_logs_1, label='1st Order')
plt.scatter(h_log, delta_f3_logs_2, label='2nd Order')
plt.scatter(h_log, delta_f3_logs_4, label='4th Order')
plt.legend()
plt.show()
