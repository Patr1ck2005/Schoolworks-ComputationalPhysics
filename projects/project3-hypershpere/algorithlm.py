import numpy as np
import math
import mpmath as mp

# ---- 配置 mpmath 精度 ----
mp.mp.dps = 50  # 有效位数设为 50 位

# ---- SimpsonIntegrator 同前 ----
class SimpsonIntegrator:
    def __init__(self, a=-1.0, b=1.0, M=2001):
        if M % 2 == 0:
            raise ValueError("M (number of points) must be odd")
        self.M = M
        self.a = a
        self.b = b
        self.h = (b - a) / (M - 1)
        self.x = a + self.h * np.arange(M)
        w = np.ones(M)
        w[1:-1:2] = 4
        w[2:-2:2] = 2
        self.w_scaled = w * (self.h / 3.0)

    def integrate(self, alpha: float) -> float:
        return np.dot(self.w_scaled, (1 - self.x**2)**alpha)

# ---- 数值递推体积 ----
def volume_numeric_optimized(n, integrator):
    if n < 0 or not isinstance(n, int):
        raise ValueError("n must be a non-negative integer")
    V = 1.0 if n == 0 else 2.0
    for k in range(2, n+1):
        alpha = (k - 1) / 2.0
        V *= integrator.integrate(alpha)
    return V

# ---- 高精度理论体积 ----
def volume_theoretical_mp(n):
    """
    使用 mpmath 完成 π^(n/2) / Γ(n/2 + 1) 的高精度计算
    """
    n2 = mp.mpf(n) / 2
    return mp.pi**n2 / mp.gamma(n2 + 1)

# ---- 主程序 ----
if __name__ == "__main__":
    M = 2001
    integrator = SimpsonIntegrator(M=M)

    dims = [0, 1, 2, 5, 10, 50, 100, 1000]
    for dim in dims:
        V_num = volume_numeric_optimized(dim, integrator)
        V_th_mp = volume_theoretical_mp(dim)
        # 转为高精度对象并计算相对误差
        V_num_mp = mp.mpf(V_num)
        rel_err = mp.nstr(abs(V_num_mp - V_th_mp) / V_th_mp, 5)
        print(f"{dim:4d}D → Numeric = {V_num:.6e}, Theoretical (mp) = {mp.nstr(V_th_mp,10)}, RelErr ≈ {rel_err}")
