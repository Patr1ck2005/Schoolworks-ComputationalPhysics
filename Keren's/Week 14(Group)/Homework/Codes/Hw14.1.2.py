import matplotlib.pyplot as plt
import numpy as np

lamda = 1
N = 1000
t = np.arange(1, N + 1, 1)


def function(m, delta):
    List = []
    for i in range(1, N + 1):
        r = np.zeros((3, m))
        for k in range(i):
            phi = np.random.uniform(0, 2 * np.pi, m)  # 生成m个随机数
            costheta = np.random.uniform(-1, 1, m)  # 生成m个随机数
            lamda = np.random.uniform(1 - delta, 1 + delta, m)
            r[0] = r[0] + lamda * np.sqrt(1 - costheta ** 2) * np.cos(phi)  # 粒子组的x坐标
            r[1] = r[1] + lamda * np.sqrt(1 - costheta ** 2) * np.sin(phi)  # 粒子组y坐标
            r[2] = r[2] + lamda * costheta  # 粒子组z坐标
        d = np.sum(np.reshape(r ** 2, (r ** 2).size))
        List.append(np.sqrt(d / m))
    return np.array(List)


y1 = function(500, 0.3)
y2 = function(500, 0.5)
y3 = function(500, 0.7)
y4 = function(500, 0.9)
y5 = function(500, 0.1)


# 拟合曲线
def coefficient(delta):
    return np.sqrt(1 + delta ** 2 / 3)


plt.scatter(t, y5, marker='.', color='black', label='delta = 0.1', alpha=0.5)
plt.scatter(t, y1, marker='x', color='blue', label='delta = 0.3', alpha=0.5)
plt.scatter(t, y2, marker='+', color='red', label='delta = 0.5', alpha=0.5)
plt.scatter(t, y3, marker='*', color='cyan', label='delta = 0.7', alpha=0.5)
plt.scatter(t, y4, marker='d', color='magenta', label='delta = 0.9', alpha=0.5)

plt.plot(t, coefficient(0.1) * np.sqrt(t), linewidth=3.0, color='gray', label='Fitting 0.1')
plt.plot(t, coefficient(0.3) * np.sqrt(t), linewidth=3.0, color='dodgerblue', label='Fitting 0.3')
plt.plot(t, coefficient(0.5) * np.sqrt(t), linewidth=3.0, color='darkred', label='Fitting 0.5')
plt.plot(t, coefficient(0.7) * np.sqrt(t), linewidth=3.0, color='darkcyan', label='Fitting 0.7')
plt.plot(t, coefficient(0.9) * np.sqrt(t), linewidth=3.0, color='darkmagenta', label='Fitting 0.9')

plt.legend()
plt.xlabel('Number of collisions')
plt.ylabel('<d>/lamda')
plt.show()
