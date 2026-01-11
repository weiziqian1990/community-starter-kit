#!/bin/bash

# 播客转写到飞书 - 安装脚本

echo "========================================"
echo "  播客转写到飞书 v1.0.0 安装向导"
echo "========================================"
echo ""

# 检查Python版本
echo "检查Python环境..."
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: 未找到Python3"
    echo "请先安装Python 3.7或更高版本"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "✓ 找到Python $PYTHON_VERSION"
echo ""

# 创建虚拟环境（可选）
read -p "是否创建Python虚拟环境? (推荐) [Y/n] " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]] || [[ -z $REPLY ]]; then
    echo "创建虚拟环境..."
    python3 -m venv venv

    # 激活虚拟环境
    if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
        source venv/Scripts/activate
    else
        source venv/bin/activate
    fi
    echo "✓ 虚拟环境已创建并激活"
fi
echo ""

# 安装依赖
echo "安装Python依赖包..."
pip install -r requirements.txt
if [ $? -eq 0 ]; then
    echo "✓ 依赖安装完成"
else
    echo "❌ 依赖安装失败"
    exit 1
fi
echo ""

# 配置环境变量
if [ ! -f .env ]; then
    echo "配置环境变量..."
    cp .env.example .env
    echo "✓ 已创建 .env 文件"
    echo ""
    echo "⚠️  请编辑 .env 文件，填入以下信息："
    echo "   - ANTHROPIC_API_KEY (Claude API密钥)"
    echo "   - FEISHU_APP_ID (飞书应用ID)"
    echo "   - FEISHU_APP_SECRET (飞书应用Secret)"
    echo ""
else
    echo "✓ .env 文件已存在"
    echo ""
fi

# 安装完成
echo "========================================"
echo "  ✓ 安装完成！"
echo "========================================"
echo ""
echo "下一步："
echo "1. 编辑 .env 文件，填入API密钥"
echo "2. 运行示例："
echo "   python src/main.py --url \"播客RSS链接\""
echo ""
echo "获取帮助："
echo "   python src/main.py --help"
echo ""
echo "查看文档："
echo "   cat README.md"
echo ""
echo "祝使用愉快！🎧"
