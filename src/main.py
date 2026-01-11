#!/usr/bin/env python3
"""
播客转写到飞书文档 - 主程序
整合播客获取、AI转写和飞书文档写入功能
"""

import argparse
import os
import sys
import logging
from pathlib import Path
from dotenv import load_dotenv

# 添加src目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from podcast_fetcher import PodcastFetcher
from ai_transformer import AITransformer
from feishu_writer import FeishuWriter

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class PodcastToFeishu:
    """播客转写到飞书主程序"""

    def __init__(self, config_dir: str = None):
        """
        初始化程序

        Args:
            config_dir: 配置文件目录
        """
        # 加载环境变量
        load_dotenv()

        # 配置目录
        self.config_dir = config_dir or os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'config'
        )

        # 初始化各模块
        self.fetcher = PodcastFetcher()
        self.transformer = None  # 延迟初始化，因为可能需要加载prompt模板
        self.writer = None  # 延迟初始化

    def run(self, podcast_url: str, prompt_template_path: str = None,
            folder_token: str = None, custom_title: str = None) -> dict:
        """
        执行完整的转写流程

        Args:
            podcast_url: 播客URL
            prompt_template_path: 自定义prompt模板文件路径
            folder_token: 飞书文件夹token
            custom_title: 自定义文档标题

        Returns:
            包含结果信息的字典
        """
        try:
            # 步骤1: 获取播客内容
            logger.info("=" * 60)
            logger.info("步骤 1/3: 获取播客内容")
            logger.info("=" * 60)
            podcast_data = self.fetcher.fetch(podcast_url)
            logger.info(f"✓ 获取成功: {podcast_data['title']}")

            if not podcast_data['content']:
                raise ValueError("播客内容为空，请检查URL是否正确")

            # 步骤2: AI转写
            logger.info("\n" + "=" * 60)
            logger.info("步骤 2/3: AI智能转写")
            logger.info("=" * 60)

            # 初始化AI转写器
            self.transformer = AITransformer()

            # 如果提供了自定义prompt模板，加载它
            if prompt_template_path:
                logger.info(f"加载自定义prompt模板: {prompt_template_path}")
                self.transformer.load_prompt_from_file(prompt_template_path)

            # 执行转写
            transformed_content = self.transformer.transform(
                podcast_data['content'],
                podcast_data['title']
            )
            logger.info("✓ AI转写完成")

            # 步骤3: 写入飞书文档
            logger.info("\n" + "=" * 60)
            logger.info("步骤 3/3: 写入飞书文档")
            logger.info("=" * 60)

            # 初始化飞书写入器
            self.writer = FeishuWriter()

            # 确定文档标题
            doc_title = custom_title or f"[播客] {podcast_data['title']}"

            # 创建文档
            result = self.writer.create_document(
                title=doc_title,
                content=transformed_content,
                folder_token=folder_token
            )
            logger.info(f"✓ 文档创建成功")

            # 返回结果
            logger.info("\n" + "=" * 60)
            logger.info("✓ 全部完成！")
            logger.info("=" * 60)
            logger.info(f"文档标题: {result['title']}")
            logger.info(f"文档ID: {result['document_id']}")
            logger.info(f"访问链接: {result['url']}")

            return {
                'success': True,
                'podcast_title': podcast_data['title'],
                'document_id': result['document_id'],
                'document_url': result['url'],
                'document_title': result['title']
            }

        except Exception as e:
            logger.error(f"\n✗ 处理失败: {e}")
            return {
                'success': False,
                'error': str(e)
            }


def main():
    """命令行入口"""
    parser = argparse.ArgumentParser(
        description='将播客转写并保存到飞书文档',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  # 基本用法
  python main.py --url "https://example.com/podcast.rss"

  # 使用自定义prompt模板
  python main.py --url "https://example.com/podcast.rss" --prompt config/custom_prompt.txt

  # 指定飞书文件夹
  python main.py --url "https://example.com/podcast.rss" --folder "fldcnxxxxxx"

  # 自定义文档标题
  python main.py --url "https://example.com/podcast.rss" --title "我的播客笔记"

环境变量配置:
  ANTHROPIC_API_KEY  - Claude API密钥（必需）
  FEISHU_APP_ID      - 飞书应用ID（必需）
  FEISHU_APP_SECRET  - 飞书应用Secret（必需）
        """
    )

    parser.add_argument(
        '--url',
        required=True,
        help='播客URL（RSS feed或单集链接）'
    )

    parser.add_argument(
        '--prompt',
        help='自定义prompt模板文件路径'
    )

    parser.add_argument(
        '--folder',
        help='飞书文件夹token（可选）'
    )

    parser.add_argument(
        '--title',
        help='自定义文档标题（可选）'
    )

    parser.add_argument(
        '--config-dir',
        help='配置文件目录（可选）'
    )

    args = parser.parse_args()

    # 检查环境变量
    required_env_vars = ['ANTHROPIC_API_KEY', 'FEISHU_APP_ID', 'FEISHU_APP_SECRET']
    missing_vars = [var for var in required_env_vars if not os.getenv(var)]

    if missing_vars:
        logger.error(f"缺少必需的环境变量: {', '.join(missing_vars)}")
        logger.error("请在.env文件或环境变量中设置这些值")
        sys.exit(1)

    # 执行转写
    app = PodcastToFeishu(config_dir=args.config_dir)
    result = app.run(
        podcast_url=args.url,
        prompt_template_path=args.prompt,
        folder_token=args.folder,
        custom_title=args.title
    )

    # 根据结果退出
    sys.exit(0 if result['success'] else 1)


if __name__ == '__main__':
    main()
