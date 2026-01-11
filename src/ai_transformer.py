"""
AI转写处理模块
使用Claude API对播客文稿进行智能转写和格式化
"""

import os
from anthropic import Anthropic
import logging
from typing import Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AITransformer:
    """AI转写处理器"""

    def __init__(self, api_key: Optional[str] = None, prompt_template: Optional[str] = None):
        """
        初始化AI转写器

        Args:
            api_key: Claude API密钥，如果不提供则从环境变量获取
            prompt_template: 转写提示词模板，如果不提供则使用默认模板
        """
        self.api_key = api_key or os.getenv('ANTHROPIC_API_KEY')
        if not self.api_key:
            raise ValueError("请设置ANTHROPIC_API_KEY环境变量或传入api_key参数")

        self.client = Anthropic(api_key=self.api_key)
        self.prompt_template = prompt_template or self._get_default_prompt()

    def _get_default_prompt(self) -> str:
        """获取默认的转写提示词模板"""
        return """请对以下播客文稿进行专业的转写和整理，要求：

1. 提取核心主题和关键观点
2. 整理成清晰的结构化内容（使用Markdown格式）
3. 突出重要信息和金句
4. 添加适当的章节标题
5. 保持原文的语气和风格

请按以下格式输出：

# 播客标题

## 核心要点
- 要点1
- 要点2
- 要点3

## 详细内容

### 第一部分标题
内容...

### 第二部分标题
内容...

## 金句摘录
> 金句1
> 金句2

---

原文稿：
{transcript}
"""

    def transform(self, transcript: str, title: str = "") -> str:
        """
        使用AI对文稿进行转写处理

        Args:
            transcript: 原始文稿内容
            title: 播客标题（可选）

        Returns:
            转写后的格式化内容
        """
        logger.info("开始AI转写处理...")

        if not transcript or len(transcript.strip()) < 10:
            raise ValueError("文稿内容过短或为空")

        try:
            # 构建提示词
            prompt = self.prompt_template.replace('{transcript}', transcript)
            if title and '{title}' in self.prompt_template:
                prompt = prompt.replace('{title}', title)

            # 调用Claude API
            logger.info("调用Claude API...")
            message = self.client.messages.create(
                model="claude-sonnet-4-5-20250929",
                max_tokens=4096,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            # 提取响应内容
            result = message.content[0].text

            logger.info("AI转写完成")
            return result

        except Exception as e:
            logger.error(f"AI转写失败: {e}")
            raise

    def set_prompt_template(self, template: str):
        """
        设置自定义的转写提示词模板

        Args:
            template: 提示词模板，使用{transcript}作为文稿内容占位符
        """
        if '{transcript}' not in template:
            raise ValueError("提示词模板必须包含{transcript}占位符")
        self.prompt_template = template
        logger.info("已更新提示词模板")

    def load_prompt_from_file(self, file_path: str):
        """
        从文件加载提示词模板

        Args:
            file_path: 提示词模板文件路径
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                template = f.read()
            self.set_prompt_template(template)
            logger.info(f"已从文件加载提示词模板: {file_path}")
        except Exception as e:
            logger.error(f"加载提示词模板失败: {e}")
            raise


if __name__ == '__main__':
    # 测试代码
    import sys

    if len(sys.argv) < 2:
        print("用法: python ai_transformer.py <文稿内容>")
        sys.exit(1)

    transformer = AITransformer()

    test_transcript = sys.argv[1]
    try:
        result = transformer.transform(test_transcript, "测试播客")
        print("\n=== 转写结果 ===")
        print(result)
    except Exception as e:
        print(f"错误: {e}")
