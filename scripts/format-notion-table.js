#!/usr/bin/env node

/**
 * AI Leaders Database - Notion Table Formatter
 * Converts AI leaders data to Notion-compatible table format
 */

const fs = require('fs');
const path = require('path');

function formatNotionTable() {
  const dataPath = path.join(__dirname, '../data/ai-leaders.json');
  const data = JSON.parse(fs.readFileSync(dataPath, 'utf8'));

  console.log('# AI领域100位值得关注的领袖\n');
  console.log(`更新时间: ${new Date(data.lastUpdated).toLocaleString('zh-CN')}\n`);
  console.log('---\n');

  // Notion table header
  console.log('| # | 姓名 | 公司 | 职位 | 类别 | 最新访谈 | 核心观点 |');
  console.log('|---|------|------|------|------|----------|----------|');

  // Sort by ID
  const sortedLeaders = data.leaders.sort((a, b) => a.id - b.id);

  sortedLeaders.forEach(leader => {
    const categoryMap = {
      'founder': '创始人',
      'executive': '高管',
      'entrepreneur': '创业者',
      'researcher': '研究者',
      'product_leader': '产品负责人'
    };

    const category = categoryMap[leader.category] || leader.category;

    // Get most recent interview
    let interviewInfo = '待补充';
    let keyPoints = '待补充';

    if (leader.interviews && leader.interviews.length > 0) {
      const latestInterview = leader.interviews.sort((a, b) =>
        new Date(b.date) - new Date(a.date)
      )[0];

      interviewInfo = `[${latestInterview.title}](${latestInterview.url})<br/>📅 ${latestInterview.date}`;

      if (latestInterview.keyPoints && latestInterview.keyPoints.length > 0) {
        keyPoints = latestInterview.keyPoints
          .slice(0, 3) // Show top 3 points
          .map((point, idx) => `${idx + 1}. ${point}`)
          .join('<br/>');
      }
    }

    const name = leader.name;
    const company = leader.company;
    const position = leader.position;

    console.log(`| ${leader.id} | ${name} | ${company} | ${position} | ${category} | ${interviewInfo} | ${keyPoints} |`);
  });

  console.log('\n---\n');
  console.log('## 如何使用这个表格\n');
  console.log('1. 复制上面的Markdown表格');
  console.log('2. 在Notion中创建新页面');
  console.log('3. 粘贴表格内容（Notion会自动识别为表格）');
  console.log('4. 调整列宽和格式以获得更好的视觉效果\n');
  console.log('## 社交媒体链接\n');

  sortedLeaders.forEach(leader => {
    if (leader.twitter || leader.linkedin) {
      console.log(`**${leader.name}**`);
      if (leader.twitter) console.log(`- Twitter: [@${leader.twitter.replace('@', '')}](https://twitter.com/${leader.twitter.replace('@', '')})`);
      if (leader.linkedin) console.log(`- LinkedIn: [Profile](${leader.linkedin})`);
      console.log('');
    }
  });
}

// Export for programmatic use
if (require.main === module) {
  formatNotionTable();
}

module.exports = { formatNotionTable };
