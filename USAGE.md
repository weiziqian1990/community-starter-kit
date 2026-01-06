# 微信表情管理页面自动切图工具使用说明

## WeChat Image Slicer Tool - Usage Guide

这是一个自动化图片处理工具，可以将图片按照腾讯微信表情管理页面的要求进行切图和优化。

This is an automated image processing tool that slices and optimizes images according to Tencent WeChat sticker management page requirements.

---

## 📋 功能特性 / Features

- ✅ 自动生成 240×240 像素的头像图片 (Avatar)
- ✅ 自动生成 50×50 像素的图标图片 (Icon)
- ✅ 输出 PNG 格式
- ✅ 自动优化文件大小，确保不超过 500KB
- ✅ 保持图片宽高比，智能居中裁剪
- ✅ 支持批量处理多个图片
- ✅ 保留图片透明通道

---

## 🚀 快速开始 / Quick Start

### 1. 安装依赖 / Install Dependencies

```bash
pip install -r requirements.txt
```

或者直接安装 Pillow:
```bash
pip install Pillow
```

### 2. 基本使用 / Basic Usage

**处理单个图片:**
```bash
python wechat_image_slicer.py your_image.png
```

这将在 `./output` 目录下生成两个文件:
- `your_image_avatar_240x240.png` - 头像图片
- `your_image_icon_50x50.png` - 图标图片

---

## 📖 详细用法 / Detailed Usage

### 命令行参数 / Command Line Arguments

```
用法: python wechat_image_slicer.py [输入文件] [选项]

位置参数:
  input                 输入图片路径，支持多个文件或通配符

可选参数:
  -h, --help            显示帮助信息
  -o OUTPUT, --output OUTPUT
                        输出目录 (默认: ./output)
  --avatar-only         仅生成头像 (240x240)
  --icon-only           仅生成图标 (50x50)
```

### 使用示例 / Examples

**1. 处理单个图片**
```bash
python wechat_image_slicer.py photo.jpg
```

**2. 指定输出目录**
```bash
python wechat_image_slicer.py photo.jpg -o ./wechat_stickers
```

**3. 批量处理多个图片**
```bash
python wechat_image_slicer.py image1.png image2.jpg image3.png
```

**4. 使用通配符批量处理**
```bash
python wechat_image_slicer.py ./images/*.png
```

**5. 只生成头像 (240x240)**
```bash
python wechat_image_slicer.py photo.jpg --avatar-only
```

**6. 只生成图标 (50x50)**
```bash
python wechat_image_slicer.py photo.jpg --icon-only
```

---

## 📐 技术规格 / Technical Specifications

### 微信要求 / WeChat Requirements

根据微信表情管理页面的要求：

| 项目 | 规格 |
|------|------|
| **头像 (Avatar)** | PNG 格式，240×240 像素，不超过 500KB |
| **图标 (Icon)** | PNG 格式，50×50 像素，不超过 500KB |

### 工具特性 / Tool Features

- **格式支持**: 支持所有常见图片格式 (PNG, JPG, JPEG, BMP, GIF 等)
- **输出格式**: PNG (保留透明通道)
- **调整方式**: 保持宽高比，智能居中裁剪
- **优化算法**: 自动调整质量参数，确保文件大小符合要求
- **重采样算法**: 使用 LANCZOS 算法，确保最佳质量

---

## 🔧 高级功能 / Advanced Features

### Python API 调用 / Python API Usage

你也可以在 Python 代码中直接使用该工具:

```python
from wechat_image_slicer import WeChatImageSlicer

# 创建处理器
slicer = WeChatImageSlicer('input.png', output_dir='./output')

# 生成所有尺寸
results = slicer.generate_all()
print(f"Avatar: {results['avatar']}")
print(f"Icon: {results['icon']}")

# 或者只生成特定尺寸
avatar_path = slicer.generate_avatar()
icon_path = slicer.generate_icon()
```

### 自定义处理 / Custom Processing

```python
from wechat_image_slicer import WeChatImageSlicer
from pathlib import Path

# 批量处理目录下所有图片
image_dir = Path('./images')
output_dir = Path('./wechat_output')

for image_file in image_dir.glob('*.png'):
    try:
        slicer = WeChatImageSlicer(str(image_file), str(output_dir))
        slicer.generate_all()
        print(f"✓ 处理完成: {image_file.name}")
    except Exception as e:
        print(f"✗ 处理失败: {image_file.name} - {e}")
```

---

## 📊 工作流程 / Workflow

1. **读取原始图片** - 加载输入图片并转换为 RGBA 模式
2. **计算缩放比例** - 根据目标尺寸计算最佳缩放比例
3. **智能裁剪** - 保持宽高比，将图片居中裁剪到目标尺寸
4. **优化压缩** - 自动调整压缩质量，确保文件大小 ≤ 500KB
5. **保存输出** - 以 PNG 格式保存处理后的图片

---

## ⚠️ 注意事项 / Notes

1. **输入格式**: 支持所有 Pillow 库支持的图片格式
2. **输出格式**: 统一输出为 PNG 格式
3. **文件大小**: 工具会自动优化，确保不超过 500KB
4. **透明度**: 保留原图的透明通道
5. **覆盖警告**: 如果输出文件已存在，将会被覆盖

---

## 🐛 故障排除 / Troubleshooting

### 问题: 安装依赖失败
**解决方案**: 确保已安装 Python 3.7+ 和 pip
```bash
python --version
pip --version
```

### 问题: 文件大小仍超过 500KB
**解决方案**: 工具会自动降低质量直到满足要求。如果原图过大，可能会显著降低质量。建议使用较小的原图。

### 问题: 图片质量下降
**解决方案**: 使用高分辨率的原图可以获得更好的输出质量。推荐原图分辨率至少为目标尺寸的 2 倍。

---

## 📄 许可证 / License

MIT License

---

## 👨‍💻 作者 / Author

Created with ❤️ for WeChat sticker creators

---

## 🔗 相关链接 / Related Links

- [微信开放平台](https://open.weixin.qq.com/)
- [Pillow 文档](https://pillow.readthedocs.io/)

---

## 📞 支持 / Support

如果遇到问题或有建议，欢迎提交 Issue。

If you encounter any issues or have suggestions, feel free to submit an Issue.
