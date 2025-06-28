import numpy as np
import matplotlib.pyplot as plt

from scipy.ndimage import convolve, generate_binary_structure

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


def get_spin_energy(lattice, BJs):
    ms = np.zeros(len(BJs))
    E_means = np.zeros(len(BJs))
    E_stds = np.zeros(len(BJs))
    for i, bj in enumerate(BJs):
        spins, energies, _ = metropolis(lattice, 10 ** 6, bj, get_energy(lattice))
        ms[i] = spins[-10 ** 5:].mean() / N ** 2
        E_means[i] = energies[-10 ** 5:].mean()
        E_stds[i] = energies[-10 ** 5:].std()
    return ms, E_means, E_stds



def metropolis2(spin_arr, times, BJ, energy):
    net_spins = np.zeros(times - 1)
    net_energy = np.zeros(times - 1)

    for t in range(0, times - 1):
        # pick point on array and flip spin in order
        x = 0
        y = 0
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

        # update the position
        x = x + 1
        y = y + 1

    return net_spins, net_energy, spin_arr


def get_spin_energy2(lattice, BJs):
    ms = np.zeros(len(BJs))
    E_means = np.zeros(len(BJs))
    E_stds = np.zeros(len(BJs))
    for i, bj in enumerate(BJs):
        spins, energies, _ = metropolis2(lattice, 10 ** 6, bj, get_energy(lattice))
        ms[i] = spins[-10 ** 5:].mean() / N ** 2
        E_means[i] = energies[-10 ** 5:].mean()
        E_stds[i] = energies[-10 ** 5:].std()
    return ms, E_means, E_stds


N = 30

init_random = np.random.random((N, N))
lattice_n = np.zeros((N, N))
lattice_n[init_random >= 0.75] = 1
lattice_n[init_random < 0.75] = -1

init_random = np.random.random((N, N))
lattice_p = np.zeros((N, N))
lattice_p[init_random >= 0.25] = 1
lattice_p[init_random < 0.25] = -1

BJs = np.arange(0.25, 1, 0.05)
ms_n, E_means_n, E_stds_n = get_spin_energy(lattice_n, BJs)
ms_p, E_means_p, E_stds_p = get_spin_energy(lattice_p, BJs)

plt.figure(figsize=(8, 5))
plt.plot(1 / BJs, E_means_n, 'o--', label='75% of spins started negative')
plt.plot(1 / BJs, E_means_p, 'o--', label='75% of spins started positive')
plt.xlabel(r'$\left(\dfrac{k}{J}\right)T$', font={'size': 16})
plt.ylabel(r'$\overline{E}$', font={'size': 16})
plt.legend(facecolor='white', framealpha=1)

plt.figure(figsize=(8,5))
plt.plot(1/BJs, ms_n, 'o--', label='75% of spins started negative')
plt.plot(1/BJs, ms_p, 'o--', label='75% of spins started positive')
plt.xlabel(r'$\left(\dfrac{k}{J}\right)T$', font={'size':16})
plt.ylabel(r'$\overline{m}$', font={'size':16})
plt.legend(facecolor='white', framealpha=1)
plt.show()