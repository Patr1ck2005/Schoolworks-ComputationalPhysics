import numpy as np
import os

# 创建目标文件夹，如果不存在
output_dir = 'target/data2'
os.makedirs(output_dir, exist_ok=True)

# 生成1000个样本
num_samples = 1000
bits_per_sample = 1000000
bytes_per_sample = (bits_per_sample + 7) // 8  # 125,000 bytes

# 定义文件大小限制
max_file_size = 128 * 1024  # 128 KB = 131,072 bytes

for sample_index in range(num_samples):
    # 使用numpy生成随机bit数组
    random_bits = np.random.randint(2, size=bits_per_sample).astype(np.uint8)

    # 将bit数组转换为字节数组
    byte_array = np.packbits(random_bits)

    if len(byte_array) > max_file_size:
        byte_array = byte_array[:max_file_size]

    # 定义文件路径
    file_path = os.path.join(output_dir, f'sample_{sample_index + 1}.bin')

    # 写入文件
    with open(file_path, 'wb') as file:
        file.write(byte_array)

print(f'Generated {num_samples} samples of {bits_per_sample} bits each in {output_dir}')
