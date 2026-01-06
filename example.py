#!/usr/bin/env python3
"""
Example script showing how to use WeChatImageSlicer programmatically
示例脚本 - 演示如何在代码中使用 WeChatImageSlicer
"""

from wechat_image_slicer import WeChatImageSlicer
from pathlib import Path


def example_single_image():
    """处理单个图片示例"""
    print("\n" + "="*60)
    print("示例 1: 处理单个图片")
    print("="*60)

    # 假设有一个输入图片
    input_image = "sample.png"

    # 检查文件是否存在
    if not Path(input_image).exists():
        print(f"⚠ 文件不存在: {input_image}")
        print("请准备一个图片文件并命名为 sample.png")
        return

    # 创建处理器
    slicer = WeChatImageSlicer(input_image, output_dir='./output')

    # 生成所有尺寸
    results = slicer.generate_all()

    print(f"\n生成的文件:")
    print(f"  - 头像: {results['avatar']}")
    print(f"  - 图标: {results['icon']}")


def example_batch_processing():
    """批量处理示例"""
    print("\n" + "="*60)
    print("示例 2: 批量处理多个图片")
    print("="*60)

    # 获取所有图片文件
    image_dir = Path("./images")

    if not image_dir.exists():
        print(f"⚠ 目录不存在: {image_dir}")
        print("请创建 ./images 目录并放入一些图片")
        return

    # 支持的图片格式
    patterns = ['*.png', '*.jpg', '*.jpeg', '*.bmp', '*.gif']
    image_files = []

    for pattern in patterns:
        image_files.extend(image_dir.glob(pattern))

    if not image_files:
        print("⚠ 未找到图片文件")
        return

    print(f"找到 {len(image_files)} 个图片文件\n")

    # 批量处理
    for idx, image_file in enumerate(image_files, 1):
        print(f"\n[{idx}/{len(image_files)}] 处理: {image_file.name}")

        try:
            slicer = WeChatImageSlicer(str(image_file), output_dir='./batch_output')
            slicer.generate_all()
        except Exception as e:
            print(f"✗ 错误: {e}")
            continue


def example_selective_generation():
    """选择性生成示例"""
    print("\n" + "="*60)
    print("示例 3: 选择性生成头像或图标")
    print("="*60)

    input_image = "sample.png"

    if not Path(input_image).exists():
        print(f"⚠ 文件不存在: {input_image}")
        return

    slicer = WeChatImageSlicer(input_image, output_dir='./output')

    # 只生成头像
    print("\n只生成头像...")
    avatar = slicer.generate_avatar()
    print(f"✓ 头像: {avatar}")

    # 只生成图标
    print("\n只生成图标...")
    icon = slicer.generate_icon()
    print(f"✓ 图标: {icon}")


def main():
    """运行所有示例"""
    print("\n" + "="*60)
    print("WeChat Image Slicer - 使用示例")
    print("="*60)

    # 运行示例
    example_single_image()
    example_selective_generation()
    example_batch_processing()

    print("\n" + "="*60)
    print("所有示例执行完成!")
    print("="*60 + "\n")


if __name__ == '__main__':
    main()
