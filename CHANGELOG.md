# Changelog

所有重要的项目变更都会记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)。

## [1.0.0] - 2026-01-11

### 新增功能

- **播客内容获取模块** (`podcast_fetcher.py`)
  - 支持RSS feed解析
  - 支持小宇宙播客平台
  - 支持Apple Podcasts
  - HTML内容自动清理
  - 多平台URL智能识别

- **AI智能转写模块** (`ai_transformer.py`)
  - 集成Claude Sonnet 4.5 API
  - 支持自定义prompt模板
  - 文稿智能结构化
  - Markdown格式输出
  - 提取核心要点和金句

- **飞书文档写入模块** (`feishu_writer.py`)
  - 飞书开放平台API集成
  - 自动创建文档
  - Markdown到飞书块的转换
  - 支持标题、列表、引用等格式

- **命令行工具** (`main.py`)
  - 简洁的CLI界面
  - 完整的参数支持
  - 三步自动化流程
  - 详细的日志输出
  - 错误处理机制

### 配置和文档

- 环境变量配置示例 (`.env.example`)
- 项目配置文件 (`config/config.yaml`)
- 默认prompt模板 (`config/prompt_template.txt`)
- 完整的README使用文档
- Python依赖管理 (`requirements.txt`)
- Git忽略配置 (`.gitignore`)

### 技术栈

- Python 3.7+
- Claude API (Anthropic)
- 飞书开放平台API
- feedparser, requests, lark-oapi

### 使用示例

```bash
# 基本用法
python src/main.py --url "https://example.com/podcast.rss"

# 使用自定义prompt
python src/main.py --url "https://example.com/podcast.rss" --prompt config/prompt_template.txt

# 指定飞书文件夹
python src/main.py --url "https://example.com/podcast.rss" --folder "fldcnxxxxxx"
```

### 已知限制

- 小宇宙和Apple Podcasts直接链接支持有限，建议使用RSS feed
- 飞书文档块写入功能需要完整的SDK支持
- 暂不支持音频直接转文字（需要播客提供文稿）

### 后续计划

- 支持音频直接转文字（集成Whisper）
- 支持批量处理多个播客
- 添加Web界面
- 优化飞书文档格式
- 添加缓存机制
- 支持更多播客平台

---

## 版本号说明

本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/) 规范：

- 主版本号：不兼容的API修改
- 次版本号：向下兼容的功能性新增
- 修订号：向下兼容的问题修正
