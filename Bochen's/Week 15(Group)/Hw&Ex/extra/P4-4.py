import numpy as np
import matplotlib.pyplot as plt

# Set up the Ising model parameters
J = 1.0  # Interaction strength
k_B = 1.0  # Boltzmann constant
T_values = np.linspace(1.0, 3.0, 10)  # Temperature values

# Define the function to calculate M^2
def calculate_m_squared(lattice):
    return np.mean(lattice)**2

# Perform simulations for different L values
L_values = [4, 8, 16, 32]
m_squared_values = []

for L in L_values:
    m_squared_avg = []
    for T in T_values:
        lattice = np.random.choice([-1, 1], size=(L, L))
        m_squared = []
        for _ in range(1000):
            for _ in range(L**2):
                i, j = np.random.randint(0, L, size=2)
                delta_E = 2 * J * lattice[i, j] * (
                    lattice[(i-1)%L, j] + lattice[(i+1)%L, j] +
                    lattice[i, (j-1)%L] + lattice[i, (j+1)%L]
                )
                if delta_E <= 0 or np.random.rand() < np.exp(-delta_E / (k_B * T)):
                    lattice[i, j] *= -1
            m_squared.append(calculate_m_squared(lattice))
        m_squared_avg.append(np.mean(m_squared))
    m_squared_values.append(m_squared_avg)

# Transpose the m_squared_values array
m_squared_values = np.array(m_squared_values).T

# Plot ln(M^2) against ln(L)
for i, m_squared_avg in enumerate(m_squared_values):
    plt.scatter(np.log(L_values), np.log(m_squared_avg), marker='o', label="L="+str(L_values[i]))

plt.xlabel('ln(L)')
plt.ylabel('ln(M^2)')
plt.legend()
plt.show()
