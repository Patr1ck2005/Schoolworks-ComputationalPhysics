import random
import numpy as np
import matplotlib.pyplot as plt

# 设定步长
step = 1
# 设定不同的步数进行模拟
total_steps = [512]
# 每个步数模拟的次数
size = 100000

# 随机行走函数
def random_walk(steps):
    position = 0
    for _ in range(steps):
        position += step * random.choice([-1, 1])
    return position

# 计算随机行走的频率分布
def calculate_distribution(steps, trials):
    distribution = np.zeros(2 * steps + 1)
    for _ in range(trials):
        final_position = total_steps + random_walk(steps)
        distribution[final_position] += 1
    return distribution / trials

# 绘制频率分布图像
for steps in total_steps:
    t = np.arange(-steps, steps + 1)
    plt.plot(t, calculate_distribution(steps, size))
    plt.xlabel('Position')
    plt.ylabel('Probability')
    plt.title(f'Random Walk Distribution for {steps} steps')
    plt.show()
