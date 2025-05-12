import numpy as np
import mpmath as mp

# ---- 配置高精度 ----
mp.mp.dps = 50  # 设置 50 位有效数字


class SimpsonIntegrator:
    def __init__(self, a: float = -1.0, b: float = 1.0, M: int = 2001):
        if M % 2 == 0:
            raise ValueError("M (number of points) must be odd")
        self.M = M
        self.a = a
        self.b = b
        self.h = (b - a) / (M - 1)
        # 均匀节点
        self.x = a + self.h * np.arange(M)
        # Simpson 权重 1,4,2,...,4,1 并缩放 h/3
        w = np.ones(M)
        w[1:-1:2] = 4
        w[2:-2:2] = 2
        self.w_scaled = w * (self.h / 3.0)

    def integrate(self, alpha: float) -> float:
        """
        计算 ∫_{a}^{b} (1 - x^2)^alpha dx
        返回普通浮点结果，用于后续对数累加
        """
        return np.dot(self.w_scaled, (1 - self.x ** 2) ** alpha)


def volume_numeric_highprec(n: int, integrator: SimpsonIntegrator) -> mp.mpf:
    """
    使用 mpmath 高精度计算 n 维单位球体积，避免浮点下溢。
    返回 mp.mpf 类型的体积值。
    """
    if n < 0 or not isinstance(n, int):
        raise ValueError("n must be a non-negative integer")

    # 初始化 logV = log(V_n)
    logV = mp.mpf(0)  # V_0 = 1
    if n >= 1:
        logV = mp.log(mp.mpf(2))  # V_1 = 2

    # 递推累加每步积分的对数
    for k in range(2, n + 1):
        alpha = (k - 1) / 2.0
        Ik = integrator.integrate(alpha)
        logV += mp.log(mp.mpf(Ik))

    # 返回体积
    return mp.e ** logV


if __name__ == "__main__":
    # 预构造 SimpsonIntegrator（可调整 M 获得更高精度）
    M = 2001
    integrator = SimpsonIntegrator(M=M)

    # 计算 500 维球体积
    n = 500
    V500 = volume_numeric_highprec(n, integrator)
    print(f"{n} 维球体积 ≈ {mp.nstr(V500, 10)}")
