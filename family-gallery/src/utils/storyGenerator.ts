import Anthropic from '@anthropic-ai/sdk';
import type { PhotoGroup } from '../types';

export async function generateStory(group: PhotoGroup, apiKey: string): Promise<string> {
  if (!apiKey) {
    return '请配置 Anthropic API Key 以使用 AI 故事生成功能。';
  }

  const client = new Anthropic({
    apiKey,
    dangerouslyAllowBrowser: true, // 注意：生产环境应该使用后端API
  });

  // 构建照片描述
  const photoDescriptions = group.photos.map((photo, index) => {
    const date = photo.timestamp.toLocaleDateString('zh-CN');
    const time = photo.timestamp.toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit' });
    const camera = photo.exifData?.camera || '未知设备';
    const location = photo.exifData?.location
      ? `(${photo.exifData.location.latitude?.toFixed(4)}, ${photo.exifData.location.longitude?.toFixed(4)})`
      : '';

    return `照片 ${index + 1}: 拍摄于 ${date} ${time}，使用 ${camera} ${location}`;
  }).join('\n');

  const prompt = `你是一位温暖、富有感情的家庭故事讲述者。我有一组家庭照片，拍摄于 ${group.year} 年 ${group.month + 1} 月，共 ${group.photos.length} 张。

照片信息：
${photoDescriptions}

请根据这些照片的时间、拍摄设备等信息，创作一段温馨、有意义的家庭故事。故事应该：
1. 体现这段时期可能发生的家庭生活场景
2. 温馨、感人，充满情感
3. 200-300字左右
4. 用中文书写
5. 不要重复照片信息，而是要想象和描述这段时期的生活场景和情感

请直接输出故事内容，不需要其他说明。`;

  try {
    const message = await client.messages.create({
      model: 'claude-3-5-sonnet-20241022',
      max_tokens: 1024,
      messages: [
        {
          role: 'user',
          content: prompt,
        },
      ],
    });

    const content = message.content[0];
    if (content.type === 'text') {
      return content.text;
    }

    return '抱歉，无法生成故事。';
  } catch (error) {
    console.error('Error generating story:', error);
    return `生成故事时出错：${error instanceof Error ? error.message : '未知错误'}`;
  }
}
