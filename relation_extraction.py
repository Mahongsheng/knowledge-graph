import spacy
from spacy import displacy
from spacy.matcher import Matcher

# 加载SpaCy的英语模型
nlp = spacy.load("en_core_web_sm")

# 输入的文本
text = "Romeo loves Juliet and they lived happily together."

# 使用模型处理文本
doc = nlp(text)

for chunk in doc.noun_chunks:
    print(f"名词短语: {chunk.text}")

# 关系抽取（基于规则）
matcher = Matcher(nlp.vocab)

# 定义规则：主谓宾
pattern = [
    {"DEP": "nsubj"},  # 主语
    {"DEP": "ROOT"},  # 谓语
    {"DEP": "dobj"}  # 宾语
]
matcher.add("relationship", [pattern])

matches = matcher(doc)

print("\n关系抽取（主谓宾）:")
for match_id, start, end in matches:
    span = doc[start:end]
    print(f"关系: {span.text}")

# 展示提取的关系
rel_html = displacy.render(doc, style="dep", options={"distance": 120})
with open("relationships.html", "w", encoding="utf-8") as f:
    f.write(rel_html)

# 字典形式
nouns = [chunk.text for chunk in doc.noun_chunks]
relations = [doc[start:end].text for match_id, start, end in matches]
extracted_info = {"noun chunks": nouns, "relations": relations}

print("\n提取的信息字典:")
print(extracted_info)
