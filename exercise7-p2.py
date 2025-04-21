#!/usr/bin/env python3
"""
利用二次样条插值求解火箭运动问题：
  (a) 在 t=16 秒时的速度
  (b) 在 t=16 秒时的加速度
  (c) 从 t=11 秒到 t=16 秒间的飞行距离

数据点：
    t: 0, 10, 15, 20, 22.5, 30  (seconds)
    v: 0, 227.04, 362.78, 517.35, 602.97, 901.67  (m/s)

二次样条分段形式：
    S_i(t) = a_i + b_i*(t - t_i) + c_i*(t - t_i)^2,  t in [t_i, t_{i+1}]
要求：
    S_i(t_i) = v_i,  S_i(t_{i+1}) = v_{i+1}
    各内节点处 S_i'(t_{i+1}) = S_{i+1}'(t_{i+1})
附加条件：设第一个区间二次项系数 c_0 = 0
"""


def build_quadratic_spline(t, v):
    """
    构造分段二次样条插值系数

    参数:
      t: 时间数据列表 (长度 n+1)
      v: 对应的速度数据列表 (长度 n+1)

    返回:
      a, b, c: 长度为 n 的列表, 其中每个区间 [t[i], t[i+1]] 的插值多项式为
          S_i(t) = a[i] + b[i]*(t - t[i]) + c[i]*(t - t[i])**2
    """
    n = len(t) - 1
    a = [0.0] * n
    b = [0.0] * n
    c = [0.0] * n

    # a_i = v_i
    for i in range(n):
        a[i] = v[i]

    # h_i = t[i+1] - t[i]
    h = [t[i + 1] - t[i] for i in range(n)]

    # 采用附加条件：c[0] = 0
    c[0] = 0.0
    # 第一区间 b0
    b[0] = (v[1] - v[0] - c[0] * h[0] * h[0]) / h[0]

    # 递推计算 i=1,2,..., n-1 的 b 和 c
    for i in range(1, n):
        # 利用上一段末端一阶导数连续： b[i] = S_{i-1}'(t[i]) = b[i-1] + 2*c[i-1]*h[i-1]
        b[i] = b[i - 1] + 2 * c[i - 1] * h[i - 1]
        # 利用区间内插值条件： S_i(t[i+1]) = a[i] + b[i]*h[i] + c[i]*h[i]**2 = v[i+1]
        # 解得 c[i]:
        c[i] = (v[i + 1] - v[i] - b[i] * h[i]) / (h[i] * h[i])

    return a, b, c, h


def evaluate_spline(t, a, b, c, x):
    """
    计算给定 x 对应的二次样条插值值

    参数:
      t: 原数据点的时间列表
      a, b, c: 对应区间的系数列表
      x: 目标时间

    返回:
      S(x)
    """
    # 找到 x 落在哪个区间，假设数据有序
    n = len(t) - 1
    for i in range(n):
        if t[i] <= x <= t[i + 1]:
            dt = x - t[i]
            return a[i] + b[i] * dt + c[i] * dt * dt
    raise ValueError("x 不在数据区间内")


def evaluate_spline_derivative(t, b, c, x):
    """
    计算二次样条在 x 处的一阶导数

    参数:
      t: 时间数据列表
      b, c: 对应区间的系数（a 不参与导数）
      x: 目标时间

    返回:
      S'(x)
    """
    n = len(t) - 1
    for i in range(n):
        if t[i] <= x <= t[i + 1]:
            dt = x - t[i]
            return b[i] + 2 * c[i] * dt
    raise ValueError("x 不在数据区间内")


def integrate_spline_segment(a_i, b_i, c_i, dt0, dt1):
    """
    对单个分段多项式 S(t)= a_i + b_i*dt + c_i*dt^2 在 dt 从 dt0 到 dt1 内积分，
    其中 dt = t - t_i

    返回:
      积分值
    """
    # 不定积分为： a_i*dt + b_i/2 * dt^2 + c_i/3 * dt^3
    I_dt1 = a_i * dt1 + b_i / 2 * dt1 ** 2 + c_i / 3 * dt1 ** 3
    I_dt0 = a_i * dt0 + b_i / 2 * dt0 ** 2 + c_i / 3 * dt0 ** 3
    return I_dt1 - I_dt0


def integrate_spline(t, a, b, c, x0, x1):
    """
    对整个分段二次样条函数在区间 [x0, x1] 上积分
    x0 和 x1 可能落在不同的区间上
    """
    n = len(t) - 1
    total = 0.0
    # 确保 x0 < x1
    if x0 > x1:
        x0, x1 = x1, x0

    # 遍历各区间，累加积分值
    for i in range(n):
        # 当前区间为 [t[i], t[i+1]]
        # 若该区间与 [x0, x1] 没有交集，则跳过
        left = max(t[i], x0)
        right = min(t[i + 1], x1)
        if left < right:
            dt0 = left - t[i]
            dt1 = right - t[i]
            total += integrate_spline_segment(a[i], b[i], c[i], dt0, dt1)
    return total


def main():
    # 数据点
    t_points = [0.0, 10.0, 15.0, 20.0, 22.5, 30.0]
    v_points = [0.0, 227.04, 362.78, 517.35, 602.97, 901.67]

    # 构造二次样条，附加条件 c[0]=0
    a_coef, b_coef, c_coef, h = build_quadratic_spline(t_points, v_points)

    # (a) 计算 t = 16 秒处的速度（16 落在区间 [15,20], 即第3个区间, 索引 2）
    t_eval = 16.0
    velocity = evaluate_spline(t_points, a_coef, b_coef, c_coef, t_eval)

    # (b) 计算 t = 16 秒处的加速度
    acceleration = evaluate_spline_derivative(t_points, b_coef, c_coef, t_eval)

    # (c) 计算从 t = 11 到 t = 16 秒的位移
    # 注意：t = 11 落在区间 [10,15]（区间索引1），t = 16 落在区间 [15,20]（区间索引2）
    distance = integrate_spline(t_points, a_coef, b_coef, c_coef, 11.0, 16.0)

    # 输出结果
    print(f"(a) Velocity at t = {t_eval:.1f} s: {velocity:.4f} m/s")
    print(f"(b) Acceleration at t = {t_eval:.1f} s: {acceleration:.4f} m/s²")
    print(f"(c) Distance traveled from t = 11 s to t = 16 s: {distance:.4f} m")


if __name__ == "__main__":
    main()
