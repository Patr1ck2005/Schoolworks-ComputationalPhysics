# static_generator.py
import os
import numpy as np
from PIL import Image
from algorithm import compute_newton_fractal
from color_schemes import color_scheme_static
import tqdm  # 引入 tqdm 库显示进度条


def generate_static_fractal(xmin=-1.5, xmax=1.5, ymin=-1.5, ymax=1.5,
                                  width=100000, height=100000, tile_size=5000,
                                  tol=1e-4, max_iter=50, scheme='scheme1',
                                  output_dir='output_static'):
    """
    采用分块方式生成超大分辨率（例如 100k×100k）分形图像，分块计算降低内存消耗。
    整个处理流程中加入了进度条显示当前已处理的 tile 数量。

    参数：
      xmin, xmax, ymin, ymax : 计算区域
      width, height         : 整幅图像的总分辨率
      tile_size             : 每个分块的大小（假设为正方形）
      tol, max_iter         : 牛顿迭代的容差和最大迭代次数
      scheme                : 配色方案（例如 'scheme1' 或 'scheme2'）
      output_dir            : 输出文件夹
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 创建存储最终图像的数组（以 uint8 保存 RGB 图像）
    full_image = np.zeros((height, width, 3), dtype=np.uint8)

    # 分块数目（向上取整）
    tiles_y = (height + tile_size - 1) // tile_size
    tiles_x = (width + tile_size - 1) // tile_size
    total_tiles = tiles_x * tiles_y

    # 每个像素对应坐标的步长
    dx = (xmax - xmin) / (width - 1)
    dy = (ymax - ymin) / (height - 1)

    # 使用 tqdm 创建进度条
    with tqdm.tqdm(total=total_tiles, desc="Processing Tiles") as pbar:
        for ty in range(tiles_y):
            for tx in range(tiles_x):
                # 当前 tile 的像素范围
                y_start = ty * tile_size
                y_end = min((ty + 1) * tile_size, height)
                x_start = tx * tile_size
                x_end = min((tx + 1) * tile_size, width)

                tile_width = x_end - x_start
                tile_height = y_end - y_start

                # 根据 tile 位置计算对应的复平面区域
                tile_xmin = xmin + x_start * dx
                tile_xmax = xmin + (x_end - 1) * dx
                tile_ymin = ymin + y_start * dy
                tile_ymax = ymin + (y_end - 1) * dy

                # 输出当前处理 tile 的调试信息（可选）
                # print(f"Processing tile: x[{x_start}:{x_end}], y[{y_start}:{y_end}]")

                # 调用加速后的牛顿迭代函数计算当前 tile
                root_index, iterations = compute_newton_fractal(tile_xmin, tile_xmax, tile_ymin, tile_ymax,
                                                                tile_width, tile_height, tol, max_iter)
                # 根据计算结果生成颜色映射图像
                tile_image = color_scheme_static(root_index, iterations, scheme=scheme)

                # 将浮点型的图像数据（假设范围在 [0,1]）转换为 uint8
                tile_image_uint8 = (np.clip(tile_image, 0, 1) * 255).astype(np.uint8)

                # 将当前 tile 拼接到整幅图像中
                full_image[y_start:y_end, x_start:x_end, :] = tile_image_uint8

                # 更新进度条，每处理完一个 tile 更新一次
                pbar.update(1)

    # 利用 PIL 保存最终大图像
    output_path = os.path.join(output_dir, f"newton_fractal_{scheme}_{width}x{height}_tiled.png")
    Image.fromarray(full_image).save(output_path)
    print(f"静态分形图已保存至: {output_path}")
