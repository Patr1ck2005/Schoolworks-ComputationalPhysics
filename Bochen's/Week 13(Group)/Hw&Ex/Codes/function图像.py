import numpy as np
import matplotlib.pyplot as plt

# 生成区间 (0, 1) 内的 x 值
x = np.linspace(0.01, 1, 100)  # 从 0.01 开始以避免 x=0 处的无穷值

# 计算对应的 y 值
y = 1 / (np.sqrt(x) + x)

# 绘制图像
plt.figure(figsize=(8, 6))

# 绘制函数曲线
plt.plot(x, y)

# 填充函数下方的阴影
plt.fill_between(x, y, color='skyblue', alpha=0.4)

# 添加标题和标签
plt.title('Function')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

plt.savefig(r'D:\FileArchiving\大二下\计算物理\瞎写的python\Week13\文档\function2.eps')
# 显示图像
plt.show()
