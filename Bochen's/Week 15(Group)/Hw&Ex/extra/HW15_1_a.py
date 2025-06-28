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


spin = np.ones(20)
E, m = MCMC(spin, 1.0, 10000, 0)

plt.figure()
plt.plot(E, label='energy')
plt.xlabel('MC steps')
plt.ylabel('energy')
plt.title('1D ising model at T = 1.0 ')
plt.legend()

plt.figure()
plt.plot(m, label='M', color='green')
plt.xlabel('MC steps')
plt.ylabel('M')
plt.title('1D ising model at T = 1.0 ')
plt.legend()
plt.show()
