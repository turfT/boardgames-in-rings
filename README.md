# 随机选择器

一个简洁美观的随机选择网页应用，从三个文本文件中随机各选一项内容。

## 功能特点

- 🎲 从三个 txt 文件中随机各选一行
- 🔄 支持重新选择
- 📱 响应式设计，完美适配手机和电脑
- 🎨 简洁现代的 UI 设计
- 👋 欢迎页面引导

## 使用方法

### 本地开发

1. 修改 `data/` 目录下的三个 txt 文件（file1.txt, file2.txt, file3.txt）
2. 运行生成脚本：
   ```bash
   python3 generate.py
   ```
3. 打开生成的 `index.html` 文件即可使用

### GitHub Pages 部署

1. 将代码推送到 GitHub 仓库
2. 在仓库设置中启用 GitHub Pages（使用 GitHub Actions）
3. 每次推送代码到 main/master 分支时，会自动生成并部署

## 文件说明

- `data/` - 存放三个 txt 数据文件
- `generate.py` - Python 生成脚本
- `index.html` - 生成的静态网页（由 generate.py 自动生成）
- `.github/workflows/deploy.yml` - GitHub Actions 自动部署配置

## 技术栈

- Python 3 - 生成静态 HTML
- HTML/CSS/JavaScript - 前端实现
- GitHub Pages - 免费托管
- GitHub Actions - 自动部署

