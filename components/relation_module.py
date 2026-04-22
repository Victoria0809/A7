import streamlit as st
import spacy
import pandas as pd

def render_module():
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
    st.header("模块2：实体关系抽取")
    
    # 左侧功能区
    col1, col2 = st.columns([2, 3])
    
    with col1:
        # 文本输入区域
        st.subheader("文本输入")
        default_text = "The founder of Microsoft, Bill Gates, was born in Seattle."
        input_text = st.text_area(
            "请输入文本",
            value=default_text,
            height=150,
            placeholder="输入需要分析的文本..."
        )
        
        # 控制按钮
        col1_btn, col2_btn = st.columns(2)
        with col1_btn:
            if st.button("清除文本", key="re_clear"):
                input_text = ""
        with col2_btn:
            if st.button("使用示例文本", key="re_example"):
                input_text = default_text
    
    with col2:
        # 关系抽取结果
        if input_text and nlp:
            with st.spinner("正在分析..."):
                doc = nlp(input_text)
                
                # 提取实体
                entities = []
                entity_dict = {}
                for i, ent in enumerate(doc.ents):
                    entity_dict[ent.text] = i
                    entities.append({
                        "text": ent.text,
                        "type": ent.label_,
                        "start": ent.start_char,
                        "end": ent.end_char
                    })
                
                # 基于规则的关系抽取
                relations = []
                
                # 规则1：founder of / founded
                for token in doc:
                    if (token.lower_ == "founder" and token.i + 1 < len(doc) and doc[token.i + 1].lower_ == "of") or token.lower_ == "founded":
                        # 寻找主语（通常在动词之前）
                        subject = None
                        for i in range(token.i - 1, -1, -1):
                            if doc[i].text in entity_dict:
                                subject = doc[i].text
                                break
                        # 寻找宾语（通常在动词之后）
                        object_ = None
                        for i in range(token.i + 1, len(doc)):
                            if doc[i].text in entity_dict:
                                object_ = doc[i].text
                                break
                        if subject and object_:
                            relations.append({
                                "subject": subject,
                                "predicate": "FOUNDER_OF",
                                "object": object_,
                                "confidence": 0.9
                            })
                
                # 规则2：born in
                for token in doc:
                    if token.lower_ == "born" and token.i + 1 < len(doc) and doc[token.i + 1].lower_ == "in":
                        # 寻找主语（通常在born之前）
                        subject = None
                        for i in range(token.i - 1, -1, -1):
                            if doc[i].text in entity_dict:
                                subject = doc[i].text
                                break
                        # 寻找宾语（通常在in之后）
                        object_ = None
                        for i in range(token.i + 2, len(doc)):
                            if doc[i].text in entity_dict:
                                object_ = doc[i].text
                                break
                        if subject and object_:
                            relations.append({
                                "subject": subject,
                                "predicate": "BORN_IN",
                                "object": object_,
                                "confidence": 0.9
                            })
                
                # 规则3：works at / work at
                for token in doc:
                    if (token.lower_ == "works" or token.lower_ == "work") and token.i + 1 < len(doc) and doc[token.i + 1].lower_ == "at":
                        # 寻找主语（通常在works之前）
                        subject = None
                        for i in range(token.i - 1, -1, -1):
                            if doc[i].text in entity_dict:
                                subject = doc[i].text
                                break
                        # 寻找宾语（通常在at之后）
                        object_ = None
                        for i in range(token.i + 2, len(doc)):
                            if doc[i].text in entity_dict:
                                object_ = doc[i].text
                                break
                        if subject and object_:
                            relations.append({
                                "subject": subject,
                                "predicate": "WORKS_AT",
                                "object": object_,
                                "confidence": 0.85
                            })
                
                # 规则4：located in / located at
                for token in doc:
                    if token.lower_ == "located" and token.i + 1 < len(doc) and (doc[token.i + 1].lower_ == "in" or doc[token.i + 1].lower_ == "at"):
                        # 寻找主语（通常在located之前）
                        subject = None
                        for i in range(token.i - 1, -1, -1):
                            if doc[i].text in entity_dict:
                                subject = doc[i].text
                                break
                        # 寻找宾语（通常在in/at之后）
                        object_ = None
                        for i in range(token.i + 2, len(doc)):
                            if doc[i].text in entity_dict:
                                object_ = doc[i].text
                                break
                        if subject and object_:
                            relations.append({
                                "subject": subject,
                                "predicate": "LOCATED_IN",
                                "object": object_,
                                "confidence": 0.85
                            })
                
                # 规则5：acquired / acquire
                for token in doc:
                    if token.lower_ == "acquired" or token.lower_ == "acquire":
                        # 寻找主语（通常在acquired之前）
                        subject = None
                        for i in range(token.i - 1, -1, -1):
                            if doc[i].text in entity_dict:
                                subject = doc[i].text
                                break
                        # 寻找宾语（通常在acquired之后）
                        object_ = None
                        for i in range(token.i + 1, len(doc)):
                            if doc[i].text in entity_dict:
                                object_ = doc[i].text
                                break
                        if subject and object_:
                            relations.append({
                                "subject": subject,
                                "predicate": "ACQUIRED",
                                "object": object_,
                                "confidence": 0.9
                            })
                
                # 规则6：part of
                for token in doc:
                    if token.lower_ == "part" and token.i + 1 < len(doc) and doc[token.i + 1].lower_ == "of":
                        # 寻找主语（通常在part之前）
                        subject = None
                        for i in range(token.i - 1, -1, -1):
                            if doc[i].text in entity_dict:
                                subject = doc[i].text
                                break
                        # 寻找宾语（通常在of之后）
                        object_ = None
                        for i in range(token.i + 2, len(doc)):
                            if doc[i].text in entity_dict:
                                object_ = doc[i].text
                                break
                        if subject and object_:
                            relations.append({
                                "subject": subject,
                                "predicate": "PART_OF",
                                "object": object_,
                                "confidence": 0.8
                            })
                
                # 规则7：CEO of
                for token in doc:
                    if token.lower_ == "ceo" and token.i + 1 < len(doc) and doc[token.i + 1].lower_ == "of":
                        # 寻找主语（通常在CEO之前）
                        subject = None
                        for i in range(token.i - 1, -1, -1):
                            if doc[i].text in entity_dict:
                                subject = doc[i].text
                                break
                        # 寻找宾语（通常在of之后）
                        object_ = None
                        for i in range(token.i + 2, len(doc)):
                            if doc[i].text in entity_dict:
                                object_ = doc[i].text
                                break
                        if subject and object_:
                            relations.append({
                                "subject": subject,
                                "predicate": "CEO_OF",
                                "object": object_,
                                "confidence": 0.9
                            })
                
                # 关系过滤功能
                st.subheader("关系过滤")
                col1_filter, col2_filter = st.columns(2)
                
                # 关系类型筛选
                with col1_filter:
                    relation_types = list(set([r["predicate"] for r in relations])) if relations else []
                    selected_relation = st.selectbox(
                        "选择关系类型",
                        options=["全部"] + relation_types,
                        index=0
                    )
                
                # 置信度阈值滑块
                with col2_filter:
                    confidence_threshold = st.slider(
                        "置信度阈值",
                        min_value=0.0,
                        max_value=1.0,
                        value=0.0,
                        step=0.1
                    )
                
                # 过滤关系
                filtered_relations = []
                for relation in relations:
                    if (selected_relation == "全部" or relation["predicate"] == selected_relation) and relation["confidence"] >= confidence_threshold:
                        filtered_relations.append(relation)
                
                # 显示统计信息
                if relations:
                    total_relations = len(relations)
                    avg_confidence = sum([r["confidence"] for r in relations]) / total_relations
                    st.info(f"总关系数: {total_relations}, 平均置信度: {avg_confidence:.2f}")
                
                # 显示关系抽取结果
                st.subheader("关系抽取结果")
                if filtered_relations:
                    # 转换为DataFrame显示
                    df = pd.DataFrame(filtered_relations)
                    
                    # 添加置信度进度条
                    def confidence_bar(confidence):
                        if confidence > 0.8:
                            color = "green"
                        elif confidence > 0.6:
                            color = "yellow"
                        else:
                            color = "red"
                        return f"<div style='width: 100%; background-color: #e2e8f0; border-radius: 4px; padding: 2px;'><div style='width: {confidence * 100}%; background-color: {color}; border-radius: 2px; height: 16px;'></div></div>"
                    
                    df["置信度"] = df["confidence"].apply(confidence_bar)
                    st.markdown(df[["subject", "predicate", "object", "置信度"]].to_html(escape=False, index=False), unsafe_allow_html=True)
                else:
                    st.info("未识别到关系")
