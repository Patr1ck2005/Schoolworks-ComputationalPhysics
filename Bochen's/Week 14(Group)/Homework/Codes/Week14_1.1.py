import matplotlib.pyplot as plt
import numpy as np

lamda = 1
N = 1000
t = np.arange(1, N + 1, 1)


def function(m):
    List = []
    for i in range(1, N + 1):
        r = np.zeros((3, m))
        for k in range(i):
            phi = np.random.uniform(0, 2 * np.pi, m)  # 生成m个随机数
            costheta = np.random.uniform(-1, 1, m)  # 生成m个随机数
            r[0] = r[0] + lamda * np.sqrt(1 - costheta ** 2) * np.cos(phi)  # 粒子组的x坐标
            r[1] = r[1] + lamda * np.sqrt(1 - costheta ** 2) * np.sin(phi)  # 粒子组y坐标
            r[2] = r[2] + lamda * costheta  # 粒子组z坐标
        d = np.sum(np.reshape(r ** 2, (r ** 2).size))
        List.append(np.sqrt(d / m))
    return np.array(List)


# plt.scatter(t, function(50), marker='x', color='r', label='m=50')
# plt.scatter(t, function(500), marker='+', color='g', label='m=500')
plt.scatter(t, function(5000), marker='*', color='blue', label='m=5000')
plt.plot(t, np.sqrt(t), color='b', label='sqrt(t)')
plt.legend()
plt.xlabel('Number of collisions')
plt.ylabel('<d>/lamda')
plt.show()
