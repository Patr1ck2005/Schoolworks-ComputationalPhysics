import mpmath
import time


def compute_pi(digits):
    # 设置有效数字
    mpmath.mp.dps = digits
    # 获取 pi，并通过 nstr 强制将 pi 转换为字符串，从而完成计算
    pi_val = mpmath.pi
    return mpmath.nstr(pi_val, digits)


if __name__ == '__main__':
    n = int(input("请输入想要计算的位数："))
    start_time = time.time()
    pi_value = compute_pi(n)
    end_time = time.time()

    print("计算得到的圆周率为：")
    print(pi_value)
    print("计算耗时：{:.6f}秒".format(end_time - start_time))
