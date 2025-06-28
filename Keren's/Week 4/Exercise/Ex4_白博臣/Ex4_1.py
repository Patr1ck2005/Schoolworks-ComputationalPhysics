import numpy as np
from sympy import symbols, Eq, solve

# 定义符号变量
x_sym = symbols('x')
a = np.float32(1.22)
b = np.float32(3.34)
c = np.float32(2.28)

# 定义方程
equation = Eq(a * x_sym ** 2 + b * x_sym + c, 0)

# 符号解
symbolic_solution = solve(equation, x_sym)
symbolic_solution_1 = symbolic_solution[0]
symbolic_solution_2 = symbolic_solution[1]
print("Symbolic solutions:", symbolic_solution_1, symbolic_solution_2)

# 数值解
# numerical_solution = np.roots([a, b, c])
# print("Numerical solutions:", numerical_solution)
# 计算判别式
r = np.float32(np.sqrt(np.float32(b ** 2.0) - np.float32(4.0 * a * c)))

# 计算数值解
x_1 = (-b + r) / (2.0 * a)
x_2 = (-b - r) / (2.0 * a)

numerical_solution_1 = np.float32(x_2)
numerical_solution_2 = np.float32(x_1)

print("Numerical solutions:", numerical_solution_1, numerical_solution_2)

# 对比误差
cancellation_error_1 = abs(symbolic_solution_1 - numerical_solution_1) / abs(symbolic_solution_1)
cancellation_error_2 = abs(symbolic_solution_2 - numerical_solution_2) / abs(symbolic_solution_2)
print('两个根的计算相对误差：', cancellation_error_1 * 100, cancellation_error_2 * 100)
