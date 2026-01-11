"""
播客转写到飞书 - Python包
Podcast to Feishu Document Transcription Tool
"""

__version__ = '1.0.0'
__author__ = 'Your Name'
__description__ = '一键将播客内容转写并保存到飞书文档的自动化工具'

from .podcast_fetcher import PodcastFetcher
from .ai_transformer import AITransformer
from .feishu_writer import FeishuWriter

__all__ = ['PodcastFetcher', 'AITransformer', 'FeishuWriter']
