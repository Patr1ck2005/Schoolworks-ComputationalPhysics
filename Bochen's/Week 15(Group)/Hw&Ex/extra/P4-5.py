import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 设置模型参数
L = 100  # 网格大小
J = 1.0  # 相互作用强度
k_B = 1.0  # 波尔兹曼常数
T = 2.0  # 温度

# 初始化二维伊辛模型
lattice = np.random.choice([-1, 1], size=(L, L))

# 定义绘制函数
def plot_lattice(i):
    plt.clf()
    plt.imshow(lattice, cmap='Greens' if lattice[0][0] == -1 else 'binary')
    plt.axis('off')

# 定义马尔科夫过程函数
def monte_carlo_step():
    global lattice
    for _ in range(L * L):
        i, j = np.random.randint(0, L, size=2)
        delta_E = 2 * J * lattice[i, j] * (
            lattice[(i-1)%L, j] + lattice[(i+1)%L, j] +
            lattice[i, (j-1)%L] + lattice[i, (j+1)%L]
        )
        if delta_E <= 0 or np.random.rand() < np.exp(-delta_E / (k_B * T)):
            lattice[i, j] *= -1

# 创建动画帧
fig = plt.figure()
frames = []
for i in range(1000):
    monte_carlo_step()
    if i % 100 == 0:
        frame = plt.imshow(lattice, cmap='Greens' if lattice[0][0] == -1 else 'binary')
        frames.append([frame])

# 创建动画
ani = animation.ArtistAnimation(fig, frames, interval=100, blit=True)
ani.save('ising_animation.gif', writer='pillow')

plt.show()
