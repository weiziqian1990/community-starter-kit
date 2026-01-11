#!/usr/bin/env python3
"""
播客转写到飞书 - Python API使用示例
展示如何在代码中使用各个模块
"""

import sys
import os

# 添加src目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from podcast_fetcher import PodcastFetcher
from ai_transformer import AITransformer
from feishu_writer import FeishuWriter
from dotenv import load_dotenv


def example_basic_usage():
    """示例1: 基本使用流程"""
    print("=" * 60)
    print("示例1: 基本使用流程")
    print("=" * 60)

    # 加载环境变量
    load_dotenv()

    # 1. 获取播客内容
    fetcher = PodcastFetcher()
    podcast_url = "https://example.com/podcast.rss"

    print(f"\n1. 获取播客: {podcast_url}")
    # podcast_data = fetcher.fetch(podcast_url)
    # print(f"   标题: {podcast_data['title']}")

    # 2. AI转写
    print("\n2. AI转写处理...")
    transformer = AITransformer()
    # transformed = transformer.transform(
    #     podcast_data['content'],
    #     podcast_data['title']
    # )

    # 3. 写入飞书
    print("\n3. 写入飞书文档...")
    writer = FeishuWriter()
    # result = writer.create_document(
    #     title=f"[播客] {podcast_data['title']}",
    #     content=transformed
    # )
    # print(f"   文档链接: {result['url']}")


def example_custom_prompt():
    """示例2: 使用自定义prompt"""
    print("\n" + "=" * 60)
    print("示例2: 使用自定义prompt模板")
    print("=" * 60)

    load_dotenv()

    # 创建AI转写器并加载自定义prompt
    transformer = AITransformer()

    custom_prompt = """
请将以下播客文稿转写为简洁的要点列表：

{transcript}
"""

    transformer.set_prompt_template(custom_prompt)
    print("\n✓ 已设置自定义prompt模板")

    # 或从文件加载
    # transformer.load_prompt_from_file('config/prompt_template.txt')


def example_batch_processing():
    """示例3: 批量处理多个播客"""
    print("\n" + "=" * 60)
    print("示例3: 批量处理多个播客")
    print("=" * 60)

    load_dotenv()

    podcast_urls = [
        "https://example.com/podcast1.rss",
        "https://example.com/podcast2.rss",
        "https://example.com/podcast3.rss",
    ]

    fetcher = PodcastFetcher()
    transformer = AITransformer()
    writer = FeishuWriter()

    for i, url in enumerate(podcast_urls, 1):
        print(f"\n处理第 {i}/{len(podcast_urls)} 个播客...")
        try:
            # 获取 -> 转写 -> 写入
            # podcast_data = fetcher.fetch(url)
            # transformed = transformer.transform(
            #     podcast_data['content'],
            #     podcast_data['title']
            # )
            # result = writer.create_document(
            #     title=f"[播客] {podcast_data['title']}",
            #     content=transformed
            # )
            # print(f"✓ 完成: {result['url']}")
            pass
        except Exception as e:
            print(f"✗ 失败: {e}")


def example_custom_config():
    """示例4: 自定义配置"""
    print("\n" + "=" * 60)
    print("示例4: 自定义配置")
    print("=" * 60)

    # 直接传入API密钥（而非从环境变量读取）
    transformer = AITransformer(
        api_key="your-api-key-here"
    )

    writer = FeishuWriter(
        app_id="your-app-id",
        app_secret="your-app-secret"
    )

    print("\n✓ 使用自定义配置初始化")


def example_error_handling():
    """示例5: 错误处理"""
    print("\n" + "=" * 60)
    print("示例5: 错误处理")
    print("=" * 60)

    load_dotenv()

    fetcher = PodcastFetcher()
    url = "https://invalid-url.com/podcast.rss"

    try:
        podcast_data = fetcher.fetch(url)
    except ValueError as e:
        print(f"✗ 值错误: {e}")
    except Exception as e:
        print(f"✗ 其他错误: {e}")


def main():
    """运行所有示例"""
    print("\n" + "=" * 60)
    print("播客转写到飞书 - Python API 使用示例")
    print("=" * 60)

    # 运行各个示例
    example_basic_usage()
    example_custom_prompt()
    example_batch_processing()
    example_custom_config()
    example_error_handling()

    print("\n" + "=" * 60)
    print("示例完成！")
    print("=" * 60)
    print("\n提示:")
    print("- 取消注释代码行以运行实际操作")
    print("- 确保已配置 .env 文件")
    print("- 查看各模块的文档字符串了解更多API")


if __name__ == '__main__':
    main()
