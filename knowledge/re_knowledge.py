import streamlit as st

def render_knowledge():
    # 知识点总结面板
    with st.expander("📚 关系抽取 (Relation Extraction) 知识点总结"):
        # 模块2使用绿色标题
        st.markdown("<h3 style='color: #10b981;'>核心概念</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class='knowledge-panel'>
        <ul>
            <li>关系抽取是从文本中识别两个或多个实体之间的语义关系</li>
            <li>用三元组&lt;HEAD, RELATION, TAIL&gt;表示结构化知识</li>
            <li>例如：&lt;Steve Jobs, FOUNDER_OF, Apple&gt;表示"Steve Jobs"和"Apple"存在"FOUNDER_OF"关系</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3 style='color: #10b981;'>方法分类</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class='knowledge-panel'>
        <ul>
            <li>按处理流程：</li>
            <ul>
                <li>流水线式（Pipeline）：先NER再RE</li>
                <ul>
                    <li>优点：模块化，易于实现</li>
                    <li>缺点：错误传递，NER错误影响RE结果</li>
                </ul>
                <li>联合式（Joint）：同时完成NER和RE</li>
                <ul>
                    <li>优点：缓解错误传递，利用任务间依赖</li>
                    <li>缺点：模型复杂，训练困难</li>
                </ul>
            </ul>
            <li>按关系类型：</li>
            <ul>
                <li>预定义关系抽取：针对特定领域预先定义的关系类型</li>
                <li>开放关系抽取：不限定领域和关系类别，自动发现关系模式</li>
            </ul>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3 style='color: #10b981;'>主流算法</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class='knowledge-panel'>
        <ul>
            <li>基于特征工程：</li>
            <ul>
                <li>词汇特征：实体间词语、词性标签</li>
                <li>句法特征：依存路径、最短路径</li>
                <li>语义特征：WordNet同义词、语义角色标注</li>
            </ul>
            <li>深度学习方法：</li>
            <ul>
                <li>CNN-based：使用卷积神经网络捕获局部特征</li>
                <li>RNN-based：使用LSTM/GRU捕获序列特征</li>
                <li>Transformer-based：BERT等预训练模型</li>
                <ul>
                    <li>句子级：将整个句子输入BERT</li>
                    <li>实体标记：在实体前后添加特殊标记[E1][E2]</li>
                </ul>
                <li>图神经网络：将句子表示为依存树，使用GNN聚合信息</li>
            </ul>
            <li>远程监督（Distant Supervision）：</li>
            <ul>
                <li>假设：知识库中存在关系的实体对，在所有提及它们的句子中都表达该关系</li>
                <li>挑战：大量错误标注（噪声）</li>
                <li>解决方案：</li>
                <ul>
                    <li>多示例学习：从多个句子中学习关系模式</li>
                    <li>基于注意力机制：为不同句子分配不同权重</li>
                </ul>
            </ul>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3 style='color: #10b981;'>挑战与前沿</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class='knowledge-panel'>
        <ul>
            <li>指代消解：处理代词（如"He", "It"）指向的实际实体</li>
            <li>关系重叠：一个实体参与多个关系</li>
            <li>文档级关系抽取：跨句子、跨段落的关系识别</li>
            <li>少样本/零样本关系抽取：在标注数据有限的情况下学习</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3 style='color: #10b981;'>评价指标</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class='knowledge-panel'>
        <ul>
            <li>预定义关系：精确率、召回率、F1值（通常使用macro-F1）</li>
            <li>开放关系：V-measure（同质性+完整性）、调整兰德系数(ARI)</li>
            <li>端到端评估：考虑NER和RE联合性能</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3 style='color: #10b981;'>学生观察任务</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class='knowledge-panel'>
        <ul>
            <li>输入复杂句子："He, the CEO of Apple Inc., was born in San Francisco and founded the company in 1976."</li>
            <li>观察系统如何处理代词"He"的指代消解（应指向Steve Jobs）</li>
            <li>分析关系抽取如何构建图结构中的边（节点=实体，边=关系）</li>
            <li>思考：为什么关系抽取比实体识别更具挑战性？</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # 复制按钮
        if st.button("复制知识点内容", key="re_knowledge_copy"):
            knowledge_content = """
关系抽取 (Relation Extraction) 知识点总结

核心概念：
- 关系抽取是从文本中识别两个或多个实体之间的语义关系
- 用三元组<HEAD, RELATION, TAIL>表示结构化知识
- 例如：<Steve Jobs, FOUNDER_OF, Apple>表示"Steve Jobs"和"Apple"存在"FOUNDER_OF"关系

方法分类：
- 按处理流程：
  - 流水线式（Pipeline）：先NER再RE
    - 优点：模块化，易于实现
    - 缺点：错误传递，NER错误影响RE结果
  - 联合式（Joint）：同时完成NER和RE
    - 优点：缓解错误传递，利用任务间依赖
    - 缺点：模型复杂，训练困难
- 按关系类型：
  - 预定义关系抽取：针对特定领域预先定义的关系类型
  - 开放关系抽取：不限定领域和关系类别，自动发现关系模式

主流算法：
- 基于特征工程：
  - 词汇特征：实体间词语、词性标签
  - 句法特征：依存路径、最短路径
  - 语义特征：WordNet同义词、语义角色标注
- 深度学习方法：
  - CNN-based：使用卷积神经网络捕获局部特征
  - RNN-based：使用LSTM/GRU捕获序列特征
  - Transformer-based：BERT等预训练模型
    - 句子级：将整个句子输入BERT
    - 实体标记：在实体前后添加特殊标记[E1][E2]
  - 图神经网络：将句子表示为依存树，使用GNN聚合信息
- 远程监督（Distant Supervision）：
  - 假设：知识库中存在关系的实体对，在所有提及它们的句子中都表达该关系
  - 挑战：大量错误标注（噪声）
  - 解决方案：
    - 多示例学习：从多个句子中学习关系模式
    - 基于注意力机制：为不同句子分配不同权重

挑战与前沿：
- 指代消解：处理代词（如"He", "It"）指向的实际实体
- 关系重叠：一个实体参与多个关系
- 文档级关系抽取：跨句子、跨段落的关系识别
- 少样本/零样本关系抽取：在标注数据有限的情况下学习

评价指标：
- 预定义关系：精确率、召回率、F1值（通常使用macro-F1）
- 开放关系：V-measure（同质性+完整性）、调整兰德系数(ARI)
- 端到端评估：考虑NER和RE联合性能

学生观察任务：
- 输入复杂句子："He, the CEO of Apple Inc., was born in San Francisco and founded the company in 1976."
- 观察系统如何处理代词"He"的指代消解（应指向Steve Jobs）
- 分析关系抽取如何构建图结构中的边（节点=实体，边=关系）
- 思考：为什么关系抽取比实体识别更具挑战性？
            """
            import pyperclip
            pyperclip.copy(knowledge_content)
            st.success("知识点内容已复制到剪贴板！")
