import time
from decimal import Decimal, getcontext


def bs(a, b):
    """
    利用二分法递归计算 P(a,b), Q(a,b) 和 T(a,b)
    其中：
      P: 累乘部分
      Q: 幂次部分
      T: 累加部分（含符号）
    """
    if b - a == 1:
        if a == 0:
            P = 1
            Q = 1
        else:
            # 根据公式：P(a) = (6a-5)*(2a-1)*(6a-1)
            P = (6 * a - 5) * (2 * a - 1) * (6 * a - 1)
            # Q(a) = a^3 * (640320)^3
            Q = a * a * a * 640320 ** 3
        # T(a) = P(a) * (13591409 + 545140134*a)，奇数项取负
        T = P * (13591409 + 545140134 * a)
        if a & 1:
            T = -T
        return (P, Q, T)
    else:
        m = (a + b) // 2
        P1, Q1, T1 = bs(a, m)
        P2, Q2, T2 = bs(m, b)
        P = P1 * P2
        Q = Q1 * Q2
        T = T1 * Q2 + P1 * T2
        return (P, Q, T)


def compute_pi_chudnovsky(digits):
    # 根据 Chudnovsky 公式，每一项大约贡献 14 位有效数字
    n_terms = digits // 14 + 1
    P, Q, T = bs(0, n_terms)

    # 设置 Decimal 模块的精度，额外增加一些防止中间误差
    getcontext().prec = digits + 10
    # 计算常数 C = 426880 * sqrt(10005)
    sqrt10005 = Decimal(10005).sqrt()
    C = Decimal(426880) * sqrt10005
    # π = (C * Q) / T
    pi = C * Decimal(Q) / Decimal(T)
    return +pi  # 应用当前精度


if __name__ == '__main__':
    digits = int(input("请输入想要计算的位数："))
    start_time = time.time()
    pi_value = compute_pi_chudnovsky(digits)
    end_time = time.time()

    print("计算得到的圆周率为：")
    print(str(pi_value))
    print("计算耗时：{:.6f}秒".format(end_time - start_time))
