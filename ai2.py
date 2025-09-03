import os
import json
import base64
import cv2
import numpy as np
from PIL import Image
import ollama


def read_png_image(file_path):
    """读取PNG格式的游戏截图"""
    try:
        img = Image.open(file_path)
        return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    except Exception as e:
        print(f"读取图片失败: {str(e)}")
        return None


def format_image_input(image_data):
    """将图像转换为Qwen3可处理的输入格式"""
    _, buffer = cv2.imencode('.png', image_data)
    image_base64 = base64.b64encode(buffer).decode('utf-8')
    return f"<|im_start|>user<vision_start><row_1_col_1><|image_pad|>{image_base64}<|image_pad|><vision_start>"


MONSTER_ANALYSIS_PROMPT = """
请快速按以下规则分析游戏截图中的怪物状态：
1. 识别所有可见怪物
2. 根据特征判断状态：
   - 站立姿态→存活
   - 倒地姿态→死亡
3. 返回JSON格式：{"alive": 数量, "dead": 数量}

"""


def analyze_monsters(image_data):
    """使用Qwen3分析怪物状态"""
    formatted_input = format_image_input(image_data) + MONSTER_ANALYSIS_PROMPT
    response = ollama.chat(
        model="qwen3:0.6b",
        messages=[{"role": "user", "content": formatted_input}],
        stream=True
    )
    try:
        return json.loads(response['message']['content'])
    except (json.JSONDecodeError, KeyError):
        print("123")
        return {"alive": 0, "dead": 0}


def main():
    img_path = '刷体/羽林军6.png'

    img_data = read_png_image(img_path)
    if img_data is None:
        return

    result = analyze_monsters(img_data)
    print(f"存活怪物: {result['alive']} | 死亡怪物: {result['dead']}")


if __name__ == "__main__":
    main()
