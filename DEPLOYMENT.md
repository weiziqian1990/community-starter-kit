# 🚀 部署指南 | Deployment Guide

本文档介绍如何将微信表情切图工具部署到在线平台，让用户通过浏览器访问使用。

This document explains how to deploy the WeChat Image Slicer tool to online platforms for browser-based access.

---

## 📋 部署选项 | Deployment Options

### 1. Streamlit Cloud (推荐 | Recommended) ⭐

**优点 | Advantages:**
- ✅ 完全免费 | Completely free
- ✅ 零配置部署 | Zero-config deployment
- ✅ 自动HTTPS | Automatic HTTPS
- ✅ GitHub集成 | GitHub integration
- ✅ 自动更新 | Auto-updates

**部署步骤 | Deployment Steps:**

1. **Fork或Clone仓库**
   ```bash
   git clone https://github.com/weiziqian1990/community-starter-kit.git
   cd community-starter-kit
   ```

2. **推送到GitHub**
   ```bash
   git push origin main
   ```

3. **访问 Streamlit Cloud**
   - 前往 https://share.streamlit.io/
   - 使用GitHub账号登录
   - 点击 "New app"

4. **配置部署**
   - Repository: `weiziqian1990/community-starter-kit`
   - Branch: `main` 或 `claude/wechat-image-slicer-tool-ylyju`
   - Main file path: `app.py`

5. **点击 Deploy！**
   - 等待几分钟，应用即可上线
   - 获得类似 `https://your-app-name.streamlit.app` 的URL

---

### 2. Hugging Face Spaces

**优点 | Advantages:**
- ✅ 免费托管 | Free hosting
- ✅ GPU支持（付费）| GPU support (paid)
- ✅ 社区友好 | Community-friendly

**部署步骤 | Deployment Steps:**

1. **创建Space**
   - 访问 https://huggingface.co/spaces
   - 点击 "Create new Space"
   - 选择 "Streamlit" SDK

2. **上传文件**
   - 上传 `app.py`
   - 上传 `wechat_image_slicer.py`
   - 上传 `requirements.txt`

3. **Space自动部署**
   - 应用会自动构建和部署
   - 获得 `https://huggingface.co/spaces/your-username/space-name` URL

---

### 3. Railway

**优点 | Advantages:**
- ✅ 简单部署 | Easy deployment
- ✅ 免费额度 | Free tier available
- ✅ 自定义域名 | Custom domain support

**部署步骤 | Deployment Steps:**

1. **安装Railway CLI**
   ```bash
   npm install -g @railway/cli
   ```

2. **登录并初始化**
   ```bash
   railway login
   railway init
   ```

3. **部署**
   ```bash
   railway up
   ```

---

### 4. Render

**优点 | Advantages:**
- ✅ 免费静态托管 | Free static hosting
- ✅ 自动SSL | Automatic SSL
- ✅ CDN支持 | CDN support

**部署步骤 | Deployment Steps:**

1. 访问 https://render.com/
2. 连接GitHub仓库
3. 选择 "Web Service"
4. 配置：
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `streamlit run app.py --server.port=$PORT`

---

## 🛠️ 本地运行 | Local Development

在部署前，先在本地测试应用：

Before deployment, test the app locally:

```bash
# 安装依赖 | Install dependencies
pip install -r requirements.txt

# 运行应用 | Run the app
streamlit run app.py
```

应用将在 `http://localhost:8501` 打开。

The app will open at `http://localhost:8501`.

---

## ⚙️ 环境变量 | Environment Variables

目前应用不需要环境变量。如果将来需要，可以在平台上设置：

The app currently doesn't require environment variables. If needed in the future:

**Streamlit Cloud:**
- Settings → Secrets → Add secrets in TOML format

**Hugging Face:**
- Settings → Repository secrets

**Railway/Render:**
- Environment → Add variables

---

## 📊 性能优化 | Performance Optimization

### 文件大小限制 | File Size Limits

不同平台的上传限制：

