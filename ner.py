import spacy

# 加载SpaCy的简体中文模型
nlp = spacy.load("zh_core_web_sm")

# 输入的中文文本
text = """
苹果公司正在考虑以10亿美元收购一家英国初创公司。
旧金山考虑禁止人行道送货机器人。
伦敦是英国的一个大城市。
"""

# 使用模型处理文本
doc = nlp(text)

# 迭代识别的实体并打印
for ent in doc.ents:
    print(f"实体: {ent.text}, 类型: {ent.label_}")

# 如果你想获取实体及其类型为字典形式，可以使用以下代码
entities = [(ent.text, ent.label_) for ent in doc.ents]
entities_dict = {"entities": entities}

print(entities_dict)
