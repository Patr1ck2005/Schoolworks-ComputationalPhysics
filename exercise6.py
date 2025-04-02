import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

# 定义原始数据
years = np.array([1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990])
population = np.array([106.46, 123.08, 132.12, 152.27, 180.67, 205.05, 227.23, 249.46])

normed_x = years-1920

# 使用七次多项式拟合
degree = 7
coeffs = np.polyfit(normed_x, population, degree)
poly = np.poly1d(coeffs)

# 打印拟合函数
print("七次多项式拟合函数:")
print(poly)

# 预测2000年和2020年的人口数据
pop_2000_pred = poly(2000-1920)
pop_2020_pred = poly(2020-1920)
print(f"\n外推预测: 2000年人口 = {pop_2000_pred:.2f} 百万")
print(f"外推预测: 2020年人口 = {pop_2020_pred:.2f} 百万")

# 构造更细的年份数组用于画曲线
years_fine = np.linspace(1920, 2030, 400)
population_fine = poly(years_fine-1920)

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(years_fine, population_fine, label=f'{degree}次多项式拟合曲线', color='blue')
plt.scatter(years, population, color='red', label='原始数据')
plt.scatter([2000, 2020], [pop_2000_pred, pop_2020_pred], color='green', zorder=5, label='外推点')
plt.scatter([2000,], [281.42,], color='red', zorder=5, label='原始数据')
plt.axvspan(1920, 1990, label='拟合区域', zorder=0, alpha=0.1, color='purple')

plt.title("1920-1990年美国人口数据与七次多项式拟合外推")
plt.xlabel("年份")
plt.ylabel("人口 (百万)")
plt.legend()
plt.grid(True)
plt.savefig('ex6-1.png', dpi=300)
# plt.show()

plt.xlim(1920, 2010)
plt.ylim(0, 300)
plt.savefig('ex6-2.png', dpi=300)
plt.show()

# 对外推合理性的讨论：
print("\n讨论：")
print("使用七次多项式对已有数据进行拟合可以较好地通过已有数据点，但多项式拟合在数据区间外的外推往往不可靠。"
      "在此案例中,这是由于7次多项式对于数据'过拟合'了.")
print("例如，对于2020年的预测，由于多项式高次项引起的振荡效应，外推结果完全偏离实际情况。")
