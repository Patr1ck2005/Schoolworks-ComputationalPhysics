# algorithm.py
import numpy as np
from numba import njit, prange


# 使用内联函数定义 f(z) 和 f'(z)，加速计算
@njit(inline='always')
def f(z):
    return z ** 3 - 1


@njit(inline='always')
def df(z):
    return 3 * z ** 2


# 三个已知的根
ROOTS = np.array([1.0 + 0.0j,
                  -0.5 + 0.86602540378j,
                  -0.5 - 0.86602540378j])


@njit(parallel=True)
def compute_newton_fractal_jit(xmin, xmax, ymin, ymax, width, height, tol, max_iter):
    """
    利用 numba 并行加速，逐像素计算牛顿迭代。
    返回：
      root_index: 每个像素收敛的根编号（-1 表示未收敛）
      iterations: 每个像素迭代的次数
    """
    # 初始化返回数组，注意数组尺寸为 (height, width)
    root_index = -np.ones((height, width), dtype=np.int32)
    iterations = np.zeros((height, width), dtype=np.int32)

    dx = (xmax - xmin) / (width - 1)
    dy = (ymax - ymin) / (height - 1)

    # 定义三个根，方便后续比较
    roots = np.empty(3, dtype=np.complex128)
    roots[0] = 1.0 + 0.0j
    roots[1] = -0.5 + 0.86602540378j
    roots[2] = -0.5 - 0.86602540378j

    # 并行遍历每个像素
    for i in prange(height):
        imag_part = ymin + i * dy
        for j in range(width):
            real_part = xmin + j * dx
            z = complex(real_part, imag_part)
            iters = 0
            # 迭代牛顿方法
            while iters < max_iter and abs(f(z)) > tol:
                z = z - f(z) / df(z)
                iters += 1
            iterations[i, j] = iters
            # 检查 z 是否收敛到某个根
            for k in range(3):
                if abs(z - roots[k]) < tol:
                    root_index[i, j] = k
                    break
    return root_index, iterations


def compute_newton_fractal(xmin, xmax, ymin, ymax, width, height, tol=1e-4, max_iter=50):
    """
    包装函数，调用 numba 加速版本进行计算
    """
    return compute_newton_fractal_jit(xmin, xmax, ymin, ymax, width, height, tol, max_iter)
