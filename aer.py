import spacy
from spacy import displacy
from spacy.matcher import Matcher

# 加载SpaCy的英语模型
nlp = spacy.load("en_core_web_sm")

# 输入的文本
text = """
Apple is looking at buying U.K. startup for $1 billion.
San Francisco considers banning sidewalk delivery robots.
London is a big city in the United Kingdom.
"""

# 使用模型处理文本
doc = nlp(text)

# 属性抽取（名词短语）
print("属性抽取（名词短语）:")
for chunk in doc.noun_chunks:
    print(f"名词短语: {chunk.text}")

# 关系抽取（基于规则）
matcher = Matcher(nlp.vocab)

# 定义规则：实体+动词+实体
pattern = [
    {"DEP": "nsubj"},
    {"DEP": "ROOT"},
    {"DEP": "dobj"}
]
matcher.add("relationship", [pattern])

matches = matcher(doc)

print("\n关系抽取（实体+动词+实体）:")
for match_id, start, end in matches:
    span = doc[start:end]
    print(f"关系: {span.text}")

# 如果你想在文本中标注并展示提取的关系，可以使用以下代码
rel_html = displacy.render(doc, style="dep", options={"distance": 120})
with open("relationships.html", "w", encoding="utf-8") as f:
    f.write(rel_html)

# 如果你想获取属性和关系为字典形式，可以使用以下代码
attributes = [chunk.text for chunk in doc.noun_chunks]
relations = [doc[start:end].text for match_id, start, end in matches]
extracted_info = {"attributes": attributes, "relations": relations}

print("\n提取的信息字典:")
print(extracted_info)
