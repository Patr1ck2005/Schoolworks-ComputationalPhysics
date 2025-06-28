import numpy as np
from mpmath import mp


def taylor_exp_single(x, n_terms=10):
    result_single = np.float32(1.0)
    term_single = np.float32(1.0)
    for i in range(1, n_terms):
        term_single = term_single * x / i
        result_single = np.float32(result_single + term_single)
    return result_single


def taylor_exp_double(x, n_terms=10):
    result_double = np.float64(1.0)
    term_double = np.float64(1.0)
    for i in range(1, n_terms):
        term_double = term_double * x / i
        result_double = np.float64(result_double + term_double)
    return result_double


def taylor_exp_quad(x, n_terms=10):
    mp.dps = 36
    result_quad = mp.mpf('1.0')
    term_quad = mp.mpf('1.0')
    for i in range(1, n_terms):
        term_quad = term_quad * x / i
        result_quad = result_quad + term_quad
    return result_quad


x = 2.0
n_terms = 20

result_single = taylor_exp_single(x, n_terms)
result_double = taylor_exp_double(x, n_terms)
result_quad = taylor_exp_quad(mp.mpf(str(x)), n_terms)

print(f"x=2,Single precision result (float): {result_single}")
print(f"x=2,Double precision result (double): {result_double}")
print(f"x=2,Quadruple precision result: {result_quad}")

x = 10.0
n_terms = 20

result_single = taylor_exp_single(x, n_terms)
result_double = taylor_exp_double(x, n_terms)
result_quad = taylor_exp_quad(mp.mpf(str(x)), n_terms)

print(f"x=10,Single precision result (float): {result_single}")
print(f"x=10,Double precision result (double): {result_double}")
print(f"x=10,Quadruple precision result: {result_quad}")
x = -2.0
n_terms = 20

result_single = taylor_exp_single(x, n_terms)
result_double = taylor_exp_double(x, n_terms)
result_quad = taylor_exp_quad(mp.mpf(str(x)), n_terms)
print(f"x=-2,Single precision result (float): {result_single}")
print(f"x=-2,Double precision result (double): {result_double}")
print(f"x=-2,Quadruple precision result: {result_quad}")

x = -10.0
n_terms = 1000

result_single = taylor_exp_single(x, n_terms)
result_double = taylor_exp_double(x, n_terms)
result_quad = taylor_exp_quad(mp.mpf(str(x)), n_terms)
print(f"x=-10,Single precision result (float): {result_single}")
print(f"x=-10,Double precision result (double): {result_double}")
print(f"x=-10,Quadruple precision result: {result_quad}")
