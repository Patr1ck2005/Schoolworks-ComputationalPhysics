import numpy as np
import matplotlib.pyplot as plt

from scipy.ndimage import convolve, generate_binary_structure

plt.rc('font',family='Times New Roman')
plt.rc('figure', figsize=(10, 5))
plt.rcParams['axes.grid']=True


# 50 by 50 grid
N = 30

init_random = np.random.random((N,N))

lattice = np.zeros((N, N))
lattice[init_random>=0.5] = 1
lattice[init_random<0.5] = -1
plt.imshow(lattice)
plt.show()