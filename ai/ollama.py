import json

import ollama  # 替换原dashscope

from Tool import find_template


def analyze_game_units(screenshot_path):
    img = find_template(screenshot_path)
    if img is None:
        raise FileNotFoundError(f"无法加载截图: {screenshot_path}")

    # 本地模型调用
    response = ollama.chat(
        model='qwen3:0.6b',
        messages=[{
            'role': 'user',
            'content': f'分析这张游戏截图：{screenshot_path}，统计敌方存活和死亡单位数量，以JSON格式返回alive_units和dead_units字段'
        }]
    )

    try:
        return json.loads(response['message']['content'])
    except Exception as e:
        raise ValueError(f"响应解析失败: {str(e)}")


if __name__ == "__main__":
    try:
        stats = analyze_game_units("../picture/alive6.png")
        print(f"存活单位: {stats.get('alive_units', 0)} | 死亡单位: {stats.get('dead_units', 0)}")
    except Exception as e:
        print(f"分析失败: {str(e)}")
