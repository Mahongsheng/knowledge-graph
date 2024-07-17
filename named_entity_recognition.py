import spacy

# 加载SpaCy的简体中文模型
nlp = spacy.load("zh_core_web_sm")

# 输入的中文文本
text = """
非洲某国发生叛乱，中国海军执行撤侨人物，冷锋奉命只身闯入硝烟四起的战场。
不屈不挠的战狼，与冷酷无情的敌人展开了悬殊之战。
"""

# 使用模型处理文本
doc = nlp(text)

for ent in doc.ents:
    print(f"实体: {ent.text}, 类型: {ent.label_}")

entities = [(ent.text, ent.label_) for ent in doc.ents]
entities_dict = {"entities": entities}

print(entities_dict)
