import numpy as np
import matplotlib.pyplot as plt

NN = 1000

def final_positions_saw(n):
    final_positions = []
    for _ in range(NN):
        position = np.array([0, 0])
        visited = [position.copy()]
        steps = 0
        while steps < n:
            valid_steps = [move for move in [(1, 0), (0, -1), (-1, 0), (0, 1)]
                           if (position + np.array(move)).tolist() not in visited]
            if not valid_steps:
                break
            position += np.array(valid_steps[np.random.randint(len(valid_steps))])
            visited.append(position.copy())
            steps += 1
        final_positions.append(np.array(visited))
    return final_positions

def d2mean_saw(n):
    final_positions = final_positions_saw(n)
    d2mean = np.mean([np.sum(np.square(traj[-1])) for traj in final_positions])
    return d2mean

def rg2_saw(n):
    final_positions = final_positions_saw(n)
    rg2 = np.mean([np.mean(np.sum(np.square(traj - np.mean(traj, axis=0)), axis=1)) for traj in final_positions])
    return rg2

data = []
for x in range(1, 101):
    data.append([np.log(x), np.log(d2mean_saw(x))])

data = np.array(data)

plt.figure()
plt.plot(data[:, 0], data[:, 1], 'o', color='brown', label=r'$\langle R^2_e \rangle$ vs Step for Traditional Random Walk')

def fit_function(x, a, b):
    return a * x + b

fit_range = 10
fit_data = data[:fit_range]
fit_params, _ = curve_fit(fit_function, fit_data[:, 0], fit_data[:, 1])
a_fit, b_fit = fit_params
plt.plot(data[:, 0], a_fit * data[:, 0] + b_fit, '-', color='red', label='Fit: {:.3f}x + {:.3f}'.format(a_fit, b_fit))

v = b_fit / 2

plt.legend()
plt.xlabel('Log(Step)')
plt.ylabel('Log(<R^2_e>)')
plt.title(r'$\langle R^2_e \rangle$ vs Step for Traditional Random Walk')
plt.grid(True)
plt.show()

rg_data = []
for x in range(2, 101):
    rg_data.append([np.log(x), np.log(rg2_saw(x))])

rg_data = np.array(rg_data)

plt.figure()
plt.plot(rg_data[:, 0], rg_data[:, 1], 'o', color='blue', label=r'$\langle R^2_g \rangle$ vs Step for Traditional Random Walk')

def fit_function_rg(x, a, b):
    return a * x + b

fit_range_rg = 10
fit_data_rg = rg_data[:fit_range_rg]
fit_params_rg, _ = curve_fit(fit_function_rg, fit_data_rg[:, 0], fit_data_rg[:, 1])
a_fit_rg, b_fit_rg = fit_params_rg
plt.plot(rg_data[:, 0], a_fit_rg * rg_data[:, 0] + b_fit_rg, '-', color='red', label='Fit: {:.3f}x + {:.3f}'.format(a_fit_rg, b_fit_rg))

u = b_fit_rg / 2

plt.legend()
plt.xlabel('Log(Step)')
plt.ylabel('Log(<R^2_g>)')
plt.title(r'$\langle R^2_g \rangle$ vs Step for Traditional Random Walk')
plt.grid(True)
plt.show()

print(f'Rg2SAW[50] / d2meanSAW[50]: {rg2_saw(50) / d2mean_saw(50)}')
