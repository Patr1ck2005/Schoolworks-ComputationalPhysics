import time
import gmpy2
from gmpy2 import mpfr, sqrt, get_context, mpz
import matplotlib.pyplot as plt

# 尝试设置 seaborn 风格，否则回退到默认风格
try:
    plt.style.use('seaborn-darkgrid')
except OSError:
    plt.style.use('default')

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体（如系统中未安装 SimHei，请更换）
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号

def bs(a, b):
    """
    利用二分法求和，返回三元组 (P, Q, T)
    对应公式中：
      P(a,b) = ∏[k=a, b-1] (6k-5)(2k-1)(6k-1)
      Q(a,b) = ∏[k=a, b-1] k³·640320³
      T(a,b) = ∑[k=a, b-1] (-1)^k * P(a,k) * (13591409+545140134*k)
    """
    if b - a == 1:
        if a == 0:
            P = mpz(1)
            Q = mpz(1)
            T = mpz(13591409)
        else:
            P = mpz((6 * a - 5) * (2 * a - 1) * (6 * a - 1))
            Q = mpz(a)**3 * mpz(640320)**3
            T = P * mpz(13591409 + 545140134 * a)
            if a & 1:  # 奇数项变号
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

def compute_pi(digits):
    """
    利用 Chudnovsky 公式的二分法优化计算圆周率
    :param digits: 十进制有效位数
    :return: 计算出的 π 值（mpfr 类型）
    """
    extra = 10
    bits = int((digits + extra) * 3.32193) + 1
    get_context().precision = bits

    # 每项大约贡献 14 位有效数字
    nterms = digits // 14 + 1

    P, Q, T = bs(0, nterms)
    # 根据公式：π = (426880 * sqrt(10005) * Q) / T
    pi = (mpfr(426880) * sqrt(mpfr(10005)) * mpfr(Q)) / mpfr(T)
    return pi

def compute_time(digits, threshold=0.01, repeats=10):
    """
    测量计算指定位数 π 的时间，如果时间太短，则多次重复计算取平均值
    """
    start = time.time()
    compute_pi(digits)
    elapsed = time.time() - start
    if elapsed < threshold:
        start = time.time()
        for _ in range(repeats):
            compute_pi(digits)
        elapsed = (time.time() - start) / repeats
    return elapsed

def benchmark():
    """
    对不同位数的 π 计算进行基准测试，并绘制图形展示计算时间变化
    """
    digit_list = [100, 500, 1000, 2000, 3000, 4000, 5000, 10000, 20000, 100000]
    times = []

    for digits in digit_list:
        print(f"正在计算 {digits} 位圆周率...")
        elapsed = compute_time(digits)
        times.append(elapsed)
        print(f"位数：{digits}，计算时间：{elapsed:.6f} 秒")

    # 绘制测试图
    plt.figure(figsize=(10, 6))
    plt.plot(digit_list, times, marker='o', linestyle='-', color='#1f77b4', linewidth=2, markersize=8)
    plt.xlabel("十进制位数", fontsize=14)
    plt.ylabel("计算时间（秒）", fontsize=14)
    plt.title("π 计算基准测试", fontsize=16)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    for i, t in enumerate(times):
        plt.text(digit_list[i], t, f"{t:.3f}", ha='center', va='bottom', fontsize=12)
    plt.tight_layout()
    plt.show()

def main():
    user_input = input("请输入需要计算的圆周率位数（例如1000），或输入 'benchmark' 运行基准测试：").strip()
    if user_input.lower() == "benchmark":
        benchmark()
    else:
        try:
            digits = int(user_input)
        except ValueError:
            print("输入无效，请输入一个整数或 'benchmark'。")
            return

        start = time.time()
        pi_val = compute_pi(digits)
        elapsed = time.time() - start

        # 转换为字符串，截取有效位数（含 "3." 两位）
        pi_str = str(pi_val)
        result = pi_str[:digits+2]
        print("圆周率：")
        print(result)
        print("计算时间：{:.6f} 秒".format(elapsed))

if __name__ == '__main__':
    main()
