import numpy as np
import matplotlib.pyplot as plt

NN = 1000

def final_positions(n):
    return [np.cumsum(np.random.choice([(1, 1), (1, -1), (-1, 1), (-1, -1)], size=n, replace=True), axis=0) for _ in range(NN)]

def d2mean(n):
    final_pos = final_positions(n)
    return np.mean([np.sum(final_pos[i][-1]**2) for i in range(NN)])

def Rg2(n):
    final_pos = final_positions(n)
    return np.mean([np.sum((final_pos[i] - np.mean(final_pos[i], axis=0))**2) for i in range(NN)])

data = [(np.log(x), np.log(d2mean(x))) for x in range(1, 101)]
rgdata = [(np.log(x), np.log(Rg2(x))) for x in range(2, 101)]

plt.figure(figsize=(8, 6))

# Plotting d2meanlogplot
plt.subplot(2, 1, 1)
plt.plot([d[0] for d in data], [d[1] for d in data], color='green', label='Data')
plt.plot(np.arange(1, 101), 1.00204 * np.log(np.arange(1, 101)) + 0.682722, color='red', label='Python Fit')
plt.xlabel('Log[n]')
plt.ylabel('Log[d2mean]')
plt.title('Log-Log Plot of d2mean')
plt.legend()

# Plotting rglogplot
plt.subplot(2, 1, 2)
plt.plot([d[0] for d in rgdata], [d[1] for d in rgdata], color='blue', label='Data')
plt.plot(np.arange(2, 101), np.log(np.arange(2, 101)) - 1.17, color='red', label='Python Fit')
plt.xlabel('Log[n]')
plt.ylabel('Log[Rg2]')
plt.title('Log-Log Plot of Rg2')
plt.legend()

plt.tight_layout()
plt.show()
