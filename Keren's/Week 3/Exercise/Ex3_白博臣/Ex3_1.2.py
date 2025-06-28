import numpy as np
from mpmath import mp


def taylor_exp_single(x, n_terms=10):
    if x >= 0:
        result = np.float32(1.0)
        term = np.float32(1.0)
        for i in range(1, n_terms):
            term = term * x / i
            result = np.float32(result + term)
    else:
        result = np.float32(1.0) / taylor_exp_single(-x, n_terms)
    return result


def taylor_exp_double(x, n_terms=10):
    if x >= 0:
        result = np.float64(1.0)
        term = np.float64(1.0)
        for i in range(1, n_terms):
            term = term * x / i
            result = np.float64(result + term)
    else:
        result = np.float64(1.0) / taylor_exp_double(-x, n_terms)
    return result


def taylor_exp_quad(x, n_terms=10):
    if x >= 0:
        mp.dps = 30
        result = mp.mpf('1.0')
        term = mp.mpf('1.0')
        for i in range(1, n_terms):
            term = term * x / i
            result = result + term
    else:
        result = 1 / taylor_exp_quad(mp.mpf(str(-x)), n_terms)
    return result


test_values = [10, 2, -2, -10]
n_terms = 20

for x in test_values:
    result_single = taylor_exp_single(x, n_terms)
    result_double = taylor_exp_double(x, n_terms)
    result_quad = taylor_exp_quad(mp.mpf(str(x)), n_terms)

    print(f"x = {x}：")
    print(f"单精度结果 (float): {result_single}")
    print(f"双精度结果 (double): {result_double}")
    print(f"四倍精度结果: {result_quad}")
    print("-----------------------------")
