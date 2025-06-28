import random
import numpy as np
import matplotlib.pyplot as plt


# Define the integrand function
def func(x):
    return 2 * np.sin(2 * np.sqrt(np.pi ** 2 - x ** 2)) + 2


# Define integration limits
xmin = 0
xmax = np.pi

# Initialize lists to store points
X_out = []  # Points outside the area
Y_out = []
X_in = []  # Points inside the area
Y_in = []

# Initialize variables
N = 50000  # Number of random points
hnit = 0  # Counter for points inside the area
Exact = -2.096131553556229  # Exact known value

# Arrays to store results over iterations
Value = np.zeros(N)
N_n = np.arange(1, N + 1)

# Perform Monte Carlo integration
for j in range(N):
    x = random.random() * np.pi
    y = random.random() * 4  # 2 * max(func(x)) = 4
    if y <= func(x):
        Y_in.append(y)
        X_in.append(x)
        hnit += 1
    else:
        Y_out.append(y)
        X_out.append(x)

    # Calculate current estimate of the integral
    Value[j] = np.pi * 4 * hnit / (j + 1) - 2 * np.pi

# Plot the results
plt.figure(figsize=(8, 6))

# Plot the integrand function and points
plt.plot(np.linspace(xmin, xmax, 1000), func(np.linspace(xmin, xmax, 1000)), 'g-', linewidth=3, label='Integrand')
plt.scatter(X_in, Y_in, s=1, c='b', label='Inside Area')
plt.scatter(X_out, Y_out, s=1, c='r', label='Outside Area')

plt.title('Monte Carlo Integration (N=50000)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))

# Plot the convergence of the integral estimate
plt.plot(N_n, np.full(N, Exact), 'r--', linewidth=3, label='Exact Value')
plt.plot(N_n, Value, 'b-', linewidth=2, label='Integral Estimate')

plt.title('Monte Carlo Integration Convergence')
plt.xlabel('N')
plt.ylabel('Integral Value')
plt.legend()
plt.grid(True)
plt.show()
