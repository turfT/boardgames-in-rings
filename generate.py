#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成静态 HTML 页面的脚本
从三个 txt 文件中读取内容，生成包含随机选择功能的网页
"""

import os
from pathlib import Path


def read_txt_file(filepath):
    """读取 txt 文件，返回非空行的列表"""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    return lines


def generate_html():
    """生成 HTML 文件"""
    # 读取三个 txt 文件
    data_dir = Path(__file__).parent / 'data'
    file1_data = read_txt_file(data_dir / 'file1.txt')
    file2_data = read_txt_file(data_dir / 'file2.txt')
    file3_data = read_txt_file(data_dir / 'file3.txt')
    
    # 将数据转换为 JavaScript 数组格式
    js_data1 = '["' + '", "'.join(file1_data) + '"]'
    js_data2 = '["' + '", "'.join(file2_data) + '"]'
    js_data3 = '["' + '", "'.join(file3_data) + '"]'
    
    html_content = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>随机选择器</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }}
        
        .container {{
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            max-width: 600px;
            width: 100%;
            padding: 40px;
            text-align: center;
        }}
        
        .welcome-screen {{
            display: block;
        }}
        
        .welcome-screen.hidden {{
            display: none;
        }}
        
        .main-screen {{
            display: none;
        }}
        
        .main-screen.show {{
            display: block;
        }}
        
        h1 {{
            color: #333;
            margin-bottom: 20px;
            font-size: 2.5em;
        }}
        
        .welcome-screen h1 {{
            color: #667eea;
            font-size: 3em;
            margin-bottom: 30px;
        }}
        
        .welcome-screen p {{
            color: #666;
            font-size: 1.2em;
            margin-bottom: 40px;
            line-height: 1.6;
        }}
        
        .result-item {{
            background: #f8f9fa;
            border-radius: 12px;
            padding: 20px;
            margin: 20px 0;
            border-left: 4px solid #667eea;
            transition: transform 0.2s, box-shadow 0.2s;
        }}
        
        .result-item:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }}
        
        .result-label {{
            color: #667eea;
            font-size: 0.9em;
            font-weight: 600;
            margin-bottom: 8px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        .result-content {{
            color: #333;
            font-size: 1.3em;
            font-weight: 500;
        }}
        
        .btn {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 15px 40px;
            font-size: 1.1em;
            border-radius: 50px;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
            font-weight: 600;
            margin-top: 30px;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        }}
        
        .btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
        }}
        
        .btn:active {{
            transform: translateY(0);
        }}
        
        .results-container {{
            margin: 30px 0;
        }}
        
        @media (max-width: 600px) {{
            .container {{
                padding: 30px 20px;
            }}
            
            h1 {{
                font-size: 2em;
            }}
            
            .welcome-screen h1 {{
                font-size: 2.2em;
            }}
            
            .welcome-screen p {{
                font-size: 1em;
            }}
            
            .result-content {{
                font-size: 1.1em;
            }}
            
            .btn {{
                padding: 12px 30px;
                font-size: 1em;
                width: 100%;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- 欢迎页面 -->
        <div class="welcome-screen" id="welcomeScreen">
            <h1>🎲 随机选择器</h1>
            <p>欢迎使用随机选择器！<br>点击下方按钮开始随机选择</p>
            <button class="btn" onclick="startApp()">开始</button>
        </div>
        
        <!-- 主功能页面 -->
        <div class="main-screen" id="mainScreen">
            <h1>随机结果</h1>
            <div class="results-container" id="resultsContainer">
                <div class="result-item">
                    <div class="result-label">游戏性+规则（无实体）</div>
                    <div class="result-content" id="result1">-</div>
                </div>
                <div class="result-item">
                    <div class="result-label">主题/背景</div>
                    <div class="result-content" id="result2">-</div>
                </div>
                <div class="result-item">
                    <div class="result-label">美术+配件+实体</div>
                    <div class="result-content" id="result3">-</div>
                </div>
            </div>
            <button class="btn" onclick="reselect()">重新选择</button>
        </div>
    </div>
    
    <script>
        // 数据数组
        const data1 = {js_data1};
        const data2 = {js_data2};
        const data3 = {js_data3};
        
        // 检查是否已经访问过（跳过欢迎页面）
        const hasVisited = localStorage.getItem('hasVisited');
        
        if (hasVisited) {{
            document.getElementById('welcomeScreen').classList.add('hidden');
            document.getElementById('mainScreen').classList.add('show');
            selectRandom();
        }}
        
        function startApp() {{
            localStorage.setItem('hasVisited', 'true');
            document.getElementById('welcomeScreen').classList.add('hidden');
            document.getElementById('mainScreen').classList.add('show');
            selectRandom();
        }}
        
        function getRandomItem(array) {{
            if (array.length === 0) return '';
            const randomIndex = Math.floor(Math.random() * array.length);
            return array[randomIndex];
        }}
        
        function selectRandom() {{
            const item1 = getRandomItem(data1);
            const item2 = getRandomItem(data2);
            const item3 = getRandomItem(data3);
            
            document.getElementById('result1').textContent = item1;
            document.getElementById('result2').textContent = item2;
            document.getElementById('result3').textContent = item3;
        }}
        
        function reselect() {{
            selectRandom();
        }}
    </script>
</body>
</html>'''
    
    # 写入 index.html
    output_path = Path(__file__).parent / 'index.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f'✓ HTML 文件已生成: {output_path}')


if __name__ == '__main__':
    generate_html()

