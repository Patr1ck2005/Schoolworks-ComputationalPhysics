# color_schemes.py
import numpy as np
from matplotlib import cm


def color_scheme_static(root_index, iterations, scheme='scheme1'):
    """
    根据给定的根编号和迭代次数生成 RGB 图像数组。
    参数：
      root_index: 每个像素收敛的根编号数组
      iterations: 每个像素的迭代次数数组
      scheme: 'scheme1' 或 'scheme2'
    返回：RGB 图像数组
    """
    h, w = root_index.shape
    image = np.zeros((h, w, 3), dtype=np.float32)

    if scheme == 'scheme1':
        # 方案 1：不同根采用不同颜色，迭代次数用于调节亮度
        base_colors = np.array([[1, 0, 0],  # 红
                                [0, 1, 0],  # 绿
                                [0, 0, 1]])  # 蓝
        norm_iter = 1 - iterations / (iterations.max() + 1e-8)  # 防止除零
        for i in range(3):
            mask = (root_index == i)
            for j in range(3):
                image[..., j] += mask * base_colors[i, j] * norm_iter
    elif scheme == 'scheme2':
        # 方案 2：利用 colormap 平滑过渡
        color_index = (root_index + iterations / (iterations.max() + 1e-8)).astype(np.float32)
        # 归一化到 [0,1]
        color_index = (color_index - color_index.min()) / (color_index.max() - color_index.min() + 1e-8)
        cmap = cm.get_cmap('plasma')
        image = cmap(color_index)[..., :3]
    else:
        raise ValueError("未知的配色方案，请选择 'scheme1' 或 'scheme2'")

    return image
