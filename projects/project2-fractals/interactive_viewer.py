# interactive_viewer.py
import numpy as np
import matplotlib.pyplot as plt
from algorithm import compute_newton_fractal
from color_schemes import color_scheme_static


class FractalViewer:
    def __init__(self, xmin=-1.5, xmax=1.5, ymin=-1.5, ymax=1.5,
                 width=80, height=80, tol=1e-4, max_iter=50, scheme='scheme2'):
        self.xmin, self.xmax = xmin, xmax
        self.ymin, self.ymax = ymin, ymax
        self.width = width
        self.height = height
        self.tol = tol
        self.max_iter = max_iter
        self.scheme = scheme

        # 创建 matplotlib 窗口
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        self.ax.set_title("Newton Fractal - 交互模式")
        self.im = None

        # 绑定事件
        self.cid_scroll = self.fig.canvas.mpl_connect('scroll_event', self.on_scroll)
        self.cid_press = self.fig.canvas.mpl_connect('button_press_event', self.on_press)
        self.cid_release = self.fig.canvas.mpl_connect('button_release_event', self.on_release)
        self.cid_motion = self.fig.canvas.mpl_connect('motion_notify_event', self.on_motion)
        self.dragging = False
        self.last_event = None

        # 首次绘制
        self.update_fractal()

    def update_fractal(self):
        print(f"计算区域: x=[{self.xmin:.3f}, {self.xmax:.3f}], y=[{self.ymin:.3f}, {self.ymax:.3f}]")
        root_index, iterations = compute_newton_fractal(self.xmin, self.xmax, self.ymin, self.ymax,
                                                        self.width, self.height, self.tol, self.max_iter)
        image = color_scheme_static(root_index, iterations, scheme=self.scheme)
        if self.im is None:
            self.im = self.ax.imshow(image, extent=(self.xmin, self.xmax, self.ymin, self.ymax))
        else:
            self.im.set_data(image)
            self.im.set_extent((self.xmin, self.xmax, self.ymin, self.ymax))
        self.ax.figure.canvas.draw_idle()

    def on_scroll(self, event):
        # 以鼠标位置为中心进行缩放
        factor = 0.8 if event.button == 'up' else 1.25
        x_range = (self.xmax - self.xmin) * factor
        y_range = (self.ymax - self.ymin) * factor
        x_center = event.xdata if event.xdata is not None else (self.xmin + self.xmax) / 2
        y_center = event.ydata if event.ydata is not None else (self.ymin + self.ymax) / 2
        self.xmin = x_center - x_range / 2
        self.xmax = x_center + x_range / 2
        self.ymin = y_center - y_range / 2
        self.ymax = y_center + y_range / 2
        self.update_fractal()

    def on_press(self, event):
        self.dragging = True
        self.last_event = event

    def on_release(self, event):
        self.dragging = False
        self.last_event = None

    def on_motion(self, event):
        if self.dragging and self.last_event is not None and event.xdata is not None and event.ydata is not None:
            # 根据鼠标移动量平移视图
            dx = event.xdata - self.last_event.xdata
            dy = event.ydata - self.last_event.ydata
            self.xmin -= dx
            self.xmax -= dx
            self.ymin -= dy
            self.ymax -= dy
            self.last_event = event
            self.update_fractal()


def start_viewer():
    viewer = FractalViewer()
    plt.show()


if __name__ == '__main__':
    start_viewer()
