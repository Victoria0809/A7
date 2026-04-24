import streamlit as st
import spacy
import base64

def render_report():
    # 加载spaCy模型
    @st.cache_resource
    def load_spacy_model():
        try:
            nlp = spacy.load("en_core_web_sm")
            return nlp
        except Exception as e:
            st.error(f"无法加载spaCy模型: {e}")
            return None
    
    nlp = load_spacy_model()
    
    # 模块标题
    st.header("实验报告生成")
    
    # 文本输入
    input_text = st.text_area(
        "请输入分析文本",
        value="Steve Jobs founded Apple Inc. in California in 1976.",
        height=150,
        placeholder="输入需要分析的文本..."
    )
    
    if st.button("生成实验报告", key="generate_report"):
        if input_text:
            with st.spinner("正在生成报告..."):
                # 分析文本
                doc = nlp(input_text)
                
                # 提取实体
                entities = []
                for ent in doc.ents:
                    entities.append({
                        "text": ent.text,
                        "type": ent.label_
                    })
                
                # 提取关系
                relations = []
                # 规则1：founded
                for token in doc:
                    if token.lower_ == "founded" or token.lower_ == "found":
                        # 寻找主语
                        subject = None
                        for i in range(token.i - 1, -1, -1):
                            if doc[i].ent_type_ != "":
                                subject = doc[i].text
                                break
                        # 寻找宾语
                        object_ = None
                        for i in range(token.i + 1, len(doc)):
                            if doc[i].ent_type_ != "":
                                object_ = doc[i].text
                                break
                        if subject and object_:
                            relations.append({
                                "subject": subject,
                                "predicate": "FOUNDED",
                                "object": object_
                            })
                
                # 生成报告内容
                report_content = f"""
                # 信息抽取与知识图谱构建实验报告
                
                ## 一、实验目的
                本实验旨在通过交互式Web应用，帮助学生直观理解信息抽取的核心概念和流程，包括命名实体识别、关系抽取和知识图谱构建。
                
                ## 二、实验内容
                
                ### 2.1 输入文本
                ```
                {input_text}
                ```
                
                ### 2.2 命名实体识别结果
                | 实体 | 类型 |
                |------|------|
                """
                
                for entity in entities:
                    report_content += f"| {entity['text']} | {entity['type']} |\n"
                
                report_content += f"""
                
                ### 2.3 关系抽取结果
                | 主体 | 关系 | 客体 |
                |------|------|------|
                """
                
                for relation in relations:
                    report_content += f"| {relation['subject']} | {relation['predicate']} | {relation['object']} |\n"
                
                report_content += f"""
                
                ## 三、实验分析
                
                ### 3.1 命名实体识别分析
                - 共识别出 {len(entities)} 个实体
                - 实体类型分布：
                """
                
                # 统计实体类型
                entity_types = {}
                for entity in entities:
                    if entity['type'] in entity_types:
                        entity_types[entity['type']] += 1
                    else:
                        entity_types[entity['type']] = 1
                
                for ent_type, count in entity_types.items():
                    report_content += f"  - {ent_type}: {count}个\n"
                
                report_content += f"""
                
                ### 3.2 关系抽取分析
                - 共识别出 {len(relations)} 个关系
                - 关系类型：
                """
                
                # 统计关系类型
                relation_types = {}
                for relation in relations:
                    if relation['predicate'] in relation_types:
                        relation_types[relation['predicate']] += 1
                    else:
                        relation_types[relation['predicate']] = 1
                
                for rel_type, count in relation_types.items():
                    report_content += f"  - {rel_type}: {count}个\n"
                
                report_content += f"""
                
                ## 四、实验结论
                通过本次实验，我们成功实现了信息抽取的核心功能，包括命名实体识别、关系抽取和知识图谱构建。系统能够从非结构化文本中提取结构化信息，并将其可视化展示。
                
                ### 4.1 技术要点
                - 使用spaCy进行命名实体识别
                - 基于规则的关系抽取
                - 使用vis-network.js进行知识图谱可视化
                
                ### 4.2 应用价值
                - 帮助学生理解信息抽取的核心概念
                - 为知识图谱构建提供基础数据
                - 可应用于智能问答、文本摘要等场景
                
                ## 五、实验工具
                - 开发框架：Python Streamlit
                - 核心库：spaCy、networkx、vis-network.js
                - AI工具：Trae软件
                
                ## 六、学生观察记录
                
                ### 6.1 观察结果
                - 命名实体识别效果：[学生填写]
                - 关系抽取效果：[学生填写]
                - 知识图谱可视化效果：[学生填写]
                
                ### 6.2 问题与思考
                - [学生填写]
                
                ### 6.3 改进建议
                - [学生填写]
                """
                
                # 显示报告
                st.subheader("实验报告内容")
                st.markdown(report_content)
                
                # 提供下载功能
                def get_download_link(text, filename):
                    b64 = base64.b64encode(text.encode()).decode()
                    href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">下载报告</a>'
                    return href
                
                st.markdown(get_download_link(report_content, "experiment_report.md"), unsafe_allow_html=True)
                
                st.success("实验报告生成成功！")
        else:
            st.error("请输入分析文本")
