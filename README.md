# 播客转写到飞书 (Podcast to Feishu)

一键将播客内容转写并保存到飞书文档的自动化工具。

## 功能特性

- **播客内容获取**: 支持RSS feed、小宇宙、Apple Podcasts等多种播客平台
- **AI智能转写**: 使用Claude AI对播客文稿进行智能整理和结构化
- **自动写入飞书**: 将转写后的内容自动创建为飞书文档
- **自定义Prompt**: 支持自定义转写提示词模板
- **命令行工具**: 简单易用的CLI界面

## 工作流程

```
输入播客URL → 获取文稿 → AI转写处理 → 写入飞书文档
```

## 安装

### 1. 克隆仓库

```bash
git clone https://github.com/yourusername/community-starter-kit.git
cd community-starter-kit
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置环境变量

复制环境变量示例文件：

```bash
cp .env.example .env
```

编辑 `.env` 文件，填入你的配置：

```bash
# Claude API配置
ANTHROPIC_API_KEY=sk-ant-xxxxx

# 飞书应用配置
FEISHU_APP_ID=cli_xxxxx
FEISHU_APP_SECRET=xxxxx
```

## 配置说明

### 获取 Claude API Key

1. 访问 [Anthropic Console](https://console.anthropic.com/)
2. 注册/登录账号
3. 创建API Key
4. 将Key填入 `.env` 文件的 `ANTHROPIC_API_KEY`

### 获取飞书应用凭证

1. 访问 [飞书开放平台](https://open.feishu.cn/)
2. 创建企业自建应用
3. 获取 App ID 和 App Secret
4. 配置应用权限：
   - 云文档相关权限
   - 创建文档权限
   - 编辑文档权限
5. 将凭证填入 `.env` 文件

### 自定义Prompt模板（可选）

编辑 `config/prompt_template.txt` 文件来自定义AI转写的行为。

模板中使用以下占位符：
- `{transcript}`: 播客原始文稿
- `{title}`: 播客标题（可选）

## 使用方法

### 基本用法

```bash
python src/main.py --url "https://example.com/podcast.rss"
```

### 使用自定义Prompt模板

```bash
python src/main.py --url "https://example.com/podcast.rss" \
  --prompt config/custom_prompt.txt
```

### 指定飞书文件夹

```bash
python src/main.py --url "https://example.com/podcast.rss" \
  --folder "fldcnxxxxxx"
```

### 自定义文档标题

```bash
python src/main.py --url "https://example.com/podcast.rss" \
  --title "我的播客笔记"
```

### 完整示例

```bash
python src/main.py \
  --url "https://feeds.example.com/podcast.rss" \
  --prompt config/prompt_template.txt \
  --folder "fldcn123456" \
  --title "[AI播客] 技术分享第10期"
```

## 支持的播客平台

### RSS Feed（推荐）

最通用的方式，大多数播客平台都提供RSS feed：

```bash
python src/main.py --url "https://feeds.example.com/podcast.rss"
```

### 小宇宙

直接使用小宇宙链接（部分支持）：

```bash
python src/main.py --url "https://www.xiaoyuzhoufm.com/episode/xxxxx"
```

**注意**: 建议使用小宇宙的RSS feed以获得更好的支持。

### Apple Podcasts

使用Apple Podcasts链接：

```bash
python src/main.py --url "https://podcasts.apple.com/podcast/id123456"
```

## 项目结构

```
community-starter-kit/
├── src/
│   ├── main.py              # 主程序入口
│   ├── podcast_fetcher.py   # 播客内容获取模块
│   ├── ai_transformer.py    # AI转写处理模块
│   └── feishu_writer.py     # 飞书文档写入模块
├── config/
│   ├── config.yaml          # 配置文件
│   └── prompt_template.txt  # Prompt模板
├── requirements.txt         # Python依赖
├── .env.example            # 环境变量示例
└── README.md               # 项目文档
```

## 常见问题

### Q: 如何获取播客的RSS feed？

A: 大多数播客平台都提供RSS feed：
- **小宇宙**: 播客主页 → 分享 → 复制RSS链接
- **Apple Podcasts**: 右键播客 → 复制节目链接，然后在浏览器中查看源代码找RSS
- **Spotify**: 部分播客提供RSS，可在播客描述中查找

### Q: 转写需要多长时间？

A: 通常在30秒到2分钟之间，取决于：
- 文稿长度
- AI处理速度
- 网络状况

### Q: 支持音频直接转文字吗？

A: 当前版本主要支持已有文稿的播客。如需音频转文字功能，可以：
1. 使用Whisper等工具先转成文字
2. 提issue或PR添加该功能

### Q: 如何修改转写的风格？

A: 编辑 `config/prompt_template.txt` 文件，调整AI转写的提示词。

### Q: 费用如何计算？

A:
- **Claude API**: 按token计费，通常每次转写约0.01-0.1美元
- **飞书API**: 企业自建应用免费

### Q: 遇到错误怎么办？

A:
1. 检查环境变量配置是否正确
2. 确认API密钥有效
3. 查看日志输出的错误信息
4. 提交issue寻求帮助

## 开发计划

- [ ] 支持音频直接转文字（集成Whisper）
- [ ] 支持批量处理多个播客
- [ ] 添加Web界面
- [ ] 支持更多播客平台
- [ ] 优化飞书文档格式
- [ ] 添加缓存机制

## 贡献

欢迎提交Issue和Pull Request！

## 许可证

MIT License

## 联系方式

如有问题或建议，请提交Issue或联系作者。

---

**开始使用**:

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 配置环境变量
cp .env.example .env
# 编辑 .env 填入你的配置

# 3. 运行
python src/main.py --url "你的播客URL"
```
