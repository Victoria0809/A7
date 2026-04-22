import streamlit as st
import subprocess
import sys
from components import ner_module, relation_module, kg_visualization
from knowledge import ner_knowledge, re_knowledge, kg_knowledge
from utils import export_report

# 自动下载spaCy模型
try:
    import spacy
    spacy.load("en_core_web_sm")
except Exception as e:
    st.info("正在下载spaCy模型...")
    subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    st.success("模型下载完成！")

def main():
    # 页面配置
    st.set_page_config(
        page_title="信息抽取与知识图谱构建系统",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # 全局样式
    st.markdown("""
    <style>
        :root {
            --primary-color: #1a365d;
            --secondary-color: #3b82f6;
            --accent-color: #8b5cf6;
            --success-color: #10b981;
            --warning-color: #f59e0b;
            --danger-color: #ef4444;
            --card-bg: #ffffff;
            --text-color: #1e293b;
            --border-radius: 10px;
            --box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .stApp {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }
        
        .module-card {
            background: var(--card-bg);
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            transition: transform 0.3s ease;
        }
        
        .module-card:hover {
            transform: translateY(-2px);
        }
        
        .knowledge-panel {
            background: #f8fafc;
            border-left: 4px solid var(--accent-color);
            padding: 1rem;
            margin: 1rem 0;
            border-radius: 0 var(--border-radius) var(--border-radius) 0;
        }
        
        .highlight-person {
            background-color: #ff9999;
            color: #cc0000;
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: 500;
        }
        
        .highlight-organization {
            background-color: #99ccff;
            color: #0066cc;
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: 500;
        }
        
        .highlight-location {
            background-color: #99ff99;
            color: #009900;
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: 500;
        }
        
        .highlight-date {
            background-color: #ffcc99;
            color: #cc6600;
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: 500;
        }
        
        .highlight-gpe {
            background-color: #ff99cc;
            color: #cc0066;
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: 500;
        }
        
        .bio-tag {
            font-family: monospace;
            padding: 2px 6px;
            border-radius: 4px;
            margin-right: 4px;
            font-size: 12px;
        }
        
        .bio-tag-b {
            background-color: #3b82f6;
            color: white;
        }
        
        .bio-tag-i {
            background-color: #60a5fa;
            color: white;
        }
        
        .bio-tag-o {
            background-color: #e2e8f0;
            color: #64748b;
        }
        
        .submit-reminder {
            background-color: #fef3c7;
            border: 1px solid #fbbf24;
            border-radius: var(--border-radius);
            padding: 1rem;
            margin-top: 2rem;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # 顶部导航
    tabs = st.tabs(["📝 实体识别", "🔗 关系抽取", "🌍 知识图谱", "📋 实验报告"])
    
    with tabs[0]:
        ner_module.render_module()
        ner_knowledge.render_knowledge()
    
    with tabs[1]:
        relation_module.render_module()
        re_knowledge.render_knowledge()
    
    with tabs[2]:
        kg_visualization.render_module()
        kg_knowledge.render_knowledge()
    
    with tabs[3]:
        export_report.render_report()
    
    # 底部提交要求提醒
    st.markdown("""
    <div class='submit-reminder'>
        <h3>📦 作业提交要求：</h3>
        <ul>
            <li>实验报告（包含截图和分析）</li>
            <li>完整Streamlit应用代码（app.py + components/）</li>
            <li>核心Python代码文件</li>
            <li>在实验报告中注明使用的AI工具：Trae软件</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()