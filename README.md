# 家庭历史展览馆 📸

一个现代化的家庭照片展览馆应用，可以批量导入iPhone照片，自动按时间线组织，并使用AI生成温馨的家庭故事。

## 项目简介

这是一个基于 React + TypeScript + Vite 构建的现代化 Web 应用，旨在帮助您整理和展示家庭照片，让珍贵的回忆以时间线的形式呈现，并通过 AI 技术为每段时光创作温馨的故事。

## 主要功能

- **📤 批量照片上传**：支持拖拽上传多张照片，自动处理
- **📅 智能时间线**：自动提取照片 EXIF 数据，按时间排序和分组
- **🤖 AI 故事生成**：使用 Claude AI 分析照片并生成温馨的家庭故事
- **📷 EXIF 数据提取**：显示拍摄时间、地点、设备等信息
- **🎨 精美界面**：现代化的渐变设计和流畅的动画效果

## 快速开始

```bash
# 进入项目目录
cd family-gallery

# 安装依赖
npm install

# 启动开发服务器
npm run dev

# 构建生产版本
npm run build
```

应用将在 http://localhost:5173 启动

## 使用说明

1. **配置 API Key**
   - 点击右上角设置按钮
   - 在 [Anthropic Console](https://console.anthropic.com/) 获取 API Key
   - 输入并保存

2. **上传照片**
   - 拖拽照片到上传区域，或点击选择文件
   - 支持批量上传多张照片
   - 自动提取 EXIF 数据

3. **查看时间线**
   - 照片自动按年月分组
   - 时间线从最近到最早排列
   - 每组显示照片缩略图

4. **生成 AI 故事**
   - 点击"生成这段时期的故事"按钮
   - AI 分析照片信息并创作故事

## 技术栈

- React 18 + TypeScript
- Vite 构建工具
- Tailwind CSS 样式框架
- exifr - EXIF 数据提取
- @anthropic-ai/sdk - Claude AI 集成
- lucide-react - 图标库

## 项目结构

```
family-gallery/
├── src/
│   ├── components/          # React 组件
│   │   ├── PhotoUploader.tsx
│   │   └── Timeline.tsx
│   ├── utils/              # 工具函数
│   │   ├── exifExtractor.ts
│   │   └── storyGenerator.ts
│   ├── types.ts            # TypeScript 类型定义
│   ├── App.tsx             # 主应用组件
│   └── main.tsx            # 应用入口
├── package.json
└── README.md
```

## 注意事项

- API Key 存储在浏览器的 localStorage 中
- 照片仅在浏览器中处理，不会上传到服务器
- 建议使用现代浏览器（Chrome、Firefox、Safari、Edge）
- 照片文件应包含 EXIF 数据以获得最佳体验

## 许可证

MIT License

---

使用 ❤️ 和 AI 构建
