#!/usr/bin/env python3
"""
WeChat Image Slicer Tool
自动切图工具 - 符合腾讯微信表情管理页面要求

Requirements from WeChat Sticker Management:
- Avatar (头像): PNG format, 240*240 pixels, max 500KB
- Icon (图标): PNG format, 50*50 pixels, max 500KB
"""

import os
import sys
from pathlib import Path
from typing import Tuple
from PIL import Image
import argparse


class WeChatImageSlicer:
    """WeChat图片处理工具类"""

    # WeChat requirements
    AVATAR_SIZE = (240, 240)
    ICON_SIZE = (50, 50)
    MAX_FILE_SIZE = 500 * 1024  # 500KB in bytes
    OUTPUT_FORMAT = 'PNG'

    def __init__(self, input_path: str, output_dir: str = None):
        """
        初始化图片处理器

        Args:
            input_path: 输入图片路径
            output_dir: 输出目录路径，默认为当前目录下的output文件夹
        """
        self.input_path = Path(input_path)
        if not self.input_path.exists():
            raise FileNotFoundError(f"输入文件不存在: {input_path}")

        self.output_dir = Path(output_dir) if output_dir else Path('./output')
        self.output_dir.mkdir(exist_ok=True)

        # Load the original image
        self.original_image = Image.open(self.input_path)
        if self.original_image.mode != 'RGBA':
            # Convert to RGBA to preserve transparency
            self.original_image = self.original_image.convert('RGBA')

    def resize_image(self, size: Tuple[int, int]) -> Image.Image:
        """
        按照指定尺寸调整图片大小，保持宽高比并居中裁剪

        Args:
            size: 目标尺寸 (width, height)

        Returns:
            调整后的图片对象
        """
        # Calculate aspect ratios
        original_ratio = self.original_image.width / self.original_image.height
        target_ratio = size[0] / size[1]

        if original_ratio > target_ratio:
            # Original is wider, fit to height
            new_height = size[1]
            new_width = int(new_height * original_ratio)
        else:
            # Original is taller, fit to width
            new_width = size[0]
            new_height = int(new_width / original_ratio)

        # Resize with high-quality resampling
        resized = self.original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Create a new image with the target size
        final_image = Image.new('RGBA', size, (255, 255, 255, 0))

        # Calculate paste position (center)
        paste_x = (size[0] - new_width) // 2
        paste_y = (size[1] - new_height) // 2

        # Paste the resized image onto the center
        final_image.paste(resized, (paste_x, paste_y))

        return final_image

    def optimize_file_size(self, image: Image.Image, output_path: Path, max_size: int = MAX_FILE_SIZE):
        """
        优化图片文件大小，确保不超过限制

        Args:
            image: PIL图片对象
            output_path: 输出路径
            max_size: 最大文件大小（字节）
        """
        # Start with high quality
        quality = 95

        while quality > 10:
            # Save with current quality
            image.save(output_path, self.OUTPUT_FORMAT, optimize=True, quality=quality)

            # Check file size
            file_size = output_path.stat().st_size

            if file_size <= max_size:
                print(f"✓ 优化成功: {output_path.name} ({file_size / 1024:.1f}KB, quality={quality})")
                return

            # Reduce quality for next iteration
            quality -= 5

        # If still too large, apply more aggressive compression
        print(f"⚠ 警告: {output_path.name} 文件较大，应用更激进的压缩...")
        image.save(output_path, self.OUTPUT_FORMAT, optimize=True, quality=10)
        final_size = output_path.stat().st_size
        print(f"✓ 最终大小: {final_size / 1024:.1f}KB")

    def generate_avatar(self) -> Path:
        """
        生成微信头像 (240x240)

        Returns:
            输出文件路径
        """
        print(f"\n生成头像 (240x240)...")
        avatar_image = self.resize_image(self.AVATAR_SIZE)

        output_filename = f"{self.input_path.stem}_avatar_240x240.png"
        output_path = self.output_dir / output_filename

        self.optimize_file_size(avatar_image, output_path)
        return output_path

    def generate_icon(self) -> Path:
        """
        生成微信图标 (50x50)

        Returns:
            输出文件路径
        """
        print(f"\n生成图标 (50x50)...")
        icon_image = self.resize_image(self.ICON_SIZE)

        output_filename = f"{self.input_path.stem}_icon_50x50.png"
        output_path = self.output_dir / output_filename

        self.optimize_file_size(icon_image, output_path)
        return output_path

    def generate_all(self) -> dict:
        """
        生成所有所需尺寸的图片

        Returns:
            包含生成文件路径的字典
        """
        print(f"\n{'='*60}")
        print(f"处理图片: {self.input_path.name}")
        print(f"原始尺寸: {self.original_image.width}x{self.original_image.height}")
        print(f"{'='*60}")

        results = {
            'avatar': self.generate_avatar(),
            'icon': self.generate_icon()
        }

        print(f"\n{'='*60}")
        print(f"✓ 所有图片生成完成!")
        print(f"输出目录: {self.output_dir.absolute()}")
        print(f"{'='*60}\n")

        return results


def main():
    """命令行入口"""
    parser = argparse.ArgumentParser(
        description='微信表情管理页面图片自动切图工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 处理单个图片
  python wechat_image_slicer.py input.png

  # 指定输出目录
  python wechat_image_slicer.py input.png -o ./my_output

  # 批量处理目录下所有图片
  python wechat_image_slicer.py ./images/*.png

  # 只生成头像
  python wechat_image_slicer.py input.png --avatar-only

  # 只生成图标
  python wechat_image_slicer.py input.png --icon-only
        """
    )

    parser.add_argument('input', nargs='+', help='输入图片路径，支持多个文件或通配符')
    parser.add_argument('-o', '--output', default='./output', help='输出目录 (默认: ./output)')
    parser.add_argument('--avatar-only', action='store_true', help='仅生成头像 (240x240)')
    parser.add_argument('--icon-only', action='store_true', help='仅生成图标 (50x50)')

    args = parser.parse_args()

    # Process each input file
    input_files = []
    for pattern in args.input:
        input_files.extend(Path('.').glob(pattern) if '*' in pattern else [Path(pattern)])

    if not input_files:
        print("错误: 未找到输入文件")
        sys.exit(1)

    print(f"\n找到 {len(input_files)} 个文件待处理\n")

    for input_file in input_files:
        try:
            slicer = WeChatImageSlicer(str(input_file), args.output)

            if args.avatar_only:
                slicer.generate_avatar()
            elif args.icon_only:
                slicer.generate_icon()
            else:
                slicer.generate_all()

        except Exception as e:
            print(f"✗ 处理失败 {input_file.name}: {str(e)}")
            continue

    print("\n处理完成!")


if __name__ == '__main__':
    main()
