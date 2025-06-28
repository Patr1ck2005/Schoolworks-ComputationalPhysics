import numpy as np
import matplotlib.pyplot as plt


def energy_ising_1d(configuration, J, h):
    num_spins = len(configuration)
    energy = 0.0
    for i in range(num_spins):
        spini = configuration[i]
        # set the value of spin i+1, make sure to test if i+1<num_spins, and otherwise account for periodic boundaries
        # you can do this with an if statement if you have to
        ip1 = (i + 1) % num_spins
        spinip1 = configuration[ip1]

        energy = energy - J * (spini * spinip1) - h * spini

    return energy


def energy_difference(J, h, si, sleft, sright):
    # fill in the formula for the energy difference from flipping spin i,
    # which has value si= 1 or -1, with spin values sleft and sright on the left and right
    dE = 2 * h * si + 2 * J * si * (sleft + sright)
    return dE


def metropolis_mc_fast(n_steps, n_lattice_sites, beta, J, h, debug=False, save_freq=10):
    # we can start with a random configuration of size n_lattice_sites by generating a random list
    #    of zeros and twos, then subtracting 1, the following does that, do you see why? Play around
    #   with this function in an empty box if you don't
    configuration = 2 * np.random.randint(2, size=n_lattice_sites) - 1
    average_spins = []

    if debug is True:
        print("Starting configuration:", configuration)

    current_energy = energy_ising_1d(configuration, J, h)
    for i in range(n_steps):

        # set this like you did above:
        spin_to_change = np.random.randint(n_lattice_sites)

        si = configuration[spin_to_change]
        # now figure out the values of the spin to the left and the spin to the right, remembering
        #  to take into account periodic boundary conditions for both
        # you can use if statements if you have to
        sright = configuration[(spin_to_change + 1) % n_lattice_sites]
        sleft = configuration[(spin_to_change - 1) % n_lattice_sites]

        dE = energy_difference(J, h, si, sleft, sright)

        r = np.random.random()
        # fill in the metropolis critereon, using dE
        if r < min(1, np.exp(-beta * (dE))):
            # flip the spin
            configuration[spin_to_change] *= -1
            # update the energy
            current_energy += dE
        else:
            pass

        # this computes the average spin
        average_spin = configuration.mean()

        if i % save_freq == 0:
            average_spins.append(average_spin)

        if debug and i % 10 == 0:
            print("%i: " % i, configuration, "Energy:", current_energy, "Spin:", average_spin)

    return average_spins


def ising_spin_exact(beta, J, h):
    sbh = np.sinh(beta * h)
    cbh = np.cosh(beta * h)
    efactor = np.exp(-4 * beta * J)
    numerator = sbh + sbh * cbh / np.sqrt(sbh * sbh + efactor)
    denominator = cbh + np.sqrt(sbh * sbh + efactor)
    return numerator / denominator


# system size dependence

test_beta = 1.0
test_J = 1

# scanning beta for a range of h's

test_h_list = np.arange(-1, 1.25, 0.25)
n_lattice_site_list = (3, 5, 25, 50, 100)

for test_n_lattice_sites in n_lattice_site_list:
    test_n_steps = test_n_lattice_sites * 500

    spin_vs_h = []
    for test_h in test_h_list:
        average_spin_at_h = metropolis_mc_fast(test_n_steps, test_n_lattice_sites, test_beta, test_J, test_h)
        mean_spin_from_trajectory = np.mean(average_spin_at_h[len(average_spin_at_h) // 2:])
        spin_vs_h.append(mean_spin_from_trajectory)

    p = plt.plot(test_h_list, spin_vs_h, marker='o', label="$N=%i$" % test_n_lattice_sites, linestyle='')

predicted_spin_v_h = ising_spin_exact(test_beta, test_J, test_h_list)
plt.plot(test_h_list, predicted_spin_v_h, label="Theory,$N\\rightarrow\\infty$", color=p[0].get_color(), linestyle='--')

plt.xlabel('$h$')
plt.ylabel('$\\langle m \\rangle$')
plt.axhline(0, linestyle='--', color='black')
plt.axvline(0, linestyle='--', color='black')
plt.legend(loc=0)
plt.show()