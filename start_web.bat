@echo off
REM 一键启动微信表情切图工具 Web 版本 (Windows)
REM Quick start script for WeChat Image Slicer web version (Windows)

echo ==================================
echo 微信表情切图工具 - Web 版本
echo WeChat Image Slicer - Web Version
echo ==================================
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ 错误: 未找到 Python
    echo ❌ Error: Python not found
    echo 请先安装 Python 3.7 或更高版本
    echo Please install Python 3.7 or higher first
    pause
    exit /b 1
)

echo ✓ 找到 Python
python --version
echo.

REM 检查是否已安装依赖
echo 📦 检查依赖...
python -c "import streamlit" 2>nul
if %errorlevel% neq 0 (
    echo ⚠ 未安装依赖，正在安装...
    echo Installing dependencies...
    python -m pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo ❌ 依赖安装失败
        echo ❌ Failed to install dependencies
        pause
        exit /b 1
    )
    echo ✓ 依赖安装完成
) else (
    echo ✓ 依赖已安装
)

echo.
echo ==================================
echo 🚀 启动 Web 应用...
echo 🚀 Starting web application...
echo ==================================
echo.
echo 浏览器将自动打开 http://localhost:8501
echo Browser will open at http://localhost:8501
echo.
echo 按 Ctrl+C 停止服务器
echo Press Ctrl+C to stop the server
echo.

REM 启动 Streamlit
python -m streamlit run app.py
