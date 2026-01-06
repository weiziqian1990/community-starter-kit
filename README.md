# 🚀 AI Leaders Curation Project

> 精选100位AI时代最值得关注的领袖人物 | 每日9:00 AM自动推送

[![Daily Report](https://github.com/yourusername/community-starter-kit/actions/workflows/daily-report.yml/badge.svg)](https://github.com/yourusername/community-starter-kit/actions/workflows/daily-report.yml)
[![Update Leaders](https://github.com/yourusername/community-starter-kit/actions/workflows/update-leaders.yml/badge.svg)](https://github.com/yourusername/community-starter-kit/actions/workflows/update-leaders.yml)

## 📋 项目简介

这个项目策划并维护了一个包含100位AI领域顶级人物的数据库，包括：

- 🏢 **顶级公司创始人** - 如Anthropic的Dario Amodei
- 💼 **一线业务负责人** - 如Claude Code负责人Boris Cherny
- 🚀 **AI创业者** - 如Opus Clip创始人Young Dong
- 🔬 **AI研究者** - 如深度学习先驱Yann LeCun
- 📊 **产品领导者** - 领导关键AI产品的负责人

### ✨ 核心功能

- **结构化数据** - JSON格式存储，易于扩展和维护
- **访谈信息** - 收录YouTube、播客等一手访谈源
- **核心观点** - 总结每个访谈的关键洞察
- **Notion导出** - 一键生成Notion表格格式
- **每日推送** - 每天9:00 AM自动生成并推送日报
- **自动化工作流** - GitHub Actions全自动运行

## 📊 当前状态

**数据库规模**: 20位AI领袖（目标100位）

**分类统计**:
- 创始人: 8位
- 高管: 2位
- 创业者: 2位
- 研究者: 6位
- 产品负责人: 2位

**最后更新**: 2026-01-06

## 🚀 快速开始

### 1. 查看数据

```bash
# 查看原始数据
cat data/ai-leaders.json

# 生成Notion表格
node scripts/format-notion-table.js

# 生成每日报告
node scripts/generate-report.js
```

### 2. 添加新领袖

```bash
# 交互式添加
node scripts/add-leader.js

# 或直接编辑 data/ai-leaders.json
```

### 3. 导出到Notion

```bash
# 生成Notion表格并保存
node scripts/format-notion-table.js > notion-table.md

# 然后：
# 1. 打开 notion-table.md
# 2. 复制表格内容
# 3. 粘贴到Notion页面（自动识别为表格）
```

## 📂 项目结构

```
community-starter-kit/
├── data/
│   ├── schema.json          # 数据结构定义
│   └── ai-leaders.json      # AI领袖数据库
├── scripts/
│   ├── format-notion-table.js   # Notion表格生成器
│   ├── add-leader.js           # 添加新领袖工具
│   └── generate-report.js      # 每日报告生成器
├── .github/
│   └── workflows/
│       ├── daily-report.yml    # 每日9AM自动推送
│       └── update-leaders.yml  # 数据更新触发
├── reports/                # 历史报告存档
├── notion-table.md        # Notion表格格式
└── README.md
```

## 🎯 数据模型

每位AI领袖包含以下信息：

```json
{
  "id": 1,
  "name": "姓名（中英文）",
  "company": "公司名称",
  "position": "职位",
  "category": "founder | executive | entrepreneur | researcher | product_leader",
  "interviews": [
    {
      "url": "访谈链接",
      "platform": "平台（YouTube/Podcast等）",
      "title": "访谈标题",
      "date": "日期",
      "duration": "时长",
      "keyPoints": [
        "核心观点1",
        "核心观点2"
      ]
    }
  ],
  "twitter": "Twitter账号",
  "linkedin": "LinkedIn链接",
  "notes": "备注信息"
}
```

## 🔧 使用工具

### 生成Notion表格

```bash
node scripts/format-notion-table.js
```

输出格式化的Markdown表格，可直接粘贴到Notion。

### 添加新领袖

```bash
node scripts/add-leader.js
```

交互式命令行工具，引导你输入所有必要信息。

### 生成每日报告

```bash
# 输出到控制台
node scripts/generate-report.js

# 保存到文件
node scripts/generate-report.js --save
```

生成包含统计数据和推荐关注的每日报告。

## ⚙️ 自动化设置

### 每日9:00 AM推送

项目已配置GitHub Actions在每天北京时间9:00 AM自动：

1. 生成每日报告
2. 更新Notion表格
3. 创建GitHub Issue推送
4. 提交到仓库

**配置文件**: `.github/workflows/daily-report.yml`

**手动触发**:
```bash
# 在GitHub仓库页面
Actions -> Daily AI Leaders Report -> Run workflow
```

### 数据更新自动化

当 `data/ai-leaders.json` 更新时自动：

1. 验证JSON格式
2. 重新生成Notion表格
3. 提交更改
4. 添加统计评论

**配置文件**: `.github/workflows/update-leaders.yml`

## 📧 推送通知设置

### GitHub Issue通知（已启用）

每日报告会自动创建GitHub Issue，你可以：
- 订阅仓库通知
- 配置邮件提醒
- 使用GitHub移动应用接收推送

### 邮件通知（可选）

编辑 `.github/workflows/daily-report.yml`，添加邮件服务配置：

```yaml
- name: Send Email
  uses: dawidd6/action-send-mail@v3
  with:
    server_address: smtp.gmail.com
    server_port: 465
    username: ${{ secrets.EMAIL_USERNAME }}
    password: ${{ secrets.EMAIL_PASSWORD }}
    subject: AI Leaders Daily Report
    to: your-email@example.com
    from: GitHub Actions
    body: file://reports/report-${{ steps.date.outputs.date }}.md
```

### 其他通知渠道

支持集成：
- Slack
- Discord
- Telegram
- 微信企业号
- 钉钉

参考 [GitHub Actions文档](https://docs.github.com/en/actions) 配置。

## 🎨 Notion集成建议

### 基础使用

1. 运行 `node scripts/format-notion-table.js > notion-table.md`
2. 打开Notion，创建新页面
3. 复制 `notion-table.md` 内容并粘贴
4. Notion自动识别为数据库表格

### 高级定制

在Notion中可以添加：
- 标签/多选属性
- 关联关系
- 自定义视图（按公司、类别分组）
- 筛选器（只看创始人、只看已有访谈）
- 排序（按日期、公司等）

### Notion API集成

可以使用Notion API实现自动同步：

```javascript
// 示例：使用@notionhq/client
const { Client } = require('@notionhq/client');
const notion = new Client({ auth: process.env.NOTION_TOKEN });

// 创建或更新数据库条目
// 参考: https://developers.notion.com/
```

## 📈 扩展到100位领袖

### 当前进度: 20/100

### 推荐添加的类别

1. **更多创始人** (20位)
   - AI芯片公司（Cerebras, Graphcore等）
   - AI应用层创业公司
   - 垂直领域AI公司

2. **产品负责人** (20位)
   - Google AI产品负责人
   - Meta AI产品负责人
   - 各大公司AI功能负责人

3. **研究者** (20位)
   - 顶级实验室首席科学家
   - 重要论文第一作者
   - AI安全研究者

4. **投资人和思想领袖** (10位)
   - AI领域顶级投资人
   - 政策制定者
   - AI伦理专家

5. **技术专家** (10位)
   - MLOps专家
   - AI基础设施负责人
   - 开源项目维护者

### 信息来源建议

- YouTube（Lex Fridman Podcast, TED, 公司频道）
- 播客（a16z, Gradient Descent等）
- 会议演讲（NeurIPS, ICML, CVPR等）
- 公司博客和技术文章
- Twitter/X 深度讨论

## 🤝 贡献指南

欢迎贡献！你可以：

### 1. 添加新的AI领袖

使用交互式工具：
```bash
node scripts/add-leader.js
```

或提交Pull Request修改 `data/ai-leaders.json`

### 2. 补充访谈信息

为现有领袖添加新的访谈和观点总结

### 3. 改进工具脚本

优化现有脚本或添加新功能

### 4. 完善文档

改进README、添加使用教程等

### 提交规范

```bash
git checkout -b feature/add-leader-xxx
# 做出更改
git commit -m "Add: [领袖姓名] from [公司]"
git push origin feature/add-leader-xxx
# 创建Pull Request
```

## 📝 数据质量标准

添加新领袖时，请确保：

✅ **必须项**:
- 姓名（中英文）
- 公司和职位
- 至少一个访谈链接
- 至少3个核心观点总结

✅ **推荐项**:
- Twitter账号
- LinkedIn链接
- 补充说明
- 多个访谈源

✅ **质量要求**:
- 访谈应该是深度对话（20分钟以上）
- 核心观点总结清晰、有价值
- 信息准确、链接有效
- 中文翻译准确

## 🔍 已收录领袖速览

<details>
<summary>点击展开完整列表</summary>

1. **Dario Amodei** - Anthropic CEO & Co-founder
2. **Boris Cherny** - Anthropic Head of Claude Code
3. **Sam Altman** - OpenAI CEO
4. **Demis Hassabis** - Google DeepMind CEO
5. **Andrej Karpathy** - AI Researcher & Educator
6. **Young Dong** - Opus Clip Co-founder
7. **Emad Mostaque** - Stability AI Founder
8. **Jensen Huang** - NVIDIA CEO
9. **Yann LeCun** - Meta Chief AI Scientist
10. **Ilya Sutskever** - SSI Co-founder
11. **Satya Nadella** - Microsoft CEO
12. **François Chollet** - Google AI Researcher
13. **Aidan Gomez** - Cohere Co-founder & CEO
14. **Mustafa Suleyman** - Microsoft AI CEO
15. **Jeremy Howard** - fast.ai Co-founder
16. **Fei-Fei Li** - Stanford HAI Co-Director
17. **Noam Shazeer** - Character.AI Co-founder
18. **Nathan Lambert** - AI Research Scientist
19. **Lex Fridman** - AI Researcher & Podcaster
20. **Daniela Amodei** - Anthropic President

[查看详细信息](./data/ai-leaders.json)

</details>

## 📚 资源链接

- [AI领袖数据库](./data/ai-leaders.json)
- [Notion表格](./notion-table.md)
- [每日报告存档](./reports/)
- [数据Schema](./data/schema.json)

## 🙋 FAQ

### Q: 如何修改推送时间？

编辑 `.github/workflows/daily-report.yml`，修改cron表达式：
```yaml
schedule:
  - cron: '0 1 * * *'  # 01:00 UTC = 09:00 Beijing
```

### Q: 如何添加邮件推送？

参考上面"推送通知设置"章节，配置邮件服务。

### Q: 数据可以导出为其他格式吗？

可以！创建新脚本转换为CSV、Excel等格式：
```bash
node scripts/export-csv.js  # 需要自己实现
```

### Q: 如何备份数据？

数据已在Git中版本控制，定期push即可。也可以：
```bash
cp data/ai-leaders.json backup/ai-leaders-$(date +%Y%m%d).json
```

### Q: 可以私有化部署吗？

完全可以！Fork这个仓库，在你自己的私有仓库中使用。

## 📜 开源协议

MIT License - 自由使用、修改、分发

## 🌟 致谢

感谢所有AI领袖们的公开分享和贡献，让我们能够学习他们的经验和见解。

---

**开始使用**: `node scripts/format-notion-table.js`

**有问题？**: [提交Issue](../../issues)

**想贡献？**: [查看贡献指南](#-贡献指南)

让我们一起打造最全面的AI领袖信息库！🚀
