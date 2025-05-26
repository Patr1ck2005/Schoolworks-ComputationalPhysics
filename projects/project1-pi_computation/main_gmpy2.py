import time
import gmpy2
from gmpy2 import mpfr, sqrt, get_context, mpz

def compute_pi(digits):
    """
    利用 Chudnovsky 公式计算圆周率
    :param digits: 十进制精度，即需要计算的位数
    :return: 计算出的 π 值（mpfr 类型）
    """
    # 为了保证足够精度，转换为二进制位数，额外增加一些精度
    extra = 10
    bits = int((digits + extra) * 3.32193) + 1
    get_context().precision = bits

    # 常量 C = 426880 * sqrt(10005)
    C = mpfr(426880) * sqrt(mpfr(10005))

    # 初始化变量，以大整数进行运算
    M = mpz(1)
    L = mpz(13591409)
    X = mpz(1)
    S = mpfr(L)

    # 每项大约增加 14 位有效数字，估计需要的迭代次数
    nterms = digits // 14 + 1

    for k in range(1, nterms):
        numerator = (6 * k - 5) * (2 * k - 1) * (6 * k - 1)
        denominator = k**3 * (640320**3)
        M = M * numerator // denominator

        L += 545140134
        X *= -262537412640768000
        term = mpfr(M * L) / mpfr(X)
        S += term

    pi = C / S
    return pi

def main():
    try:
        user_input = input("请输入需要计算的圆周率位数（例如1000）：")
        digits = int(user_input)
    except ValueError:
        print("输入无效，请输入一个整数。")
        return

    t0 = time.time()
    pi_val = compute_pi(digits)
    t1 = time.time()

    # 将 pi_val 转换为字符串，包含小数点后的所有数字
    pi_str = str(pi_val)
    # 截取结果，保留 "3." 后面的 digits 位数字（总长度为 digits+2）
    result = pi_str[:digits+2]

    print("圆周率：")
    print(result)
    print("计算时间：{:.6f} 秒".format(t1 - t0))

if __name__ == '__main__':
    main()
