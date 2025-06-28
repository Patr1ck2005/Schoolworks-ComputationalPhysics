import numpy as np
import matplotlib.pyplot as plt


# 计算周期性边界的系统能量
def energy(spins, h):
    n = len(spins)
    energy = 0
    for i in range(n):
        energy += -(spins[(i - 1) % n] + spins[(i + 1) % n]) * spin[i] - h * spins[i]
    return energy / 2


# 实现自旋翻转
def flip(spins, beta):
    n = len(spins)
    # 随机选取翻转的自旋格子
    i = np.random.randint(n)
    s = -spins[i]
    accept = 0

    deltaE = 2 * spins[i] * (spins[(i - 1) % n] + spins[(i + 1) % n])
    if deltaE <= 0:
        spins[i] = s
        accept = 1
    elif np.random.random() < np.exp(-beta * deltaE):
        spins[i] = s
        accept = 1
    return spins, accept


# 实现MCMC算法
def MCMC(spins, T, n, h):
    beta = 1.0 / T
    energies = np.array([])
    m = np.array([])
    accept = 0
    for i in range(n):
        spins, a = flip(spins, beta)
        accept += a
        e = energy(spins, h)
        m = np.append(m, sum(spins))
        energies = np.append(energies, e)
    ratio = accept / n

    return energies, m, ratio


spin = np.random.choice([-1, 1], size=20)
spin,k = flip(spin, 100)
T = np.linspace(0.5, 5.0, 100)
E = np.array([])
M = np.array([])
R=np.array([])
for i in range(len(T)):
    e, m, r = MCMC(spin, T[i], 1000, 0)
    E = np.append(E, np.sum(e) / len(e))
    M = np.append(M, np.sum(m) / len(m))
    R = np.append(R,r)

plt.figure()
plt.scatter(T, R, label='acceptance ratio')
plt.xlabel('T')
plt.ylabel('ratio')
plt.title('1D ising model at MC steps=1000')
plt.legend()
plt.show()
