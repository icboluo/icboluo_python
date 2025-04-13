import easyocr
reader = easyocr.Reader(['ch_sim'])  # 指定语言（中文简体和英文）
results = reader.readtext('image.jpg')
for (bbox, text, prob) in results:
    print(f"文本：{text}, 置信度：{prob}")
