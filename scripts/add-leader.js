#!/usr/bin/env node

/**
 * AI Leaders Database - Add New Leader
 * Interactive tool to add new AI leaders to the database
 */

const fs = require('fs');
const path = require('path');
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function question(query) {
  return new Promise(resolve => rl.question(query, resolve));
}

async function addLeader() {
  console.log('=== 添加新的AI领袖 ===\n');

  const dataPath = path.join(__dirname, '../data/ai-leaders.json');
  const data = JSON.parse(fs.readFileSync(dataPath, 'utf8'));

  // Get next ID
  const maxId = Math.max(...data.leaders.map(l => l.id), 0);
  const newId = maxId + 1;

  // Collect basic info
  const name = await question('姓名 (中英文): ');
  const company = await question('公司: ');
  const position = await question('职位: ');

  console.log('\n类别选项:');
  console.log('1. founder (创始人)');
  console.log('2. executive (高管)');
  console.log('3. entrepreneur (创业者)');
  console.log('4. researcher (研究者)');
  console.log('5. product_leader (产品负责人)');
  const categoryChoice = await question('选择类别 (1-5): ');

  const categories = ['founder', 'executive', 'entrepreneur', 'researcher', 'product_leader'];
  const category = categories[parseInt(categoryChoice) - 1] || 'entrepreneur';

  // Interview info
  const hasInterview = await question('\n是否添加访谈信息? (y/n): ');

  let interviews = [];
  if (hasInterview.toLowerCase() === 'y') {
    const url = await question('访谈链接 (URL): ');
    const platform = await question('平台 (如: YouTube, Podcast): ');
    const title = await question('访谈标题: ');
    const date = await question('日期 (YYYY-MM-DD): ');
    const duration = await question('时长 (如: 1:30:45): ');

    console.log('\n核心观点 (每行一个，输入空行结束):');
    const keyPoints = [];
    while (true) {
      const point = await question('> ');
      if (!point.trim()) break;
      keyPoints.push(point);
    }

    interviews.push({
      url,
      platform,
      title,
      date,
      duration,
      keyPoints
    });
  }

  // Social media
  const twitter = await question('\nTwitter handle (可选): ');
  const linkedin = await question('LinkedIn URL (可选): ');
  const notes = await question('备注 (可选): ');

  // Create new leader object
  const newLeader = {
    id: newId,
    name,
    company,
    position,
    category,
    interviews
  };

  if (twitter) newLeader.twitter = twitter;
  if (linkedin) newLeader.linkedin = linkedin;
  if (notes) newLeader.notes = notes;

  // Add to data
  data.leaders.push(newLeader);
  data.lastUpdated = new Date().toISOString();

  // Save
  fs.writeFileSync(dataPath, JSON.stringify(data, null, 2));

  console.log('\n✅ 成功添加新领袖:');
  console.log(JSON.stringify(newLeader, null, 2));
  console.log(`\n当前总数: ${data.leaders.length} 位领袖`);

  rl.close();
}

if (require.main === module) {
  addLeader().catch(console.error);
}

module.exports = { addLeader };
