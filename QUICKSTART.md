# 🚀 快速开始指南

欢迎使用AI领袖信息策划系统！这个指南会帮助你在5分钟内上手。

## 📦 安装

这个项目不需要安装任何依赖，只需要Node.js即可运行。

**环境要求**:
- Node.js 14.0 或更高版本
- Git（用于版本控制和自动推送）

检查你的Node.js版本：
```bash
node --version
```

## 🎯 核心功能快速体验

### 1️⃣ 查看Notion表格（最常用）

```bash
# 方式1: 直接查看
npm run notion

# 方式2: 保存到文件
npm run notion:save
```

然后：
1. 打开生成的 `notion-table.md` 文件
2. 复制全部内容
3. 在Notion中新建页面，粘贴
4. Notion会自动识别为数据库表格 ✨

### 2️⃣ 生成每日报告

```bash
# 方式1: 在终端查看
npm run report

# 方式2: 保存到文件
npm run report:save
```

报告会保存在 `reports/` 目录下，以日期命名。

### 3️⃣ 添加新的AI领袖

```bash
npm run add
```

这会启动交互式命令行工具，一步步引导你输入信息。

### 4️⃣ 查看数据库统计

```bash
npm run stats
```

显示当前数据库的统计信息：
- 总人数
- 各类别人数
- 已有访谈的人数

### 5️⃣ 验证数据格式

```bash
npm run validate
```

检查 `data/ai-leaders.json` 是否是有效的JSON格式。

## 📝 手动编辑数据

如果你更喜欢直接编辑JSON文件：

```bash
# 使用你喜欢的编辑器打开
vim data/ai-leaders.json
# 或
code data/ai-leaders.json
```

**数据格式示例**:
```json
{
  "id": 21,
  "name": "新领袖名字（中英文）",
  "company": "公司名称",
  "position": "职位",
  "category": "founder",
  "interviews": [
    {
      "url": "https://youtube.com/watch?v=xxx",
      "platform": "YouTube",
      "title": "访谈标题",
      "date": "2024-12-01",
      "duration": "1:30:00",
      "keyPoints": [
        "核心观点1",
        "核心观点2",
        "核心观点3"
      ]
    }
  ],
  "twitter": "@username",
  "linkedin": "https://linkedin.com/in/username",
  "notes": "备注说明"
}
```

编辑后记得验证：
```bash
npm run validate
```

## ⚙️ 设置自动化推送

### GitHub Actions自动运行

项目已配置好GitHub Actions，会在每天北京时间9:00 AM自动：
- ✅ 生成每日报告
- ✅ 更新Notion表格
- ✅ 创建GitHub Issue
- ✅ 提交到仓库

**无需任何配置，push到GitHub后自动生效！**

### 手动触发GitHub Actions

1. 进入你的GitHub仓库
2. 点击 **Actions** 标签
3. 选择 **Daily AI Leaders Report**
4. 点击 **Run workflow** 按钮

### 接收通知

**方式1: GitHub通知（推荐）**
- 在仓库页面点击 "Watch" → "Custom" → 勾选 "Issues"
- 每日报告会作为Issue创建，你会收到通知

**方式2: 邮件通知**
- GitHub会发送邮件通知（如果你启用了邮件通知）
- 可以在GitHub设置中配置通知偏好

**方式3: RSS订阅**
- 订阅仓库的Issues RSS Feed
- URL格式: `https://github.com/用户名/仓库名/issues.atom`

## 📊 数据质量标准

添加新领袖时，请确保：

✅ **基本信息完整**
- 姓名（中英文都有更好）
- 公司和职位清晰
- 类别选择准确

✅ **访谈质量高**
- 至少20分钟的深度对话
- 有实质性内容，不是简单采访
- 链接有效可访问

✅ **核心观点总结好**
- 至少3个核心观点
- 每个观点清晰、有价值
- 用自己的话总结，不是复制粘贴

