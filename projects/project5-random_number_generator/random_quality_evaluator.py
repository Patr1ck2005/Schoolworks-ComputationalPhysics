#!/usr/bin/env python3
"""
random_quality_evaluator.py

全方位评估指定二进制随机数文件质量，各项测试结果在控制台输出。
依赖：numpy, scipy
"""

import numpy as np
from scipy.stats import chi2, norm
from numpy.fft import fft

# ========== 参数设置（硬编码） ==========
INPUT_FILE = "random.bin"   # 要评估的随机数二进制文件路径
BLOCK_SIZE = 128            # 块频率检验时使用的块大小 M
RUN_LAG = 1                 # 自相关检验时使用的滞后值 lag
APEN_M = 2                  # 近似熵检验时的 m 值

# ========== 辅助函数 ==========
def read_bits(filename):
    """从二进制文件读取并转为比特流（一维 0/1 数组）。"""
    data = np.fromfile(filename, dtype=np.uint8)
    return np.unpackbits(data)

def bits_to_signed(bits):
    # 先 cast 再映射：0→-1，1→+1
    return bits.astype(np.int8) * 2 - 1

def monobit_test(bits):
    """比特频率检验（Monobit Test）"""
    signed = bits_to_signed(bits)
    n = len(signed)
    s = signed.sum()
    s_obs = abs(s) / np.sqrt(n)
    return 2 * (1 - norm.cdf(s_obs))

def block_frequency_test(bits, M):
    """块频率检验（Block Frequency Test）"""
    n = len(bits)
    N = n // M
    if N == 0:
        return None
    props = [np.sum(bits[i*M:(i+1)*M]) / M for i in range(N)]
    chi_sq = 4 * M * sum((p - 0.5)**2 for p in props)
    return chi2.sf(chi_sq, df=N)

def runs_test(bits):
    """游程检验（Runs Test）"""
    n = len(bits)
    pi = np.mean(bits)
    if abs(pi - 0.5) > 2/np.sqrt(n):
        return 0.0
    Vn = 1 + sum(bits[i] != bits[i-1] for i in range(1, n))
    num = abs(Vn - 2*n*pi*(1-pi))
    den = 2*np.sqrt(2*n)*pi*(1-pi)
    return 2 * (1 - norm.cdf(num/den))

def autocorrelation_test(bits, lag):
    """自相关检验（Autocorrelation Test）"""
    n = len(bits)
    b0, b1 = bits[:-lag], bits[lag:]
    corr = np.corrcoef(b0, b1)[0,1]
    z = corr * np.sqrt(n - lag) / np.sqrt(1 - corr**2)
    p = 2 * (1 - norm.cdf(abs(z)))
    return p, corr

def spectral_test(bits):
    """离散傅里叶谱检验（Spectral Test）"""
    seq = bits_to_signed(bits)
    S = np.abs(fft(seq))
    N = len(S)
    T = np.sqrt(np.log(1 / 0.05) * N)

    # 原始代码用全谱：count = np.sum(S < T)
    # NIST 标准只看正频率区间、排除直流分量：
    half = N // 2
    # 排除 S[0]（直流），只统计 k=1..half-1
    count = np.sum(S[1:half] < T)

    expected = 0.95 * (half - 1)
    sigma = np.sqrt((half - 1) * 0.95 * 0.05)
    z = (count - expected) / sigma

    # 同样用 sf 保持小尾部数值
    p = 2 * norm.sf(abs(z))
    return p, count, expected

def approximate_entropy_test(bits, m):
    """近似熵检验（Approximate Entropy Test）"""
    n = len(bits)
    def phi(m_):
        patterns = [bits[i:i+m_] for i in range(n - m_ + 1)]
        cnt = {}
        for pat in patterns:
            key = ''.join(pat.astype(str))
            cnt[key] = cnt.get(key, 0) + 1
        return sum(v * np.log(v/(n-m_+1)) for v in cnt.values()) / (n-m_+1)
    phi_m   = phi(m)
    phi_m1  = phi(m+1)
    ApEn    = phi_m - phi_m1
    chi_sq  = 2*n*(np.log(2) - ApEn)
    p       = chi2.sf(chi_sq/2, df=2**(m-1))
    return p, ApEn

# ========== 主流程 ==========
bits = read_bits(INPUT_FILE)
print(f"评估文件: {INPUT_FILE}")
print(f"总比特数: {len(bits)}\n")

results = [
    ("Monobit Test",                     monobit_test(bits)),
    ("Block Frequency Test",             block_frequency_test(bits, BLOCK_SIZE)),
    ("Runs Test",                        runs_test(bits)),
    ("Autocorrelation Test (lag=1)",     autocorrelation_test(bits, RUN_LAG)),
    ("Spectral Test",                    spectral_test(bits)),
    ("Approximate Entropy Test (m=2)",   approximate_entropy_test(bits, APEN_M)),
]

for name, res in results:
    if isinstance(res, tuple):
        print(f"{name}: {res}")
    else:
        print(f"{name}: p-value = {res}")
