#!/bin/bash

# 播客转写到飞书 - 使用示例

echo "========================================"
echo "  播客转写到飞书 - 使用示例"
echo "========================================"
echo ""

# 示例1: 基本用法
echo "示例1: 基本用法"
echo "命令: python src/main.py --url \"https://example.com/podcast.rss\""
echo ""

# 示例2: 使用自定义prompt
echo "示例2: 使用自定义prompt模板"
echo "命令: python src/main.py --url \"https://example.com/podcast.rss\" --prompt config/prompt_template.txt"
echo ""

# 示例3: 指定飞书文件夹
echo "示例3: 指定飞书文件夹"
echo "命令: python src/main.py --url \"https://example.com/podcast.rss\" --folder \"fldcnxxxxxx\""
echo ""

# 示例4: 自定义文档标题
echo "示例4: 自定义文档标题"
echo "命令: python src/main.py --url \"https://example.com/podcast.rss\" --title \"我的播客笔记\""
echo ""

# 示例5: 完整示例
echo "示例5: 完整示例"
echo "命令:"
echo "python src/main.py \\"
echo "  --url \"https://feeds.example.com/podcast.rss\" \\"
echo "  --prompt config/prompt_template.txt \\"
echo "  --folder \"fldcn123456\" \\"
echo "  --title \"[AI播客] 技术分享第10期\""
echo ""

# 提示
echo "========================================"
echo "提示："
echo "- 确保已配置 .env 文件"
echo "- RSS feed是最推荐的方式"
echo "- 可以修改 config/prompt_template.txt 自定义转写风格"
echo ""
echo "获取帮助："
echo "python src/main.py --help"
echo "========================================"
