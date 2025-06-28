import numpy as np
import matplotlib.pyplot as plt

def initialize_system(N):
    return np.random.choice([-1, 1], size=N)

def calculate_energy(system, J, h):
    return -J * np.sum(system[:-1] * system[1:]) - h * np.sum(system)

def metropolis_step(system, J, h, k_B, T):
    N = len(system)
    for _ in range(N):
        i = np.random.randint(N)
        delta_E = 2 * J * system[i] * (system[(i+1) % N] + system[(i-1) % N]) + 2 * h * system[i]
        if delta_E <= 0 or np.random.rand() < np.exp(-delta_E / (k_B * T)):
            system[i] *= -1

def simulate_ising_model(N, J, h, k_B, T, equilibration_steps, measurement_steps):
    system = initialize_system(N)
    magnetizations = []

    # Equilibration steps
    for _ in range(equilibration_steps):
        metropolis_step(system, J, h, k_B, T)

    # Measurement steps
    for _ in range(measurement_steps):
        metropolis_step(system, J, h, k_B, T)
        magnetization = np.sum(system)
        magnetizations.append(magnetization)

    return np.mean(magnetizations)

# Constants
N = 20  # Number of spins
J = 1.0  # Interaction strength
k_B = 1.0  # Boltzmann constant

# Magnetic field range
magnetic_fields = np.linspace(-2.0, 2.0, 100)

# Temperature range
temperatures = [1.0, 2.0, 3.0]  # Example temperatures

# Simulation parameters
equilibration_steps = 100
measurement_steps = 200

# Perform simulation
magnetizations = []
for T in temperatures:
    magnetization = []
    for h in magnetic_fields:
        mean_magnetization = simulate_ising_model(N, J, h, k_B, T, equilibration_steps, measurement_steps)
        magnetization.append(mean_magnetization)
    magnetizations.append(magnetization)

# Plot magnetization as a function of h for various temperatures
for i, T in enumerate(temperatures):
    plt.plot(magnetic_fields, magnetizations[i], label=f'T = {T}')

plt.xlabel('Magnetic Field (h)')
plt.ylabel('Magnetization (M)')
plt.title('Magnetization vs Magnetic Field')
plt.legend()
plt.show()
