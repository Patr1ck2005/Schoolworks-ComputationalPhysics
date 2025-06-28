import sys
import time
# 增加整数字符串转换限制
sys.set_int_max_str_digits(10000000)

n = int(input('请输入圆周率小数点后的位数:'))
start_time = time.time()   # 计算pi计时起点
w = n + 10                 # 考虑精度，位数增加 k，结果减少 k 位
b = 10 ** w                # 用整数计算pi  如3.14 * 10^2 = 314
x1 = b * 4// 5             # 第一项前半部分
x2 = b // -239             # 第一项后半部分
sum = x1 + x2              # 第一项的值
n *= 2
for i in range(3, n, 2):
    x1 //= -25
    x2 //= -239*239
    x = (x1+x2)//i
    sum += x
mpi = sum * 4
mpi //= 10**10
end_time = time.time()
run_time = str(end_time - start_time)
mpi_str = str(mpi)
mpi_str = mpi_str[:1] + '.' + mpi_str[1:]



print('运行时间: ' + run_time)
print('计算结果: ',mpi_str)
print('')
