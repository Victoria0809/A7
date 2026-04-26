import streamlit as st
import spacy
import networkx as nx

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
    st.header("模块3：知识图谱交互可视化")
    
    # 左侧功能区
    col1, col2 = st.columns([2, 3])
    
    with col1:
        # 文本输入区域
        st.subheader("文本输入")
        default_text = "In 2022, Oracle acquired Cerner for $28.3 billion. Larry Ellison announced this at Oracle's headquarters in Austin, Texas."
        input_text = st.text_area(
            "请输入文本",
            value=default_text,
            height=150,
            placeholder="输入需要分析的文本..."
        )
        
        # 控制按钮
        col1_btn, col2_btn = st.columns(2)
        with col1_btn:
            if st.button("清除文本", key="kg_clear"):
                input_text = ""
        with col2_btn:
            if st.button("使用示例文本", key="kg_example"):
                input_text = default_text
    
    with col2:
        # 知识图谱可视化
        if input_text and nlp:
            with st.spinner("正在分析..."):
                doc = nlp(input_text)
                
                # 提取实体
                entities = []
                entity_dict = {}
                for i, ent in enumerate(doc.ents):
                    entity_id = f"node_{i}"
                    entity_dict[ent.text] = entity_id
                    entities.append({
                        "id": entity_id,
                        "label": ent.text,
                        "type": ent.label_
                    })
                
                # 基于规则的关系抽取
                relations = []
                relation_id = 0
                
                # 规则1：acquired / acquire
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
                                "id": f"edge_{relation_id}",
                                "from": entity_dict[subject],
                                "to": entity_dict[object_],
                                "label": "ACQUIRED",
                                "confidence": 0.9
                            })
                            relation_id += 1
                
                # 规则2：CEO of
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
                                "id": f"edge_{relation_id}",
                                "from": entity_dict[subject],
                                "to": entity_dict[object_],
                                "label": "CEO_OF",
                                "confidence": 0.9
                            })
                            relation_id += 1
                
                # 规则3：headquarters in
                for token in doc:
                    if token.lower_ == "headquarters" and token.i + 1 < len(doc) and doc[token.i + 1].lower_ == "in":
                        # 寻找主语（通常在headquarters之前）
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
                                "id": f"edge_{relation_id}",
                                "from": entity_dict[subject],
                                "to": entity_dict[object_],
                                "label": "HEADQUARTERS_IN",
                                "confidence": 0.85
                            })
                            relation_id += 1
                
                # 规则4：founded / founder of
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
                                "id": f"edge_{relation_id}",
                                "from": entity_dict[subject],
                                "to": entity_dict[object_],
                                "label": "FOUNDER_OF",
                                "confidence": 0.9
                            })
                            relation_id += 1
                
                # 规则5：located in
                for token in doc:
                    if token.lower_ == "located" and token.i + 1 < len(doc) and doc[token.i + 1].lower_ == "in":
                        # 寻找主语（通常在located之前）
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
                                "id": f"edge_{relation_id}",
                                "from": entity_dict[subject],
                                "to": entity_dict[object_],
                                "label": "LOCATED_IN",
                                "confidence": 0.85
                            })
                            relation_id += 1
                
                # 生成节点和边的数据
                nodes_data = []
                for entity in entities:
                    if entity["type"] == "PERSON":
                        color = "#ff6b6b"
                        shape = "circle"
                        size = 25
                    elif entity["type"] == "ORG":
                        color = "#4dabf7"
                        shape = "square"
                        size = 30
                    elif entity["type"] in ["LOC", "GPE"]:
                        color = "#51cf66"
                        shape = "triangle"
                        size = 25
                    elif entity["type"] == "DATE":
                        color = "#ff922b"
                        shape = "diamond"
                        size = 20
                    else:
                        color = "#64748b"
                        shape = "circle"
                        size = 25
                    
                    nodes_data.append({
                        "id": entity["id"],
                        "label": entity["label"],
                        "color": color,
                        "shape": shape,
                        "size": size
                    })
                
                edges_data = []
                for relation in relations:
                    # 根据关系类型设置颜色
                    if relation["label"] == "FOUNDER_OF":
                        edge_color = "#8b5cf6"
                    elif relation["label"] == "LOCATED_IN":
                        edge_color = "#51cf66"
                    elif relation["label"] == "ACQUIRED":
                        edge_color = "#ff6b6b"
                    elif relation["label"] == "CEO_OF":
                        edge_color = "#4dabf7"
                    else:
                        edge_color = "#64748b"
                    
                    edges_data.append({
                        "id": relation["id"],
                        "from": relation["from"],
                        "to": relation["to"],
                        "label": relation["label"],
                        "arrows": "to",
                        "color": edge_color,
                        "width": 2,
                        "title": f"置信度: {relation.get('confidence', 0):.2f}"
                    })
                
                # 布局算法选择
                st.subheader("图谱配置")
                layout_algorithm = st.selectbox(
                    "选择布局算法",
                    options=["力导向布局", "层次布局", "环形布局"],
                    index=0
                )
                
                # 构建知识图谱可视化
                st.subheader("知识图谱可视化")
                
                # 使用vis-network.js创建知识图谱
                graph_html = """
                <!DOCTYPE html>
                <html>
                <head>
                    <title>知识图谱可视化</title>
                    <script type="text/javascript" src="https://unpkg.com/vis-network@latest/dist/vis-network.min.js"></script>
                    <style type="text/css">
                        #network {
                            width: 100%;
                            height: 600px;
                            border: 1px solid #e2e8f0;
                            border-radius: 10px;
                        }
                        .info-panel {
                            position: absolute;
                            top: 10px;
                            right: 10px;
                            background: white;
                            border: 1px solid #e2e8f0;
                            border-radius: 8px;
                            padding: 15px;
                            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                            max-width: 300px;
                            display: none;
                        }
                    </style>
                </head>
                <body>
                    <div id="network"></div>
                    <div class="info-panel" id="infoPanel">
                        <h3>详细信息</h3>
                        <div id="infoContent"></div>
                    </div>
                    <script type="text/javascript">
                        // 创建节点和边的数据
                        var nodes = new vis.DataSet({json_string});
                        var edges = new vis.DataSet({json_string2});
                        
                        // 配置布局
                        var layoutOption = {
                            improvedLayout: true,
                            hierarchical: false
                        };
                        
                        if ('{layout_algorithm}' === '层次布局') {
                            layoutOption = {
                                hierarchical: {
                                    enabled: true,
                                    levelSeparation: 150,
                                    nodeSpacing: 100,
                                    treeSpacing: 200,
                                    blockShifting: true,
                                    edgeMinimization: true,
                                    parentCentralization: true,
                                    direction: 'UD',
                                    sortMethod: 'directed'
                                }
                            };
                        } else if ('{layout_algorithm}' === '环形布局') {
                            layoutOption = {
                                hierarchical: false,
                                randomSeed: 42
                            };
                        }
                        
                        // 配置选项
                        var options = {
                            nodes: {
                                font: {
                                    size: 14,
                                    color: '#ffffff'
                                },
                                borderWidth: 2,
                                shadow: {
                                    enabled: true,
                                    size: 10,
                                    blur: 10
                                }
                            },
                            edges: {
                                font: {
                                    size: 12,
                                    color: '#333333'
                                },
                                smooth: {
                                    enabled: true,
                                    type: 'dynamic'
                                },
                                shadow: {
                                    enabled: true,
                                    size: 5,
                                    blur: 5
                                }
                            },
                            interaction: {
                                dragNodes: true,
                                zoomView: true,
                                panView: true,
                                hover: true
                            },
                            layout: layoutOption,
                            physics: {
                                enabled: true,
                                stabilization: {
                                    enabled: true,
                                    iterations: 1000
                                }
                            }
                        };
                        
                        // 创建网络
                        var container = document.getElementById('network');
                        var network = new vis.Network(container, {nodes: nodes, edges: edges}, options);
                        
                        // 双击节点居中
                        network.on('doubleClick', function(params) {
                            if (params.nodes.length > 0) {
                                var nodeId = params.nodes[0];
                                network.focus(nodeId, {scale: 1.5, animation: {duration: 1000}});
                            }
                        });
                        
                        // 点击节点/边显示详细信息
                        network.on('click', function(params) {
                            var infoPanel = document.getElementById('infoPanel');
                            var infoContent = document.getElementById('infoContent');
                            
                            if (params.nodes.length > 0) {
                                var nodeId = params.nodes[0];
                                var node = nodes.get(nodeId);
                                infoContent.innerHTML = `
                                    <p><strong>节点ID:</strong> ${node.id}</p>
                                    <p><strong>标签:</strong> ${node.label}</p>
                                    <p><strong>类型:</strong> ${node.shape}</p>
                                `;
                                infoPanel.style.display = 'block';
                            } else if (params.edges.length > 0) {
                                var edgeId = params.edges[0];
                                var edge = edges.get(edgeId);
                                var sourceNode = nodes.get(edge.from);
                                var targetNode = nodes.get(edge.to);
                                infoContent.innerHTML = `
                                    <p><strong>边ID:</strong> ${edge.id}</p>
                                    <p><strong>源节点:</strong> ${sourceNode.label}</p>
                                    <p><strong>目标节点:</strong> ${targetNode.label}</p>
                                    <p><strong>关系:</strong> ${edge.label}</p>
                                    <p><strong>置信度:</strong> ${edge.title ? edge.title.replace('置信度: ', '') : 'N/A'}</p>
                                `;
                                infoPanel.style.display = 'block';
                            } else {
                                infoPanel.style.display = 'none';
                            }
                        });
                        
                        // 导出为PNG
                        function exportNetwork() {
                            network.once('afterDrawing', function(ctx) {
                                var dataURL = ctx.canvas.toDataURL('image/png');
                                var link = document.createElement('a');
                                link.download = 'knowledge_graph.png';
                                link.href = dataURL;
                                link.click();
                            });
                            network.redraw();
                        };
                        
                        // 暴露导出函数
                        window.exportNetwork = exportNetwork;
                    </script>
                </body>
                </html>
                """
                
                # 替换变量
                graph_html = graph_html.replace('{json_string}', str(nodes_data))
                graph_html = graph_html.replace('{json_string2}', str(edges_data))
                graph_html = graph_html.replace('{layout_algorithm}', layout_algorithm)
                
                # 显示知识图谱
                st.components.v1.html(graph_html, height=600)
                
                # 导出功能
                if st.button("导出知识图谱为PNG", key="kg_export"):
                    st.markdown("""
                    <script>
                        window.exportNetwork();
                    </script>
                    """, unsafe_allow_html=True)
                    st.success("导出成功！")
                
                # 图谱分析功能
                st.subheader("图谱分析")
                col1_stats, col2_stats, col3_stats = st.columns(3)
                with col1_stats:
                    st.metric("节点数", len(nodes_data))
                with col2_stats:
                    st.metric("边数", len(edges_data))
                with col3_stats:
                    # 简单计算连通分量数
                    G = nx.DiGraph()
                    for node in nodes_data:
                        G.add_node(node["id"])
                    for edge in edges_data:
                        G.add_edge(edge["from"], edge["to"])
                    connected_components = nx.number_weakly_connected_components(G)
                    st.metric("连通分量数", connected_components)
                
                # 中心性分析
                st.subheader("中心性分析")
                if nodes_data:
                    # 计算度中心性
                    degree_centrality = nx.degree_centrality(G)
                    sorted_nodes = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:3]
                    top_nodes = []
                    for node_id, centrality in sorted_nodes:
                        for node in nodes_data:
                            if node["id"] == node_id:
                                top_nodes.append((node["label"], centrality))
                                break
                    
                    if top_nodes:
                        st.write("度中心性最高的节点：")
                        for node_label, centrality in top_nodes:
                            st.write(f"- {node_label}: {centrality:.3f}")
                
                # 路径查询
                st.subheader("路径查询")
                if nodes_data:
                    node_labels = [node["label"] for node in nodes_data]
                    col1_path, col2_path = st.columns(2)
                    with col1_path:
                        source_node = st.selectbox("源节点", options=node_labels)
                    with col2_path:
                        target_node = st.selectbox("目标节点", options=node_labels)
                    
                    if st.button("查询最短路径", key="kg_path_query"):
                        # 查找节点ID
                        source_id = None
                        target_id = None
                        for node in nodes_data:
                            if node["label"] == source_node:
                                source_id = node["id"]
                            if node["label"] == target_node:
                                target_id = node["id"]
                        
                        if source_id and target_id:
                            try:
                                shortest_path = nx.shortest_path(G, source=source_id, target=target_id)
                                path_labels = []
                                for node_id in shortest_path:
                                    for node in nodes_data:
                                        if node["id"] == node_id:
                                            path_labels.append(node["label"])
                                            break
                                st.success(f"最短路径: {' → '.join(path_labels)}")
                            except nx.NetworkXNoPath:
                                st.info("两节点之间无路径")