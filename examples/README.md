# 使用示例

本目录包含播客转写到飞书工具的使用示例。

## 文件列表

- `example.sh` - Shell脚本示例，展示各种命令行用法
- `example.py` - Python代码示例，展示如何在代码中使用API

## 运行示例

### Shell示例

```bash
# 查看示例命令
bash examples/example.sh

# 或直接执行
chmod +x examples/example.sh
./examples/example.sh
```

### Python示例

```bash
# 运行Python示例
python examples/example.py
```

**注意**: Python示例中的实际操作代码已被注释，取消注释后即可运行。

## 常见使用场景

### 1. 基本用法

最简单的使用方式：

```bash
python src/main.py --url "https://example.com/podcast.rss"
```

### 2. 自定义转写风格

使用自定义prompt模板：

```bash
python src/main.py \
  --url "https://example.com/podcast.rss" \
  --prompt config/prompt_template.txt
```

### 3. 指定飞书文件夹

将文档保存到特定文件夹：

```bash
python src/main.py \
  --url "https://example.com/podcast.rss" \
  --folder "fldcnxxxxxx"
```

### 4. 批量处理

处理多个播客（需要编写脚本）：

```bash
for url in $(cat podcast_urls.txt); do
  python src/main.py --url "$url"
done
```

### 5. 定时任务

使用cron定时处理新播客：

```bash
# 每天早上8点处理
0 8 * * * cd /path/to/project && python src/main.py --url "https://example.com/podcast.rss"
```

## Python API 使用

在你的Python代码中使用：

```python
from podcast_fetcher import PodcastFetcher
from ai_transformer import AITransformer
from feishu_writer import FeishuWriter

# 获取播客
fetcher = PodcastFetcher()
data = fetcher.fetch("https://example.com/podcast.rss")

# AI转写
transformer = AITransformer()
content = transformer.transform(data['content'], data['title'])

# 写入飞书
writer = FeishuWriter()
result = writer.create_document(title=data['title'], content=content)

print(f"文档链接: {result['url']}")
```

## 自定义Prompt示例

### 提取要点版本

```
请从以下播客文稿中提取3-5个核心要点：

{transcript}
```

### 会议纪要版本

```
请将以下播客内容整理为会议纪要格式：

# 会议主题
# 讨论内容
# 行动项
# 总结

原文：
{transcript}
```

### 知识卡片版本

```
请将以下播客内容整理为知识卡片：

## 标题
## 一句话总结
## 核心内容（3个要点）
## 可行动建议
## 相关资源

原文：
{transcript}
```

## 故障排查

### 问题：无法获取播客内容

**解决方案**:
1. 检查URL是否正确
2. 尝试使用RSS feed而非网页链接
3. 查看日志输出的具体错误

### 问题：AI转写失败

**解决方案**:
1. 检查ANTHROPIC_API_KEY是否正确
2. 确认API额度是否充足
3. 检查网络连接

### 问题：飞书文档创建失败

**解决方案**:
1. 检查飞书应用凭证是否正确
2. 确认应用权限已正确配置
3. 验证folder_token是否有效

## 更多帮助

- 查看 [README.md](../README.md) 了解完整文档
- 查看 [CHANGELOG.md](../CHANGELOG.md) 了解版本更新
- 提交 [Issue](https://github.com/weiziqian1990/community-starter-kit/issues) 寻求帮助