## 🎨 Notion使用技巧

### 基础操作

1. **创建数据库**
   - 运行 `npm run notion:save`
   - 复制 `notion-table.md` 内容
   - 粘贴到Notion → 自动创建数据库

2. **添加视图**
   - 点击数据库右上角 "+ Add a view"
   - 创建不同的筛选视图：
     - 只看创始人
     - 只看已有访谈
     - 按公司分组

3. **添加自定义属性**
   - 点击表格右上角 "..."
   - "Customize page"
   - 添加你需要的列（标签、日期等）

### 高级技巧

**过滤器示例**:
- 只看创始人：类别 = "创始人"
- 最近访谈：访谈日期 > 2024-01-01
- 特定公司：公司 contains "OpenAI"

**排序**:
- 按访谈日期排序（最新的在前）
- 按公司字母顺序
- 按ID顺序

**分组**:
- 按公司分组
- 按类别分组
- 按年份分组

## 🔍 查找特定信息

### 使用grep搜索

```bash
# 查找特定公司
grep -i "anthropic" data/ai-leaders.json

# 查找特定人物
grep -i "dario" data/ai-leaders.json

# 查找特定关键词
grep -i "transformer" data/ai-leaders.json
```

### 使用JSON工具

如果你安装了 `jq`（JSON处理工具）：

```bash
# 查看所有创始人
jq '.leaders[] | select(.category == "founder") | .name' data/ai-leaders.json

# 统计各类别人数
jq '.leaders | group_by(.category) | map({category: .[0].category, count: length})' data/ai-leaders.json

# 查找特定公司的人
jq '.leaders[] | select(.company == "Anthropic")' data/ai-leaders.json
```

## 🐛 常见问题

### Q: 运行脚本时报错 "Cannot find module"

**解决**: 确保在项目根目录运行命令：
```bash
cd /path/to/community-starter-kit
npm run notion
```

### Q: JSON格式错误

**解决**: 运行验证检查：
```bash
npm run validate
```

查看具体错误信息，通常是少了逗号或引号。

### Q: GitHub Actions没有运行

**解决**:
1. 检查 `.github/workflows/` 文件是否存在
2. 确保push到了正确的分支
3. 在GitHub仓库的 Actions 标签查看日志

### Q: Notion表格格式不对

**解决**:
1. 确保复制了完整的表格内容
2. 在Notion中粘贴时，不要粘贴到代码块
3. 如果还不对，尝试先粘贴到空白页面

### Q: 想修改推送时间

**解决**: 编辑 `.github/workflows/daily-report.yml`：
```yaml
schedule:
  - cron: '0 1 * * *'  # 修改这行
  # 格式: 分 时 日 月 周
  # 例如: '0 2 * * *' = 北京时间10:00 AM
```

## 📚 下一步

现在你已经掌握了基础操作，可以：

1. **扩展数据库** - 添加更多AI领袖（目标100位）
2. **完善信息** - 为现有领袖添加更多访谈
3. **自定义工具** - 修改脚本以满足你的需求
4. **分享知识** - 将Notion表格分享给你的团队

## 💡 使用场景

**个人学习**:
- 跟踪AI领域最新动态
- 学习顶尖人物的思考方式
- 发现高质量访谈内容

**团队协作**:
- 与团队分享AI行业洞察
- 讨论重要观点和趋势
- 建立共同的知识库

**内容创作**:
- 寻找采访素材
- 了解行业话题
- 发现引用来源

**投资研究**:
- 追踪关键公司和人物
- 了解技术趋势
- 评估市场动态

## 🤝 需要帮助？

- 📖 查看完整文档: [README.md](./README.md)
- 🐛 报告问题: [GitHub Issues](../../issues)
- 💬 讨论想法: [GitHub Discussions](../../discussions)

---

**现在就开始**: `npm run notion:save`

祝你使用愉快！🎉
