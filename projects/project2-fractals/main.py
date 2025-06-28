# main.py
import argparse
from static_generator import generate_static_fractal
from interactive_viewer import start_viewer

def main():
    parser = argparse.ArgumentParser(description="Newton Fractal 生成器")
    parser.add_argument('--mode', choices=['static', 'interactive'], default='static',
                        help="选择模式：静态生成 (static) 或交互模式 (interactive)")
    parser.add_argument('--scheme', choices=['scheme1', 'scheme2'], default='scheme1',
                        help="选择颜色方案")
    args = parser.parse_args()

    if args.mode == 'static':
        # 调整参数：例如这里先尝试 100000x100000 的静态大图
        generate_static_fractal(width=100000, height=100000, scheme=args.scheme)
    else:
        start_viewer()

if __name__ == '__main__':
    main()
