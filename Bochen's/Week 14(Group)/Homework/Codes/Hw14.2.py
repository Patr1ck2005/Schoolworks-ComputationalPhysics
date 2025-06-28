import math
import random


class Polymer:
    """ A class representing a random-flight polymer in solution. """

    def __init__(self, N, a):
        """
        Initialize a Polymer object with N segments, each of length a.

        """

        # save N and a to self.N, self.a
        self.N, self.a = N, a
        # self.xyz holds the segment position vectors as tuples
        self.xyz = [(None, None, None)] * N
        # End-to-end vector
        self.R = None
        # Make our polymer by assigning segment positions
        self.make_polymer()

    def make_polymer(self):
        """
        Calculate the segment positions, centre of mass and end-to-end
        distance for a random-flight polymer.

        """

        # Start our polymer off at the origin, (0,0,0).
        self.xyz[0] = x, y, z = cx, cy, cz = 0., 0., 0.
        for i in range(1, self.N):
            # Pick a random orientation for the next segment.
            theta = math.acos(2 * random.random() - 1)
            phi = random.random() * 2. * math.pi
            # Add on the corresponding displacement vector for this segment.
            x += self.a * math.sin(theta) * math.cos(phi)
            y += self.a * math.sin(theta) * math.sin(phi)
            z += self.a * math.cos(theta)
            # Store it, and update or centre of mass sum.
            self.xyz[i] = x, y, z
            cx, cy, cz = cx + x, cy + y, cz + z
        # Calculate the position of the centre of mass.
        cx, cy, cz = cx / self.N, cy / self.N, cz / self.N
        # The end-to-end vector is the position of the last
        # segment, since we started at the origin.
        self.R = x, y, z

        # Finally, re-centre our polymer on the centre of mass.
        for i in range(self.N):
            self.xyz[i] = self.xyz[i][0] - cx, self.xyz[i][1] - cy, self.xyz[i][2] - cz

    def calc_Rg(self):
        """
        Calculates and returns the radius of gyration, Rg. The polymer
        segment positions are already given relative to the centre of
        mass, so this is just the rms position of the segments.

        """

        self.Rg = 0.
        for x, y, z in self.xyz:
            self.Rg += x ** 2 + y ** 2 + z ** 2
        self.Rg = math.sqrt(self.Rg / self.N)
        return self.Rg


import polymer.Polymer

polymer1 = Polymer(1000, 0.5)  # A polymer with 1000 segments of length 0.5
polymer1.R  # End-to-end vector
polymer1.calc_Rg()  # Radius of gyration

import numpy as np
import matplotlib.pyplot as plt
import polymer.Polymer

pi = np.pi

# Calculate R for Np polymers
Np = 3000
# Each polymer consists of N segments of length a
N, a = 1000, 1.
R = [None] * Np
for i in range(Np):
    polymer = Polymer(N, a)
    Rx, Ry, Rz = polymer.R
    R[i] = np.sqrt(Rx ** 2 + Ry ** 2 + Rz ** 2)
    # Output a progress indicator every 100 polymers
    if not (i + 1) % 100:
        print(i + 1)

# Plot the distribution of Rx as a normalized histogram
# using 50 bins
plt.hist(R, 50, density=True)

# Plot the theoretical probability distribution, Pr, as a function of r
r = np.linspace(0, 200, 1000)
msr = N * a ** 2
Pr = 4. * pi * r ** 2 * (2 * pi * msr / 3) ** -1.5 * np.exp(-3 * r ** 2 / 2 / msr)
plt.plot(r, Pr, lw=2, c='r')
plt.xlabel('R')
plt.ylabel('P(R)')
plt.show()
