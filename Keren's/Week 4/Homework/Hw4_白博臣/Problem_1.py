from sympy import symbols, Eq, solve
import numpy as np

# 定义符号变量
x = symbols('x')
# 给定b的值
b = eval(input('请给定b的值：'))
# 定义方程
equation = Eq(x ** 2 - b * x + 1, 0)

# 求解方程得到符号解
symbolic_solution = solve(equation, x)[0]

# 使用公式法求解得到数值解
r = np.sqrt(b ** 2 - 4)
x_1 = (b + r) / 2
x_2 = (b - r) / 2
numerical_solution = x_2

# 计算误差
absolute_error = abs(symbolic_solution.evalf() - numerical_solution)
percent_error = abs(absolute_error / symbolic_solution.evalf() * 100)

print("符号解：", symbolic_solution.evalf())
print("数值解：", numerical_solution)
print("绝对误差：", absolute_error)
print("误差百分比：", percent_error, "%")
print('-------------------------------分割线---------------------------------')

# 改进方法后
x_2_new = 2 / (b + r)
numerical_solution = x_2_new
absolute_error = abs(symbolic_solution.evalf() - numerical_solution)
percent_error = abs(absolute_error / symbolic_solution.evalf() * 100)

print("符号解：", symbolic_solution.evalf())
print("数值解：", numerical_solution)
print("绝对误差：", absolute_error)
print("误差百分比：", percent_error, "%")
