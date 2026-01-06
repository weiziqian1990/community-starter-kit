# WeChat Image Slicer Tool | 微信表情管理页面自动切图工具

🎨 一个自动化图片处理工具，可以将图片按照腾讯微信表情管理页面的要求进行切图和优化。

An automated image processing tool that slices and optimizes images according to Tencent WeChat sticker management page requirements.

---

## ✨ Features | 功能特性

- ✅ **自动生成头像** - 240×240 像素 PNG 格式，不超过 500KB
- ✅ **自动生成图标** - 50×50 像素 PNG 格式，不超过 500KB
- ✅ **智能优化** - 自动压缩文件大小到符合要求
- ✅ **保持比例** - 智能居中裁剪，保持原图宽高比
- ✅ **批量处理** - 支持一次处理多个图片
- ✅ **透明通道** - 完整保留图片透明度信息

---

## 🌐 在线使用 | Online Version

### 🎯 立即使用 | Use Now

**无需安装，直接在浏览器中使用！**

**No installation required - use directly in your browser!**

👉 **在线工具链接 | Online Tool:**

1. **本地运行在线版 | Run Locally:**
   ```bash
   # 安装依赖
   pip install -r requirements.txt

   # 启动Web应用
   streamlit run app.py
   ```
   然后在浏览器打开 `http://localhost:8501`

2. **部署到云端 | Deploy to Cloud:**
   - 查看 [DEPLOYMENT.md](./DEPLOYMENT.md) 了解如何部署到 Streamlit Cloud、Hugging Face 等平台
   - 一键部署，获得永久在线链接

### 💻 两种使用方式 | Two Ways to Use

| 方式 | 优点 | 适用场景 |
|------|------|---------|
| 🌐 **在线版** | 无需安装，浏览器直接使用 | 快速处理，偶尔使用 |
| 💻 **命令行版** | 批量处理，自动化脚本 | 大量图片，重复操作 |

---

## 🚀 Quick Start | 快速开始

### Installation | 安装

```bash
# Clone the repository
git clone https://github.com/weiziqian1990/community-starter-kit.git
cd community-starter-kit

# Install dependencies
pip install -r requirements.txt
```

### Usage | 使用方法

```bash
# Process a single image
python wechat_image_slicer.py your_image.png

# Batch process multiple images
python wechat_image_slicer.py image1.png image2.jpg image3.png

# Specify output directory
python wechat_image_slicer.py your_image.png -o ./output

# Generate only avatar (240x240)
python wechat_image_slicer.py your_image.png --avatar-only

# Generate only icon (50x50)
python wechat_image_slicer.py your_image.png --icon-only
```

---

## 📖 Documentation | 文档

详细使用说明请查看 [USAGE.md](./USAGE.md)

For detailed usage instructions, please see [USAGE.md](./USAGE.md)

---

## 📐 WeChat Requirements | 微信规格要求

| 项目 Item | 尺寸 Size | 格式 Format | 大小 Max Size |
|-----------|-----------|-------------|---------------|
| 头像 Avatar | 240×240 px | PNG | ≤ 500KB |
| 图标 Icon | 50×50 px | PNG | ≤ 500KB |

---

## 🛠️ Technology Stack | 技术栈

- **Python 3.7+**
- **Pillow (PIL)** - Image processing library
- **Streamlit** - Web application framework (for online version)

---

## 📄 License | 许可证

MIT License

---

## 🤝 Contributing | 贡献

欢迎提交 Issue 和 Pull Request！

Issues and Pull Requests are welcome!
