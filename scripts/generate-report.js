#!/usr/bin/env node

/**
 * AI Leaders Database - Daily Report Generator
 * Generates formatted daily reports for push notifications
 */

const fs = require('fs');
const path = require('path');

function generateDailyReport() {
  const dataPath = path.join(__dirname, '../data/ai-leaders.json');
  const data = JSON.parse(fs.readFileSync(dataPath, 'utf8'));

  const today = new Date().toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    weekday: 'long'
  });

  console.log('# 🌅 AI领袖日报\n');
  console.log(`📅 ${today}\n`);
  console.log('---\n');

  // Stats
  const stats = {
    total: data.leaders.length,
    founders: data.leaders.filter(l => l.category === 'founder').length,
    executives: data.leaders.filter(l => l.category === 'executive').length,
    entrepreneurs: data.leaders.filter(l => l.category === 'entrepreneur').length,
    researchers: data.leaders.filter(l => l.category === 'researcher').length,
    product_leaders: data.leaders.filter(l => l.category === 'product_leader').length,
    withInterviews: data.leaders.filter(l => l.interviews && l.interviews.length > 0).length
  };

  console.log('## 📊 数据概览\n');
  console.log(`- 总计: **${stats.total}** 位AI领袖`);
  console.log(`- 创始人: ${stats.founders} | 高管: ${stats.executives} | 创业者: ${stats.entrepreneurs}`);
  console.log(`- 研究者: ${stats.researchers} | 产品负责人: ${stats.product_leaders}`);
  console.log(`- 已收录访谈: ${stats.withInterviews} 人\n`);

  console.log('---\n');
  console.log('## 🎯 本周推荐关注\n');

  // Featured leaders (random 5)
  const shuffled = [...data.leaders].sort(() => 0.5 - Math.random());
  const featured = shuffled.slice(0, 5);

  featured.forEach((leader, idx) => {
    console.log(`### ${idx + 1}. ${leader.name}`);
    console.log(`**${leader.company}** - ${leader.position}\n`);

    if (leader.interviews && leader.interviews.length > 0) {
      const latestInterview = leader.interviews[0];
      console.log(`🎙️ **最新访谈**: [${latestInterview.title}](${latestInterview.url})`);
      console.log(`📅 ${latestInterview.date} | ⏱️ ${latestInterview.duration}\n`);

      if (latestInterview.keyPoints && latestInterview.keyPoints.length > 0) {
        console.log('**核心观点**:');
        latestInterview.keyPoints.slice(0, 3).forEach(point => {
          console.log(`- ${point}`);
        });
        console.log('');
      }
    }

    if (leader.notes) {
      console.log(`💡 ${leader.notes}\n`);
    }

    console.log('---\n');
  });

  console.log('## 🔗 快速访问\n');
  console.log('- [查看完整Notion表格](./notion-table.md)');
  console.log('- [添加新领袖](./scripts/add-leader.js)');
  console.log('- [数据源文件](./data/ai-leaders.json)\n');

  console.log('---\n');
  console.log('💌 每日 9:00 AM 自动推送 | 由 GitHub Actions 驱动\n');
}

// Save report to file
function saveDailyReport() {
  const reportPath = path.join(__dirname, '../reports');
  if (!fs.existsSync(reportPath)) {
    fs.mkdirSync(reportPath, { recursive: true });
  }

  const date = new Date().toISOString().split('T')[0];
  const fileName = `report-${date}.md`;
  const filePath = path.join(reportPath, fileName);

  // Redirect console output to file
  const originalLog = console.log;
  let output = '';
  console.log = (...args) => {
    output += args.join(' ') + '\n';
  };

  generateDailyReport();

  console.log = originalLog;

  fs.writeFileSync(filePath, output);
  console.log(`✅ 报告已生成: ${filePath}`);

  return filePath;
}

if (require.main === module) {
  const args = process.argv.slice(2);
  if (args.includes('--save')) {
    saveDailyReport();
  } else {
    generateDailyReport();
  }
}

module.exports = { generateDailyReport, saveDailyReport };
