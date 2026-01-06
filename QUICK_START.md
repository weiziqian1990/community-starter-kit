# 🚀 快速开始 | Quick Start Guide

## 🌐 在线版本 - 最简单的使用方式

### 方式一：一键启动（推荐）

**Windows 用户:**
```bash
双击运行 start_web.bat
```

**Mac/Linux 用户:**
```bash
./start_web.sh
```

**或者手动运行:**
```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 启动应用
streamlit run app.py
```

✅ **应用将在浏览器自动打开:** `http://localhost:8501`

---

## 📱 如何使用在线版

### 步骤 1: 上传图片
- 点击"上传图片"按钮
- 选择你的图片文件（支持 PNG, JPG, BMP, GIF 等格式）
- 图片会立即显示预览

### 步骤 2: 选择输出类型
- **全部** - 同时生成头像和图标
- **仅头像** - 只生成 240×240 的头像
- **仅图标** - 只生成 50×50 的图标

### 步骤 3: 开始处理
- 点击"开始处理"按钮
- 等待几秒钟（通常不到1秒）
- 查看处理结果

### 步骤 4: 下载
- 点击对应的"下载"按钮
- 可以单独下载头像或图标
- 也可以打包下载所有文件（ZIP格式）

---

## 💻 命令行版本 - 批量处理

如果你需要处理大量图片，使用命令行版本更高效：

```bash
# 处理单个图片
python wechat_image_slicer.py image.png

# 批量处理
python wechat_image_slicer.py *.png

# 只生成头像
python wechat_image_slicer.py image.png --avatar-only

# 指定输出目录
python wechat_image_slicer.py image.png -o ./my_output
```

---

## 🎯 实际效果

### 输入
- 任意尺寸的图片（如 1920×1080, 800×600 等）
- 常见格式：PNG, JPG, BMP, GIF 等

### 输出
- **头像**: `image_avatar_240x240.png`
  - 尺寸: 240×240 像素
  - 格式: PNG
  - 大小: ≤ 500KB

- **图标**: `image_icon_50x50.png`
  - 尺寸: 50×50 像素
  - 格式: PNG
  - 大小: ≤ 500KB

---

## 🔧 系统要求

- **Python**: 3.7 或更高版本
- **系统**: Windows, Mac, Linux 均支持
- **浏览器**: Chrome, Firefox, Safari, Edge（在线版）

---

## 📦 首次使用

第一次使用需要安装依赖：

```bash
pip install -r requirements.txt
```

这将安装：
- Pillow (图片处理库)
- Streamlit (Web框架，仅在线版需要)

---

## ❓ 常见问题

### Q: 启动后浏览器没有自动打开？
A: 手动访问 `http://localhost:8501`

### Q: 提示"命令未找到"？
A: 确保已安装 Python 并添加到系统 PATH

### Q: 处理后的图片质量下降？
A: 使用更高分辨率的原图可以获得更好的效果

### Q: 文件大小仍然超过 500KB？
A: 工具会自动压缩，如果原图过大可能会显著降低质量。建议使用适中尺寸的原图。

### Q: 支持透明背景吗？
A: 是的！工具完全支持 PNG 透明背景

---

## 🌐 部署到云端

如果你想让其他人也能使用，可以部署到云端：

### 最简单的方式 - Streamlit Cloud (免费)

1. Fork 这个仓库到你的 GitHub
2. 访问 https://share.streamlit.io/
3. 用 GitHub 登录
4. 选择你的仓库和 `app.py` 文件
5. 点击 Deploy
6. 等待几分钟，获得永久链接！

详细部署指南请查看 [DEPLOYMENT.md](./DEPLOYMENT.md)

---

## 📞 需要帮助？

- 查看 [USAGE.md](./USAGE.md) - 详细使用说明
- 查看 [DEPLOYMENT.md](./DEPLOYMENT.md) - 部署指南
- 提交 Issue 到 GitHub

---

## 🎉 开始使用吧！

现在就运行 `streamlit run app.py` 或双击启动脚本，开始使用吧！

**祝使用愉快！ Enjoy! 🚀**