| 平台 Platform | 默认限制 Default Limit |
|--------------|----------------------|
| Streamlit Cloud | 200MB |
| Hugging Face | 500MB |
| Railway | 100MB |
| Render | 512MB |

### 优化建议 | Optimization Tips

1. **缓存处理**
   ```python
   @st.cache_data
   def process_image(image_data):
       # 处理逻辑
       pass
   ```

2. **限制上传大小**
   - 在 `.streamlit/config.toml` 中设置
   - 默认已设置为10MB

3. **压缩输出**
   - 已实现自动优化
   - 确保输出 ≤ 500KB

---

## 🔒 安全性 | Security

### 已实现的安全措施 | Implemented Security Measures

- ✅ XSRF保护 | XSRF protection
- ✅ 文件类型验证 | File type validation
- ✅ 临时文件清理 | Temporary file cleanup
- ✅ 无数据存储 | No data storage

### 推荐的额外措施 | Recommended Additional Measures

1. **速率限制** - 使用平台提供的限流功能
2. **访问控制** - 如需要，可添加密码保护
3. **日志监控** - 启用平台的日志功能

---

## 📱 移动端支持 | Mobile Support

应用已优化移动端体验：

The app is optimized for mobile:

- ✅ 响应式布局 | Responsive layout
- ✅ 触摸友好 | Touch-friendly
- ✅ 移动端上传 | Mobile upload support

---

## 🐛 故障排除 | Troubleshooting

### 常见问题 | Common Issues

**1. 部署失败 "Module not found"**
```bash
# 确保requirements.txt包含所有依赖
pip freeze > requirements.txt
```

**2. 应用超时**
```python
# 在app.py中增加超时设置
st.set_page_config(
    ...,
    initial_sidebar_state="collapsed"
)
```

**3. 图片上传失败**
```bash
# 检查.streamlit/config.toml中的maxUploadSize设置
[server]
maxUploadSize = 10
```

**4. 处理速度慢**
- 使用缓存装饰器 `@st.cache_data`
- 优化图片处理算法
- 考虑升级到付费计划

---

## 📈 监控和分析 | Monitoring & Analytics

### Streamlit Cloud

- 内置分析面板
- 查看访问量和使用情况
- Settings → Analytics

### 添加Google Analytics

在 `app.py` 中添加：

```python
# 在<head>中注入Google Analytics
st.markdown("""
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR-GA-ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'YOUR-GA-ID');
</script>
""", unsafe_allow_html=True)
```

---

## 🔄 更新部署 | Updating Deployment

### Streamlit Cloud / Hugging Face

自动部署 - 只需推送代码：

```bash
git add .
git commit -m "Update feature"
git push origin main
```

### Railway / Render

同样支持自动部署，或使用CLI手动触发：

```bash
railway up
# 或
render deploy
```

---

## 💰 成本估算 | Cost Estimation

### 免费额度 | Free Tier

所有推荐平台都提供免费额度，足够个人使用：

| 平台 | 免费额度 | 限制 |
|------|---------|------|
| Streamlit Cloud | 无限制 | 公开应用，1个私有应用 |
| Hugging Face | 无限制 | 社区支持 |
| Railway | $5/月 | 500小时运行时间 |
| Render | 750小时/月 | 自动休眠 |

### 付费升级 | Paid Upgrades

如果需要更多资源或私有部署：

- **Streamlit Cloud Teams**: $250/月起
- **Hugging Face Pro**: $9/月起
- **Railway Pro**: $20/月起
- **Render Standard**: $7/月起

---

## 📞 获取帮助 | Getting Help

遇到部署问题？

Having deployment issues?

1. 查看平台文档
2. 在GitHub提Issue
3. 访问平台社区论坛

---

## 🎯 快速部署链接 | Quick Deploy Links

点击下方按钮一键部署：

Click below for one-click deployment:

[![Deploy to Streamlit Cloud](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)

---

**祝部署顺利！Good luck with your deployment! 🚀**
