import cv2
import numpy as np
from hashlib import sha256
from tqdm import tqdm  # 进度条库

# ========== 参数设置（硬编码） ==========
VIDEO_PATH = "sample_960x400_ocean_with_audio.avi"   # 输入视频文件路径
BITS_PER_PIXEL = 2                  # 每像素提取最低几位 (1-8)
BATCH_FRAMES = 10                   # 每次聚合多少帧再做一次哈希
OUTPUT_FILE = "random.bin"          # 随机数输出二进制文件

def extract_lsb_bits(frame: np.ndarray, bits_per_pixel: int = BITS_PER_PIXEL) -> bytes:
    """
    从灰度帧中提取每像素最低 bits_per_pixel 位，并打包为字节流。
    """
    gray = frame if len(frame.shape) == 2 else cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mask = (1 << bits_per_pixel) - 1
    lsb = np.bitwise_and(gray, mask).astype(np.uint8)

    # 打平并转换成位串
    flat = lsb.flatten()
    bitstr = ''.join(f"{val:0{bits_per_pixel}b}" for val in flat)
    # 补齐到字节边界
    padding = (-len(bitstr)) % 8
    bitstr += '0' * padding

    # 按 8 位打包
    out = bytearray()
    for i in range(0, len(bitstr), 8):
        out.append(int(bitstr[i : i + 8], 2))
    return bytes(out)

def hash_compress(data: bytes) -> bytes:
    """使用 SHA-256 对输入字节流做一次压缩提取，输出 32 字节随机数。"""
    return sha256(data).digest()

# ========== 主流程 ==========
cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    raise IOError(f"无法打开视频文件: {VIDEO_PATH}")

# 获取总帧数用于进度条显示（若无法获取，可设为 None）
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) or None

out_fp = open(OUTPUT_FILE, "wb")
frame_buf = []
frame_count = 0

# 初始化进度条
progress = tqdm(total=total_frames, desc="Processing frames", unit="frame")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_count += 1
    progress.update(1)

    # 提取 LSB 比特
    bits = extract_lsb_bits(frame)
    frame_buf.append(bits)

    # 达到批量帧数，做哈希压缩并写入
    if frame_count % BATCH_FRAMES == 0:
        raw_chunk = b"".join(frame_buf)
        rnd = hash_compress(raw_chunk)
        out_fp.write(rnd)
        frame_buf.clear()

# 处理剩余帧
if frame_buf:
    raw_chunk = b"".join(frame_buf)
    rnd = hash_compress(raw_chunk)
    out_fp.write(rnd)

# 完成并关闭
progress.close()
cap.release()
out_fp.close()

print(f"提取完毕，总帧数={frame_count}，随机数据写入 {OUTPUT_FILE}")
