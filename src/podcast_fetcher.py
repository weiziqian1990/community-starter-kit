"""
播客内容获取模块
支持从RSS feed、小宇宙、Apple Podcasts等平台获取播客文稿
"""

import feedparser
import requests
import re
from typing import Dict, Optional
from urllib.parse import urlparse
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PodcastFetcher:
    """播客内容获取器"""

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    def fetch(self, url: str) -> Dict[str, str]:
        """
        从播客URL获取内容

        Args:
            url: 播客URL（支持RSS feed、单集链接等）

        Returns:
            包含title, content, url等字段的字典
        """
        logger.info(f"开始获取播客内容: {url}")

        # 判断URL类型并调用相应的处理方法
        if self._is_rss_feed(url):
            return self._fetch_from_rss(url)
        elif 'xiaoyuzhoufm.com' in url or 'xyzfm.com' in url:
            return self._fetch_from_xiaoyuzhou(url)
        elif 'apple.com/podcast' in url or 'podcasts.apple.com' in url:
            return self._fetch_from_apple_podcasts(url)
        else:
            # 尝试作为RSS feed处理
            return self._fetch_from_rss(url)

    def _is_rss_feed(self, url: str) -> bool:
        """判断是否为RSS feed URL"""
        return url.endswith('.xml') or url.endswith('.rss') or 'feed' in url.lower()

    def _fetch_from_rss(self, url: str) -> Dict[str, str]:
        """从RSS feed获取播客内容"""
        logger.info("从RSS feed获取内容")

        try:
            feed = feedparser.parse(url)

            if not feed.entries:
                raise ValueError("RSS feed中没有找到任何剧集")

            # 获取最新一集
            entry = feed.entries[0]

            title = entry.get('title', '未知标题')

            # 尝试从多个可能的字段获取内容
            content = ''
            if hasattr(entry, 'content'):
                content = entry.content[0].value
            elif hasattr(entry, 'summary'):
                content = entry.summary
            elif hasattr(entry, 'description'):
                content = entry.description

            # 清理HTML标签
            content = self._clean_html(content)

            return {
                'title': title,
                'content': content,
                'url': entry.get('link', url),
                'published': entry.get('published', ''),
            }

        except Exception as e:
            logger.error(f"从RSS获取内容失败: {e}")
            raise

    def _fetch_from_xiaoyuzhou(self, url: str) -> Dict[str, str]:
        """从小宇宙获取播客内容"""
        logger.info("从小宇宙获取内容")

        try:
            # 小宇宙API端点（可能需要根据实际情况调整）
            # 这里提供一个基础实现，实际可能需要reverse engineer小宇宙的API

            response = requests.get(url, headers=self.headers, timeout=30)
            response.raise_for_status()

            # 从HTML中提取内容（简化版本）
            html = response.text

            # 提取标题
            title_match = re.search(r'<title>(.*?)</title>', html)
            title = title_match.group(1) if title_match else '未知标题'

            # 提取描述/文稿（这里需要根据小宇宙实际HTML结构调整）
            # 这是一个占位实现
            content = "小宇宙播客内容提取功能待完善。建议使用RSS feed URL。"

            logger.warning("小宇宙直接链接支持有限，建议使用RSS feed")

            return {
                'title': title,
                'content': content,
                'url': url,
                'published': '',
            }

        except Exception as e:
            logger.error(f"从小宇宙获取内容失败: {e}")
            raise

    def _fetch_from_apple_podcasts(self, url: str) -> Dict[str, str]:
        """从Apple Podcasts获取播客内容"""
        logger.info("从Apple Podcasts获取内容")

        try:
            # Apple Podcasts通常有对应的RSS feed
            # 需要从页面中提取RSS feed URL

            response = requests.get(url, headers=self.headers, timeout=30)
            response.raise_for_status()

            html = response.text

            # 尝试从HTML中找到RSS feed链接
            rss_match = re.search(r'https?://[^"\']+\.rss', html)
            if rss_match:
                rss_url = rss_match.group(0)
                logger.info(f"找到RSS feed: {rss_url}")
                return self._fetch_from_rss(rss_url)

            # 如果找不到RSS，提取页面内容
            title_match = re.search(r'<title>(.*?)</title>', html)
            title = title_match.group(1) if title_match else '未知标题'

            return {
                'title': title,
                'content': "Apple Podcasts内容提取功能待完善。建议使用RSS feed URL。",
                'url': url,
                'published': '',
            }

        except Exception as e:
            logger.error(f"从Apple Podcasts获取内容失败: {e}")
            raise

    def _clean_html(self, html: str) -> str:
        """清理HTML标签，保留纯文本"""
        if not html:
            return ''

        # 移除HTML标签
        text = re.sub(r'<[^>]+>', '', html)
        # 解码HTML实体
        text = text.replace('&nbsp;', ' ')
        text = text.replace('&amp;', '&')
        text = text.replace('&lt;', '<')
        text = text.replace('&gt;', '>')
        text = text.replace('&quot;', '"')
        # 清理多余空白
        text = re.sub(r'\s+', ' ', text).strip()

        return text


if __name__ == '__main__':
    # 测试代码
    fetcher = PodcastFetcher()

    # 示例：获取一个RSS feed
    test_url = input("请输入播客URL: ")
    try:
        result = fetcher.fetch(test_url)
        print(f"\n标题: {result['title']}")
        print(f"发布时间: {result['published']}")
        print(f"内容预览: {result['content'][:200]}...")
    except Exception as e:
        print(f"错误: {e}")
