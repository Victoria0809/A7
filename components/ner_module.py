import streamlit as st

def render_module():
    # 模块标题
    st.header("模块1：命名实体识别与BIO标注")
    
    # 左侧功能区
    col1, col2 = st.columns([2, 3])
    
    with col1:
        # 文本输入区域
        st.subheader("文本输入")
        default_text = "Steve Jobs founded Apple Inc. in California."
        input_text = st.text_area(
            "请输入文本",
            value=default_text,
            height=150,
            placeholder="输入需要分析的文本..."
        )
        
        # 控制按钮
        col1_btn, col2_btn = st.columns(2)
        with col1_btn:
            if st.button("清除文本", key="ner_clear"):
                input_text = ""
        with col2_btn:
            if st.button("使用示例文本", key="ner_example"):
                input_text = default_text
    
    with col2:
        # 尝试导入spacy
        try:
            import spacy
            nlp = spacy.load("en_core_web_sm")
            
            # 实体识别结果
            if input_text and nlp:
                with st.spinner("正在分析..."):
                    doc = nlp(input_text)
                    
                    # 高亮显示实体
                    highlighted_text = input_text
                    offset = 0
                    for ent in doc.ents:
                        entity_text = ent.text
                        entity_type = ent.label_
                        
                        if entity_type == "PERSON":
                            highlight_class = "highlight-person"
                        elif entity_type == "ORG":
                            highlight_class = "highlight-organization"
                        elif entity_type == "LOC":
                            highlight_class = "highlight-location"
                        elif entity_type == "DATE":
                            highlight_class = "highlight-date"
                        elif entity_type == "GPE":
                            highlight_class = "highlight-gpe"
                        else:
                            highlight_class = "highlight-other"
                        
                        start = ent.start_char + offset
                        end = ent.end_char + offset
                        highlighted_text = highlighted_text[:start] + f"<span class='{highlight_class}' title='{entity_type}'>{entity_text}</span>" + highlighted_text[end:]
                        offset += len(f"<span class='{highlight_class}' title='{entity_type}'></span>")
                    
                    # 显示高亮结果
                    st.subheader("实体识别结果")
                    st.markdown(f"<div class='module-card'>{highlighted_text}</div>", unsafe_allow_html=True)
                    
                    # BIO标注切换
                    show_bio = st.checkbox("显示BIO标注序列")
                    if show_bio:
                        bio_tags = []
                        for token in doc:
                            if token.ent_iob_ == "B":
                                bio_tags.append(f"<span class='bio-tag bio-tag-b'>B-{token.ent_type_}</span>")
                            elif token.ent_iob_ == "I":
                                bio_tags.append(f"<span class='bio-tag bio-tag-i'>I-{token.ent_type_}</span>")
                            else:
                                bio_tags.append(f"<span class='bio-tag bio-tag-o'>O</span>")
                        
                        st.subheader("BIO标注序列")
                        st.markdown(f"<div class='module-card'>{' '.join(bio_tags)}</div>", unsafe_allow_html=True)
        except ImportError:
            st.warning("⚠️ spaCy未安装，实体识别功能不可用")
        except Exception as e:
            st.error(f"❌ 实体识别失败: {e}")