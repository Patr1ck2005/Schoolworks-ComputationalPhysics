#!/usr/bin/env python3
"""
计算火箭在 t=16 秒时的速度，数据来自线性样条插值法。
已知数据点：t=15秒时速度 v=362.78 m/s；t=20秒时速度 v=517.35 m/s。
"""


def linear_interpolation(t1, v1, t2, v2, t):
    """
    计算两个数据点 (t1, v1) 和 (t2, v2) 之间，给定时刻 t 的线性插值结果。

    参数:
        t1 (float): 第一个时间点
        v1 (float): 第一个时间点对应的速度
        t2 (float): 第二个时间点
        v2 (float): 第二个时间点对应的速度
        t (float): 目标时间

    返回:
        float: 在 t 时间点处估算的速度
    """
    slope = (v2 - v1) / (t2 - t1)
    return v1 + slope * (t - t1)


def main():
    # 已知数据点
    t1, v1 = 15.0, 362.78
    t2, v2 = 20.0, 517.35

    # 目标时间
    t_target = 16.0

    # 利用线性插值计算 t_target 处的速度
    v_target = linear_interpolation(t1, v1, t2, v2, t_target)

    # 输出结果，保留两位小数
    print(f"At t = {t_target:.1f} seconds, the estimated velocity is {v_target:.2f} m/s.")


if __name__ == "__main__":
    main()
