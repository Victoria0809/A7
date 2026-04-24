import streamlit as st

def render_knowledge():
    # 知识点总结面板
    with st.expander("📚 知识图谱与信息抽取整合知识点总结"):
        # 模块3使用紫色标题
        st.markdown("<h3 style='color: #8b5cf6;'>信息抽取在知识图谱中的作用</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class='knowledge-panel'>
        <ul>
            <li>信息抽取是构建知识图谱的核心技术</li>
            <li>从非结构化文本中提取结构化信息：</li>
            <ul>
                <li>命名实体识别 → 知识图谱节点</li>
                <li>关系抽取 → 知识图谱边</li>
                <li>事件抽取 → 复杂关系和时序信息</li>
            </ul>
            <li>转换流程：文本 → 实体/关系 → 三元组 → 知识图谱</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3 style='color: #8b5cf6;'>知识图谱基础概念</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class='knowledge-panel'>
        <ul>
            <li>知识图谱是结构化的语义知识库</li>
            <li>基本组成：实体（节点）、关系（边）、属性（节点/边的特征）</li>
            <li>表示形式：RDF三元组（主体，谓词，客体）</li>
            <li>存储方式：图数据库（Neo4j, Amazon Neptune）、RDF存储（Apache Jena）</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3 style='color: #8b5cf6;'>事件抽取补充</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class='knowledge-panel'>
        <ul>
            <li>事件抽取识别特定类型事件及其元素</li>
            <li>事件组成：</li>
            <ul>
                <li>事件触发词(Trigger)：最清楚表达事件的词（如"acquired", "founded"）</li>
                <li>事件论元(Argument)：事件涉及的参与者</li>
                <li>论元角色：论元在事件中的角色（Agent, Patient, Time, Location等）</li>
            </ul>
            <li>例如："Microsoft acquired GitHub for $7.5 billion in 2018"</li>
            <ul>
                <li>触发词："acquired"</li>
                <li>事件类型："收购"</li>
                <li>论元：</li>
                <ul>
                    <li>Agent: Microsoft (收购方)</li>
                    <li>Patient: GitHub (被收购方)</li>
                    <li>Money: $7.5 billion (金额)</li>
                    <li>Time: 2018 (时间)</li>
                </ul>
            </ul>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3 style='color: #8b5cf6;'>技术演进</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class='knowledge-panel'>
        <ul>
            <li>传统方法：基于规则和统计特征</li>
            <li>深度学习方法：</li>
            <ul>
                <li>基于RNN的联合事件抽取：同时识别触发词和论元</li>
                <li>基于Transformer的端到端事件抽取</li>
                <li>基于预训练模型的少样本事件抽取</li>
            </ul>
            <li>评估标准：</li>
            <ul>
                <li>触发词识别(TI)、触发词分类(TC)</li>
                <li>论元识别(AI)、论元分类(AC)</li>
                <li>整体F1值</li>
            </ul>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3 style='color: #8b5cf6;'>应用场景</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class='knowledge-panel'>
        <ul>
            <li>智能问答：基于知识图谱的精准回答</li>
            <ul>
                <li>例子："谁创立了Apple？" → 通过FOUNDER_OF关系找到答案</li>
            </ul>
            <li>信息检索：通过结构化数据提升检索精度</li>
            <ul>
                <li>例子：搜索"California的大学" → 通过LOCATED_IN关系过滤</li>
            </ul>
            <li>推荐系统：利用图结构发现用户-物品关系</li>
            <ul>
                <li>例子：用户A喜欢公司X，公司X位于城市Y → 推荐城市Y的相关内容</li>
            </ul>
            <li>金融风控：通过关系网络识别欺诈模式</li>
            <ul>
                <li>例子：多个公司共享相同地址/法人 → 潜在关联风险</li>
            </ul>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3 style='color: #8b5cf6;'>可视化最佳实践</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class='knowledge-panel'>
        <ul>
            <li>节点布局：力导向布局适合展示关系密度，层次布局适合展示层级关系</li>
            <li>交互设计：悬停显示详情，点击展开/折叠子图</li>
            <li>性能优化：大型图谱使用聚合、采样、渐进加载策略</li>
            <li>可访问性：为色盲用户提供颜色+形状双重编码</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3 style='color: #8b5cf6;'>学生观察任务</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class='knowledge-panel'>
        <ul>
            <li>输入商业新闻："Microsoft acquired GitHub for $7.5 billion in 2018. Satya Nadella, the CEO of Microsoft, announced this acquisition at the company's headquarters in Redmond, Washington."</li>
            <li>观察知识图谱如何将线性文本转化为网状结构</li>
            <li>分析节点（Microsoft, GitHub, Satya Nadella, Redmond, Washington）和边（ACQUIRED, CEO_OF, LOCATED_IN）的关系</li>
            <li>思考：知识图谱如何帮助理解复杂文本中的隐含关系</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # 复制按钮
        if st.button("复制知识点内容", key="kg_knowledge_copy"):
            knowledge_content = """
知识图谱与信息抽取整合知识点总结

信息抽取在知识图谱中的作用：
- 信息抽取是构建知识图谱的核心技术
- 从非结构化文本中提取结构化信息：
  - 命名实体识别 → 知识图谱节点
  - 关系抽取 → 知识图谱边
  - 事件抽取 → 复杂关系和时序信息
- 转换流程：文本 → 实体/关系 → 三元组 → 知识图谱

知识图谱基础概念：
- 知识图谱是结构化的语义知识库
- 基本组成：实体（节点）、关系（边）、属性（节点/边的特征）
- 表示形式：RDF三元组（主体，谓词，客体）
- 存储方式：图数据库（Neo4j, Amazon Neptune）、RDF存储（Apache Jena）

事件抽取补充：
- 事件抽取识别特定类型事件及其元素
- 事件组成：
  - 事件触发词(Trigger)：最清楚表达事件的词（如"acquired", "founded"）
  - 事件论元(Argument)：事件涉及的参与者
  - 论元角色：论元在事件中的角色（Agent, Patient, Time, Location等）
- 例如："Microsoft acquired GitHub for $7.5 billion in 2018"
  - 触发词："acquired"
  - 事件类型："收购"
  - 论元：
    - Agent: Microsoft (收购方)
    - Patient: GitHub (被收购方)
    - Money: $7.5 billion (金额)
    - Time: 2018 (时间)

技术演进：
- 传统方法：基于规则和统计特征
- 深度学习方法：
  - 基于RNN的联合事件抽取：同时识别触发词和论元
  - 基于Transformer的端到端事件抽取
  - 基于预训练模型的少样本事件抽取
- 评估标准：
  - 触发词识别(TI)、触发词分类(TC)
  - 论元识别(AI)、论元分类(AC)
  - 整体F1值

应用场景：
- 智能问答：基于知识图谱的精准回答
  - 例子："谁创立了Apple？" → 通过FOUNDER_OF关系找到答案
- 信息检索：通过结构化数据提升检索精度
  - 例子：搜索"California的大学" → 通过LOCATED_IN关系过滤
- 推荐系统：利用图结构发现用户-物品关系
  - 例子：用户A喜欢公司X，公司X位于城市Y → 推荐城市Y的相关内容
- 金融风控：通过关系网络识别欺诈模式
  - 例子：多个公司共享相同地址/法人 → 潜在关联风险

可视化最佳实践：
- 节点布局：力导向布局适合展示关系密度，层次布局适合展示层级关系
- 交互设计：悬停显示详情，点击展开/折叠子图
- 性能优化：大型图谱使用聚合、采样、渐进加载策略
- 可访问性：为色盲用户提供颜色+形状双重编码

学生观察任务：
- 输入商业新闻："Microsoft acquired GitHub for $7.5 billion in 2018. Satya Nadella, the CEO of Microsoft, announced this acquisition at the company's headquarters in Redmond, Washington."
- 观察知识图谱如何将线性文本转化为网状结构
- 分析节点（Microsoft, GitHub, Satya Nadella, Redmond, Washington）和边（ACQUIRED, CEO_OF, LOCATED_IN）的关系
- 思考：知识图谱如何帮助理解复杂文本中的隐含关系
            """
            import pyperclip
            pyperclip.copy(knowledge_content)
            st.success("知识点内容已复制到剪贴板！")
