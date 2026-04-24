import streamlit as st

def render_knowledge():
    # 知识点总结面板
    with st.expander("📚 命名实体识别 (NER) 知识点总结"):
        # 模块1使用蓝色标题
        st.markdown("<h3 style='color: #3b82f6;'>核心概念</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class='knowledge-panel'>
        <ul>
            <li>命名实体识别是从非结构化文本中抽取具有特定意义的实体词（人名、地名、机构名、专有名词等）</li>
            <li>包含两个关键步骤：实体边界判断 + 实体类别判断</li>
            <li>主要挑战：歧义问题（同一名称在不同上下文指代不同类型）和未登录词问题</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3 style='color: #3b82f6;'>实体类型</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class='knowledge-panel'>
        <ul>
            <li>非嵌套命名实体：每个单词只对应一个标签，使用BIO标注体系</li>
            <ul>
                <li>B-X：实体开头（Begin）</li>
                <li>I-X：实体中间（Inside）</li>
                <li>O：非实体（Outside）</li>
            </ul>
            <li>嵌套命名实体：实体内部包含其他实体</li>
            <ul>
                <li>例如："University of California, Los Angeles"中</li>
                <li>"University of California" 是机构名</li>
                <li>"Los Angeles" 是地名</li>
                <li>整体"University of California, Los Angeles"是机构名</li>
                <li>挑战：单层BIO标注无法表示嵌套结构</li>
            </ul>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3 style='color: #3b82f6;'>标注体系演进</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class='knowledge-panel'>
        <ul>
            <li>BIO：基础标注，无法处理实体边界重叠</li>
            <li>BIOES：增强版，增加E（End）和S（Single）标签</li>
            <ul>
                <li>S-X：单个词的实体</li>
                <li>E-X：实体结尾</li>
            </ul>
            <li>改进：使用多层标注或图结构标注处理嵌套实体</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3 style='color: #3b82f6;'>主流算法</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class='knowledge-panel'>
        <ul>
            <li>基于序列标注：HMM、CRF、BiLSTM-CRF</li>
            <li>基于Transformer：BERT-BiLSTM-CRF架构</li>
            <ul>
                <li>BERT提供上下文词向量</li>
                <li>BiLSTM捕获序列依赖</li>
                <li>CRF确保标签一致性</li>
            </ul>
            <li>中文NER特殊挑战：</li>
            <ul>
                <li>无明确词边界</li>
                <li>需要结合分词信息</li>
                <li>常用Lattice LSTM融合词典知识</li>
            </ul>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3 style='color: #3b82f6;'>评价指标</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class='knowledge-panel'>
        <ul>
            <li>精确率(Precision) = 正确识别的实体数 / 识别的总实体数</li>
            <li>召回率(Recall) = 正确识别的实体数 / 真实实体总数</li>
            <li>F1值 = 2 × (Precision × Recall) / (Precision + Recall)</li>
            <li>宏平均F1：对所有实体类别平等对待</li>
            <li>微平均F1：对每个实体个体平等对待</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3 style='color: #3b82f6;'>学生观察任务</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class='knowledge-panel'>
        <ul>
            <li>输入文本："Steve Jobs founded Apple in California."</li>
            <li>观察高亮效果：Steve Jobs (Person), Apple (Organization), California (Location)</li>
            <li>切换BIO模式，观察标注序列：B-PER I-PER O B-ORG I-ORG O B-LOC I-LOC</li>
            <li>思考嵌套实体：输入"University of California, Los Angeles"，分析为什么单层BIO标注无法同时标注"University of California"和"Los Angeles"</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # 复制按钮
        if st.button("复制知识点内容", key="ner_knowledge_copy"):
            knowledge_content = """
命名实体识别 (NER) 知识点总结

核心概念：
- 命名实体识别是从非结构化文本中抽取具有特定意义的实体词（人名、地名、机构名、专有名词等）
- 包含两个关键步骤：实体边界判断 + 实体类别判断
- 主要挑战：歧义问题（同一名称在不同上下文指代不同类型）和未登录词问题

实体类型：
- 非嵌套命名实体：每个单词只对应一个标签，使用BIO标注体系
  - B-X：实体开头（Begin）
  - I-X：实体中间（Inside）
  - O：非实体（Outside）
- 嵌套命名实体：实体内部包含其他实体
  - 例如："University of California, Los Angeles"中
    - "University of California" 是机构名
    - "Los Angeles" 是地名
    - 整体"University of California, Los Angeles"是机构名
  - 挑战：单层BIO标注无法表示嵌套结构

标注体系演进：
- BIO：基础标注，无法处理实体边界重叠
- BIOES：增强版，增加E（End）和S（Single）标签
  - S-X：单个词的实体
  - E-X：实体结尾
- 改进：使用多层标注或图结构标注处理嵌套实体

主流算法：
- 基于序列标注：HMM、CRF、BiLSTM-CRF
- 基于Transformer：BERT-BiLSTM-CRF架构
  - BERT提供上下文词向量
  - BiLSTM捕获序列依赖
  - CRF确保标签一致性
- 中文NER特殊挑战：
  - 无明确词边界
  - 需要结合分词信息
  - 常用Lattice LSTM融合词典知识

评价指标：
- 精确率(Precision) = 正确识别的实体数 / 识别的总实体数
- 召回率(Recall) = 正确识别的实体数 / 真实实体总数
- F1值 = 2 × (Precision × Recall) / (Precision + Recall)
- 宏平均F1：对所有实体类别平等对待
- 微平均F1：对每个实体个体平等对待

学生观察任务：
- 输入文本："Steve Jobs founded Apple in California."
- 观察高亮效果：Steve Jobs (Person), Apple (Organization), California (Location)
- 切换BIO模式，观察标注序列：B-PER I-PER O B-ORG I-ORG O B-LOC I-LOC
- 思考嵌套实体：输入"University of California, Los Angeles"，分析为什么单层BIO标注无法同时标注"University of California"和"Los Angeles"
            """
            import pyperclip
            pyperclip.copy(knowledge_content)
            st.success("知识点内容已复制到剪贴板！")
