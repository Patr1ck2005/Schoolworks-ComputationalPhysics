import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

NN = 1000

def final_positions(n):
    positions = []
    for _ in range(NN):
        steps = np.random.choice([[1, 0], [0, -1], [-1, 0], [0, 1]], size=(n, 2))
        positions.append(np.cumsum(steps, axis=0))
    return positions

def d2mean(n):
    final_pos = final_positions(n)
    d2_mean = np.mean([np.sum(pos[-1]**2) for pos in final_pos])
    return d2_mean

def Rg2(n):
    data = final_positions(n)
    Rg2_mean = np.mean([np.sum((pos - np.mean(pos, axis=0))**2) for pos in data])
    return Rg2_mean

# Calculate data points for d2mean vs log(n)
data_d2mean = [(np.log(x), np.log(d2mean(x))) for x in range(1, 101)]
data_d2mean = np.array(data_d2mean)

plt.figure(figsize=(8, 6))
plt.plot(data_d2mean[:, 0], data_d2mean[:, 1], 'go', label='d2mean vs log(n)')
plt.xlabel('log(n)')
plt.ylabel('log(d2mean)')
plt.title('d2mean vs Step for Traditional Random Walk')
plt.grid(True)

# Fit a line to d2mean data
def linear_fit(x, a, b):
    return a * x + b

fit_d2mean, _ = curve_fit(linear_fit, data_d2mean[:, 0], data_d2mean[:, 1])
plt.plot(data_d2mean[:, 0], linear_fit(data_d2mean[:, 0], *fit_d2mean), 'r-', label='Fit: a*log(n) + b')

plt.legend()
plt.show()

# Calculate data points for Rg2 vs log(n)
data_Rg2 = [(np.log(x), np.log(Rg2(x))) for x in range(2, 101)]
data_Rg2 = np.array(data_Rg2)

plt.figure(figsize=(8, 6))
plt.plot(data_Rg2[:, 0], data_Rg2[:, 1], 'go', label='Rg2 vs log(n)')
plt.xlabel('log(n)')
plt.ylabel('log(Rg2)')
plt.title('Rg2 vs Step for Traditional Random Walk')
plt.grid(True)

# Fit a line to Rg2 data
fit_Rg2, _ = curve_fit(linear_fit, data_Rg2[:, 0], data_Rg2[:, 1])
plt.plot(data_Rg2[:, 0], linear_fit(data_Rg2[:, 0], *fit_Rg2), 'r-', label='Fit: a*log(n) + b')

plt.legend()
plt.show()

# Calculate Rg2(100) / d2mean(100)
ratio = Rg2(100) / d2mean(100)
print(f'Rg2(100) / d2mean(100) = {ratio}')
