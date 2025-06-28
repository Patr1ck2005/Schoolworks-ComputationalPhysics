import numpy as np
import matplotlib.pyplot as plt


# 计算周期性边界的系统能量
def energy(spins, h):
    n = len(spins)
    energy = 0
    for i in range(n):
        energy += -(spins[(i - 1) % n] + spins[(i + 1) % n])*spin[i] - h * spins[i]
    return energy/2


# 实现自旋翻转
def flip(spins, beta):
    n = len(spins)
    # 随机选取翻转的自旋格子
    i = np.random.randint(n)
    s = -spins[i]

    deltaE = 2 * spins[i] * (spins[(i - 1) % n] + spins[(i + 1) % n])
    if deltaE <= 0:
        spins[i] = s
    elif np.random.random() < np.exp(-beta * deltaE):
        spins[i] = s

    return spins


# 实现MCMC算法
def MCMC(spins, T, n, h):
    beta = 1.0 / T
    energies = np.array([])
    m = np.array([])
    for i in range(n):
        spins = flip(spins, beta)
        e = energy(spins, h)
        m = np.append(m, sum(spins))
        energies = np.append(energies, e)
    return energies, m


spin = np.random.choice([-1, 1], size=20)
spin = flip(spin, 100)
T = np.linspace(0.5, 5.0, 100)
y = -20 * np.tanh(1.0 / T)
E = np.array([])
M = np.array([])
for i in range(len(T)):
    e, m = MCMC(spin, T[i], 1000, 0)
    E = np.append(E, np.sum(e) / len(e))
    M = np.append(M, np.sum(m) / len(m))

plt.figure()
plt.scatter(T, E, label='average energy')
plt.plot(T, y)
plt.xlabel('T')
plt.ylabel('energy')
plt.title('1D ising model ')
plt.legend()

plt.figure()
plt.scatter(T, M, label='M', color='green')
plt.xlabel('T')
plt.ylabel('M')
plt.title('1D ising model ')
plt.legend()
plt.show()
