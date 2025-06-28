import numpy as np
import matplotlib.pyplot as plt


f = open("magnetization_data.txt")
Lines = f.readlines()
T,J = [],[]

for i in Lines:
    try:
        T.append(float(i.split()[0]))
        J.append(float(i.split()[1]))
    except:
        print(i)
        
f.close()

plt.plot(T,J)
plt.title("3D ising model MC simulations")
plt.xlabel("T/J")
plt.ylabel("m")
plt.savefig("P5-m.jpg")
plt.cla()

J = [-i for i in J]
plt.plot(T,J)
plt.title("3D ising model MC simulations")
plt.xlabel("T/J")
plt.ylabel("m")
plt.savefig("P5-m-new.jpg")
