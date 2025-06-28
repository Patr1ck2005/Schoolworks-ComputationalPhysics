import numpy as np
import matplotlib.pyplot as plt

from scipy.ndimage import convolve, generate_binary_structure

# 50 by 50 grid
N = 30

plt.rc('font', family='Times New Roman')
plt.rc('figure', figsize=(10, 5))
plt.rcParams['axes.grid'] = True


def get_energy(lattice):
    # applies the nearest neighbours summation
    kern = generate_binary_structure(2, 1)
    kern[1][1] = False
    arr = -lattice * convolve(lattice, kern, mode='constant', cval=0)
    return arr.sum()


def metropolis(spin_arr, times, BJ, energy):
    net_spins = np.zeros(times - 1)
    net_energy = np.zeros(times - 1)

    for t in range(0, times - 1):
        # 2. pick random point on array and flip spin
        x = np.random.randint(0, N)
        y = np.random.randint(0, N)
        spin_i = spin_arr[x, y]  # initial spin
        spin_f = spin_i * -1  # proposed spin flip

        # compute change in energy for one atom
        E_i = 0
        E_f = 0
        if x > 0:
            E_i += -spin_i * spin_arr[x - 1, y]
            E_f += -spin_f * spin_arr[x - 1, y]
        if x < N - 1:
            E_i += -spin_i * spin_arr[x + 1, y]
            E_f += -spin_f * spin_arr[x + 1, y]
        if y > 0:
            E_i += -spin_i * spin_arr[x, y - 1]
            E_f += -spin_f * spin_arr[x, y - 1]
        if y < N - 1:
            E_i += -spin_i * spin_arr[x, y + 1]
            E_f += -spin_f * spin_arr[x, y + 1]

        dE = E_f - E_i

        if (dE > 0) * (np.random.random() < np.exp(-BJ * dE)):
            spin_arr[x, y] = spin_f
            energy += dE

        elif dE <= 0:
            spin_arr[x, y] = spin_f
            energy += dE

        net_spins[t] = spin_arr.sum()
        net_energy[t] = energy

    return net_spins, net_energy, spin_arr


num = 10 ** 6

init_random = np.random.random((N, N))

lattice = np.zeros((N, N))
lattice[init_random >= 0.5] = 1
lattice[init_random < 0.5] = -1
spins, energies, pattern = metropolis(lattice, num, 2, get_energy(lattice))
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
ax = axes[0]
ax.plot(spins / N ** 2)
ax.set_xlabel('Algorithm Time Steps')
ax.set_ylabel(r'Average Spin $\bar{m}$')
ax.grid()
ax = axes[1]
ax.plot(energies / N ** 2)
ax.set_xlabel('Algorithm Time Steps')
ax.set_ylabel(r'Energy $E/J$')
ax.grid()
fig.tight_layout()
fig.suptitle(r'Evolution of Average Spin and Energy for $\beta J=$2', y=1.07, size=18)

plt.figure()
plt.imshow(pattern)
plt.show()
