import numpy as np

unit_roundoff_half = np.finfo(np.float16).eps
unit_roundoff_single = np.finfo(np.float32).eps
unit_roundoff_double = np.finfo(np.float64).eps

half_min = np.finfo(np.float16).tiny

print("半精度数据类型的最小精度:", half_min)

print("Half Precision Unit Roundoff:", unit_roundoff_half)
print("Single Precision Unit Roundoff:", unit_roundoff_single)
print("Double Precision Unit Roundoff:", unit_roundoff_double)