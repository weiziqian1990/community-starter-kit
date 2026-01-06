#!/bin/bash
# 一键启动微信表情切图工具 Web 版本
# Quick start script for WeChat Image Slicer web version

echo "=================================="
echo "微信表情切图工具 - Web 版本"
echo "WeChat Image Slicer - Web Version"
echo "=================================="
echo ""

# 检查Python是否安装
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "❌ 错误: 未找到 Python"
    echo "❌ Error: Python not found"
    echo "请先安装 Python 3.7 或更高版本"
    echo "Please install Python 3.7 or higher first"
    exit 1
fi

# 使用 python3 或 python
PYTHON_CMD="python3"
if ! command -v python3 &> /dev/null; then
    PYTHON_CMD="python"
fi

echo "✓ 找到 Python: $($PYTHON_CMD --version)"
echo ""

# 检查是否已安装依赖
echo "📦 检查依赖..."
if ! $PYTHON_CMD -c "import streamlit" 2>/dev/null; then
    echo "⚠ 未安装依赖，正在安装..."
    echo "Installing dependencies..."
    $PYTHON_CMD -m pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "❌ 依赖安装失败"
        echo "❌ Failed to install dependencies"
        exit 1
    fi
    echo "✓ 依赖安装完成"
else
    echo "✓ 依赖已安装"
fi

echo ""
echo "=================================="
echo "🚀 启动 Web 应用..."
echo "🚀 Starting web application..."
echo "=================================="
echo ""
echo "浏览器将自动打开 http://localhost:8501"
echo "Browser will open at http://localhost:8501"
echo ""
echo "按 Ctrl+C 停止服务器"
echo "Press Ctrl+C to stop the server"
echo ""

# 启动 Streamlit
$PYTHON_CMD -m streamlit run app.py
