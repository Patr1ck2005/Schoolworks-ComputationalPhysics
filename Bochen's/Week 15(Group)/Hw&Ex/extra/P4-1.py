import numpy as np
import matplotlib.pyplot as plt

def initialize_system(N):
    return np.random.choice([-1, 1], size=(N, N))

def calculate_energy(system, J):
    energy = 0
    for i in range(len(system)):
        for j in range(len(system)):
            energy += -J * system[i, j] * (
                system[(i+1) % len(system), j] +
                system[(i-1) % len(system), j] +
                system[i, (j+1) % len(system)] +
                system[i, (j-1) % len(system)]
            )
    return energy

def metropolis_step(system, J, k_B, T):
    N = len(system)
    for _ in range(N**2):
        i, j = np.random.randint(N, size=2)
        delta_E = 2 * J * system[i, j] * (
            system[(i+1) % N, j] +
            system[(i-1) % N, j] +
            system[i, (j+1) % N] +
            system[i, (j-1) % N]
        )
        if delta_E <= 0 or np.random.rand() < np.exp(-delta_E / (k_B * T)):
            system[i, j] *= -1

def simulate_2d_ising_model(N, J, k_B, T_range, equilibration_steps, measurement_steps):
    system = initialize_system(N)
    magnetizations = []

    for T in T_range:
        energy = calculate_energy(system, J)
        magnetization = np.sum(system) / (N**2)
        magnetizations.append(magnetization)

        # Equilibration steps
        for _ in range(equilibration_steps):
            metropolis_step(system, J, k_B, T)

        # Measurement steps
        for _ in range(measurement_steps):
            metropolis_step(system, J, k_B, T)
            magnetization = np.sum(system) / (N**2)
            magnetizations.append(magnetization)

    return magnetizations

# Constants
N = 20  # Size of the system (N x N)
J = 1.0  # Interaction strength
k_B = 1.0  # Boltzmann constant

# Simulation parameters
equilibration_steps = 1000
measurement_steps = 2000

# Temperature range
T_range = np.linspace(1.0, 4.0, 50)

# Perform simulation
magnetizations = simulate_2d_ising_model(N, J, k_B, T_range, equilibration_steps, measurement_steps)

# Plot magnetization versus temperature
plt.plot(T_range, magnetizations, marker='o')
plt.axvline(x=2.27, color='r', linestyle='--', label='Phase Transition')
plt.xlabel('Temperature (T)')
plt.ylabel('Magnetization (m)')
plt.title('Magnetization vs Temperature')
plt.legend()
plt.show()
