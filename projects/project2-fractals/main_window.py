# main_window.py
import tkinter as tk
from tkinter import messagebox
from static_generator import generate_static_fractal
from interactive_viewer import start_viewer
import threading


def run_static_mode():
    # 静态模式的计算可能比较耗时，为防止阻塞GUI，建议放入子线程运行
    def task():
        try:
            # 可以在此处调整参数，例如宽度和高度、颜色方案等
            generate_static_fractal(width=10000, height=10000, scheme='scheme1')
            messagebox.showinfo("完成", "静态分形图已生成并保存。")
        except Exception as e:
            messagebox.showerror("错误", str(e))

    threading.Thread(target=task).start()


def run_interactive_mode():
    # 交互模式直接启动窗口（该窗口将占用当前线程，不建议同时运行多个 tkinter 窗口）
    start_viewer()


def main():
    root = tk.Tk()
    root.title("Newton Fractal 模式选择")
    root.geometry("300x200")

    label = tk.Label(root, text="请选择模式", font=("Arial", 14))
    label.pack(pady=20)

    btn_static = tk.Button(root, text="静态模式", command=run_static_mode, width=15)
    btn_static.pack(pady=10)

    btn_interactive = tk.Button(root, text="交互模式", command=run_interactive_mode, width=15)
    btn_interactive.pack(pady=10)

    root.mainloop()


if __name__ == '__main__':
    main()
