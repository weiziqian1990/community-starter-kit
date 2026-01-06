#!/usr/bin/env python3
"""
WeChat Image Slicer - Streamlit Web Application
微信表情管理页面自动切图工具 - 在线版本
"""

import streamlit as st
from PIL import Image
import io
from pathlib import Path
import tempfile
import zipfile
from wechat_image_slicer import WeChatImageSlicer


# Page configuration
st.set_page_config(
    page_title="微信表情切图工具 | WeChat Sticker Slicer",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .feature-box {
        padding: 1rem;
        background: #f0f2f6;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    .success-box {
        padding: 1rem;
        background: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 8px;
        color: #155724;
    }
</style>
""", unsafe_allow_html=True)


def process_uploaded_image(uploaded_file, output_type='both'):
    """
    处理上传的图片

    Args:
        uploaded_file: Streamlit上传的文件对象
        output_type: 'both', 'avatar', 'icon'

    Returns:
        字典包含处理后的图片数据
    """
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_path = tmp_file.name

    # Create temporary output directory
    output_dir = tempfile.mkdtemp()

    try:
        # Process the image
        slicer = WeChatImageSlicer(tmp_path, output_dir)

        results = {}

        if output_type == 'both' or output_type == 'avatar':
            avatar_path = slicer.generate_avatar()
            with open(avatar_path, 'rb') as f:
                results['avatar'] = {
                    'data': f.read(),
                    'filename': f'avatar_240x240.png',
                    'size': avatar_path.stat().st_size
                }

        if output_type == 'both' or output_type == 'icon':
            icon_path = slicer.generate_icon()
            with open(icon_path, 'rb') as f:
                results['icon'] = {
                    'data': f.read(),
                    'filename': f'icon_50x50.png',
                    'size': icon_path.stat().st_size
                }

        return results

    finally:
        # Cleanup
        Path(tmp_path).unlink(missing_ok=True)


def create_zip(results):
    """创建包含所有图片的ZIP文件"""
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for key, data in results.items():
            zip_file.writestr(data['filename'], data['data'])

    zip_buffer.seek(0)
    return zip_buffer


def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🎨 微信表情切图工具</h1>
        <h3>WeChat Sticker Image Slicer</h3>
        <p>快速生成符合微信表情管理页面要求的图片</p>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar - Instructions
    with st.sidebar:
        st.header("📖 使用说明 | Instructions")

        st.markdown("""
        ### 微信规格要求

        **头像 (Avatar)**
        - 尺寸: 240×240 px
        - 格式: PNG
        - 大小: ≤ 500KB

        **图标 (Icon)**
        - 尺寸: 50×50 px
        - 格式: PNG
        - 大小: ≤ 500KB

        ---

        ### 如何使用

        1. 📤 上传您的图片
        2. ⚙️ 选择输出类型
        3. 🎨 点击"开始处理"
        4. 💾 下载生成的图片

        ---

        ### 支持格式
        - PNG
        - JPG/JPEG
        - BMP
        - GIF
        - WebP
        """)

        st.info("💡 提示：使用高分辨率图片可获得更好的输出质量")

    # Main content
    col1, col2 = st.columns([1, 1])

    with col1:
        st.header("📤 上传图片")

        uploaded_file = st.file_uploader(
            "选择图片文件 | Choose an image file",
            type=['png', 'jpg', 'jpeg', 'bmp', 'gif', 'webp'],
            help="支持常见图片格式，建议使用高分辨率图片"
        )

        if uploaded_file:
            st.success(f"✓ 已上传: {uploaded_file.name}")

            # Display original image
            image = Image.open(uploaded_file)
            st.image(image, caption=f"原图 ({image.width}×{image.height})", use_container_width=True)

            # File info
            file_size_kb = len(uploaded_file.getvalue()) / 1024
            st.info(f"📊 文件大小: {file_size_kb:.1f} KB | 尺寸: {image.width}×{image.height} px")

    with col2:
        st.header("⚙️ 处理选项")

        output_type = st.radio(
            "选择输出类型 | Select output type",
            options=['both', 'avatar', 'icon'],
            format_func=lambda x: {
                'both': '🎯 全部 (头像 + 图标)',
                'avatar': '👤 仅头像 (240×240)',
                'icon': '🔖 仅图标 (50×50)'
            }[x],
            help="选择需要生成的图片类型"
        )

        if uploaded_file:
            if st.button("🎨 开始处理", type="primary", use_container_width=True):
                with st.spinner("⏳ 正在处理图片..."):
                    try:
                        results = process_uploaded_image(uploaded_file, output_type)

                        st.success("✅ 处理完成！")

                        # Display results
                        st.header("💾 下载结果")

                        # Show generated images
                        if 'avatar' in results:
                            st.subheader("👤 头像 (240×240)")
                            avatar_img = Image.open(io.BytesIO(results['avatar']['data']))
                            col_a, col_b = st.columns([1, 1])
                            with col_a:
                                st.image(avatar_img, caption="头像预览", width=240)
                            with col_b:
                                st.download_button(
                                    label=f"📥 下载头像 ({results['avatar']['size']/1024:.1f} KB)",
                                    data=results['avatar']['data'],
                                    file_name=results['avatar']['filename'],
                                    mime="image/png",
                                    use_container_width=True
                                )

                        if 'icon' in results:
                            st.subheader("🔖 图标 (50×50)")
                            icon_img = Image.open(io.BytesIO(results['icon']['data']))
                            col_a, col_b = st.columns([1, 1])
                            with col_a:
                                st.image(icon_img, caption="图标预览", width=100)
                            with col_b:
                                st.download_button(
                                    label=f"📥 下载图标 ({results['icon']['size']/1024:.1f} KB)",
                                    data=results['icon']['data'],
                                    file_name=results['icon']['filename'],
                                    mime="image/png",
                                    use_container_width=True
                                )

                        # Download all as ZIP
                        if len(results) > 1:
                            st.subheader("📦 打包下载")
                            zip_data = create_zip(results)
                            st.download_button(
                                label="📥 下载全部 (ZIP)",
                                data=zip_data,
                                file_name="wechat_stickers.zip",
                                mime="application/zip",
                                use_container_width=True
                            )

                    except Exception as e:
                        st.error(f"❌ 处理失败: {str(e)}")
        else:
            st.info("👆 请先上传图片")

    # Footer
    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-box">
            <h4>🚀 快速处理</h4>
            <p>自动优化图片大小和尺寸</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-box">
            <h4>✅ 符合规范</h4>
            <p>完全符合微信表情管理要求</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-box">
            <h4>🎯 智能裁剪</h4>
            <p>保持比例，居中裁剪</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
        <p>Made with ❤️ | <a href="https://github.com/weiziqian1990/community-starter-kit" target="_blank">GitHub</a></p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == '__main__':
    main()
