# 🎉 播客转写到飞书 v1.0.0 发布

我们很高兴地宣布 **播客转写到飞书 (Podcast to Feishu)** v1.0.0 正式发布！

这是一个自动化工具，可以一键将播客内容转写并保存到飞书文档。

---

## ✨ 核心功能

### 1️⃣ 多平台播客支持
- ✅ RSS Feed（推荐，通用性最强）
- ✅ 小宇宙播客
- ✅ Apple Podcasts
- ✅ 其他支持RSS的播客平台

### 2️⃣ AI智能转写
- 🤖 使用Claude Sonnet 4.5进行智能处理
- 📝 自动提取核心要点
- 🎯 结构化内容整理
- 💎 识别和提取金句
- 🎨 Markdown格式输出

### 3️⃣ 飞书文档集成
- 📄 自动创建飞书文档
- 🔗 即时获取文档链接
- 📂 支持指定文件夹
- 🎨 保留格式和样式

### 4️⃣ 灵活配置
- ⚙️ 自定义prompt模板
- 🔧 环境变量配置
- 📋 YAML配置文件
- 🎯 命令行参数支持

---

## 🚀 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/weiziqian1990/community-starter-kit.git
cd community-starter-kit

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 填入你的API密钥
```

### 配置

需要准备以下API凭证：

1. **Claude API Key** - 从 [Anthropic Console](https://console.anthropic.com/) 获取
2. **飞书应用凭证** - 从 [飞书开放平台](https://open.feishu.cn/) 创建应用获取

### 使用

```bash
# 基本用法
python src/main.py --url "https://example.com/podcast.rss"

# 完整示例
python src/main.py \
  --url "https://feeds.example.com/podcast.rss" \
  --prompt config/prompt_template.txt \
  --folder "fldcn123456" \
  --title "我的播客笔记"
```

---

## 📦 项目结构

```
community-starter-kit/
├── src/
│   ├── main.py              # 主程序入口
│   ├── podcast_fetcher.py   # 播客内容获取
│   ├── ai_transformer.py    # AI转写处理
│   └── feishu_writer.py     # 飞书文档写入
├── config/
│   ├── config.yaml          # 项目配置
│   └── prompt_template.txt  # Prompt模板
├── requirements.txt         # 依赖列表
├── .env.example            # 环境变量示例
├── CHANGELOG.md            # 变更日志
└── README.md               # 使用文档
```

---

## 💡 使用场景

- 📚 **知识管理**: 将优质播客内容保存到知识库
- 📝 **笔记整理**: 自动生成结构化的播客笔记
- 👥 **团队分享**: 快速分享播客精华给团队
- 🎓 **学习记录**: 记录学习内容和要点
- 🔍 **内容检索**: 方便后续搜索和查阅

---

## 🎯 工作流程

```
用户输入播客URL
       ↓
  获取播客文稿
       ↓
  Claude AI转写
       ↓
  创建飞书文档
       ↓
   返回文档链接
```

---

## ⚡ 性能指标

- **处理速度**: 通常30秒-2分钟
- **支持长度**: 无限制（根据API额度）
- **准确度**: 依赖Claude AI（行业领先水平）
- **成本**: 约$0.01-0.1/次（根据文稿长度）

---

## 🛠️ 技术栈

- **语言**: Python 3.7+
- **AI**: Claude Sonnet 4.5 (Anthropic)
- **API**: 飞书开放平台
- **依赖**: feedparser, requests, lark-oapi, python-dotenv

---

## 📖 文档

- [README.md](./README.md) - 完整使用文档
- [CHANGELOG.md](./CHANGELOG.md) - 版本变更记录
- [config/prompt_template.txt](./config/prompt_template.txt) - Prompt模板示例

---

## 🐛 已知问题

- 小宇宙直接链接支持有限，建议使用RSS feed
- 飞书文档块写入需要完整SDK支持
- 暂不支持音频直接转文字

---

## 🗺️ 后续规划

- [ ] 支持音频直接转文字（Whisper集成）
- [ ] 批量处理多个播客
- [ ] Web界面
- [ ] 更多播客平台支持
- [ ] 优化飞书文档格式
- [ ] 添加缓存机制
- [ ] Docker容器化

---

## 🤝 贡献

欢迎提交Issue和Pull Request！

如果这个项目对你有帮助，请给个⭐️ Star支持一下！

---

## 📄 许可证

MIT License - 详见 [LICENSE](./LICENSE) 文件

---

## 📮 联系方式

- **GitHub**: [weiziqian1990/community-starter-kit](https://github.com/weiziqian1990/community-starter-kit)
- **Issues**: [提交问题](https://github.com/weiziqian1990/community-starter-kit/issues)

---

## 🙏 致谢

感谢以下技术和平台：
- [Anthropic Claude](https://www.anthropic.com/) - 提供强大的AI能力
- [飞书开放平台](https://open.feishu.cn/) - 提供文档API
- 所有贡献者和使用者

---

**祝使用愉快！Happy Podcasting! 🎧**
