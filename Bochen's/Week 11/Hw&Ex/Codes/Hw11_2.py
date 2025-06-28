import numpy as np
import matplotlib.pyplot as plt


def estimate_pi(num_samples):
    num_inside = 0
    for _ in range(num_samples):
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        if x ** 2 + y ** 2 < 1:
            num_inside += 1
    pi_estimate = 4 * num_inside / num_samples
    return pi_estimate


# 参数设置
num_samples = 100000

# 估算 pi
pi_value = estimate_pi(num_samples)
print(f"Estimated value of pi: {pi_value}")

# 可视化结果
fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')
theta = np.linspace(0, np.pi / 2, 100)
x_arc = np.cos(theta)
y_arc = np.sin(theta)
ax.plot(x_arc, y_arc, 'b', linewidth=2)

# 生成随机点并绘制
x_rand = np.random.uniform(0, 1, num_samples)
y_rand = np.random.uniform(0, 1, num_samples)
dist = np.sqrt(x_rand ** 2 + y_rand ** 2)
x_inside = x_rand[dist < 1]
y_inside = y_rand[dist < 1]
x_outside = x_rand[dist >= 1]
y_outside = y_rand[dist >= 1]

ax.scatter(x_inside, y_inside, color='g', marker='.')
ax.scatter(x_outside, y_outside, color='r', marker='.')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_title(f'Estimation of Pi: {pi_value:.6f}')
plt.show()
