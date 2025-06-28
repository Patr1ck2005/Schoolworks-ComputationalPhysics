import time
import numpy as np
from math import pi, gamma

def true_ball_volume(n):
    return pi**(n/2) / gamma(n/2 + 1)

def mc_volume_importance(n, num_samples, sigma):
    """
    Importance sampling estimate of the volume of the unit n-ball.
    Proposal: x ~ N(0, σ^2 I_n).
    """
    X = np.random.normal(loc=0, scale=sigma, size=(num_samples, n))
    r2 = np.sum(X**2, axis=1)
    inside = (r2 <= 1.0).astype(float)
    # log q(x) = -0.5 * n * log(2πσ²) - 0.5 * ||x||² / σ²
    log_q = -0.5 * n * np.log(2*pi*sigma**2) - 0.5 * r2/(sigma**2)
    w = inside * np.exp(-log_q)  # = inside / q(x)
    return np.mean(w)

if __name__ == "__main__":
    n = 50
    true_vol = true_ball_volume(n)
    sigmas = [0.1 * 1/np.sqrt(n), 1/np.sqrt(n), 0.5, 1.0]
    num_samples = 200_000

    # 记录脚本开始时间
    t_start_all = time.perf_counter()

    for sigma in sigmas:
        # 记录单次调用开始时间
        t0 = time.perf_counter()
        est = mc_volume_importance(n, num_samples=num_samples, sigma=sigma)
        t1 = time.perf_counter()

        err = abs(est - true_vol) / true_vol
        print(f"σ={sigma:.3f} 估计={est:.3e}, 真实={true_vol:.3e}, 相对误差={err:.3%} "
              f"(用时 {t1 - t0:.3f} 秒)")

    # 记录脚本结束时间
    t_end_all = time.perf_counter()
    print(f"\n脚本总运行时间：{t_end_all - t_start_all:.3f} 秒")
