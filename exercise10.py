import numpy as np
import matplotlib.pyplot as plt

# Define transition matrix and initial distribution
W = np.array([[0,   1,   0],
              [1/6, 1/2, 1/3],
              [0,   2/3, 1/3]])
P0 = np.array([1, 0, 0])
n_iterations = 30

# Prepare array to record the distribution at each step
distributions = np.zeros((n_iterations + 1, 3))
distributions[0] = P0.copy()

# Print and record the initial distribution
print("Iteration 0:", distributions[0])

# Iterate the Markov chain: print and record at each step
P = P0.copy()
for i in range(1, n_iterations + 1):
    P = P.dot(W)
    distributions[i] = P
    print(f"Iteration {i}:", P)

# Plot the evolution of each state's probability
plt.figure(figsize=(8, 5))
plt.plot(range(n_iterations + 1), distributions[:, 0], label='State 0')
plt.plot(range(n_iterations + 1), distributions[:, 1], label='State 1')
plt.plot(range(n_iterations + 1), distributions[:, 2], label='State 2')
plt.xlabel('Iteration')
plt.ylabel('Probability')
plt.title('Evolution of Probability Distribution Over Iterations')
plt.legend()
plt.tight_layout()
plt.savefig('ex10.png')
plt.show()
