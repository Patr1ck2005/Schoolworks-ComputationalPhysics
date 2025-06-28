import os
import random

# 创建目标文件夹
os.makedirs("target/data", exist_ok=True)

# 生成并保存随机数
num_samples = 1000
bits_per_sample = 1000000

for i in range(num_samples):
    random_bytes = bytearray(random.getrandbits(8) for _ in range(bits_per_sample // 8))
    with open(f"target/data/sample_{i}.bin", "wb") as file:
        file.write(random_bytes)
