import numpy as np


def simpson_integral(alpha: float,
                     a: float = -1.0,
                     b: float = 1.0,
                     M: int = 2001) -> float:
    """
    复合 Simpson 法 ∫_a^b (1 - x^2)^alpha dx
    M 必须是奇数，用于切分区间。
    """
    if M % 2 == 0:
        raise ValueError("M (分点数) 必须是奇数")
    h = (b - a) / (M - 1)
    x = a + h * np.arange(M)
    y = (1 - x * x) ** alpha
    S = y[0] + y[-1] \
        + 4.0 * np.sum(y[1:-1:2]) \
        + 2.0 * np.sum(y[2:-2:2])
    return S * h / 3.0


def volume_numeric(n: int,
                   M: int = 2001) -> float:
    """
    递推+复合 Simpson 估计单位 n 维球体积。

    参数
    ----
    n : int
        维度，n>=0
    M : int
        Simpson 切分点数，必须为奇数，越大精度越高（推荐 1001~5001）

    返回
    ----
    float
        估计的 V_n
    """
    if n < 0 or not isinstance(n, int):
        raise ValueError("n 必须是非负整数")
    V = 1.0  # V_0 = 1
    if n >= 1:
        V = 2.0  # V_1 = 2
    # 从 2 维开始递推
    for k in range(2, n + 1):
        alpha = (k - 1) / 2.0
        I = simpson_integral(alpha, M=M)
        V *= I
    return V


if __name__ == "__main__":
    # 试算 0~30 维
    for dim in [0, 1, 2, 5, 10, 20, 300]:
        vol = volume_numeric(dim, M=2001)
        print(f"{dim:2d} 维 → V ≈ {vol:.6e}")
