import time

import cv2
import numpy as np
import pyautogui


def find_template(template_path):
    # 读取模板图片
    with open(template_path, 'rb') as f:
        img_bytes = np.frombuffer(f.read(), dtype=np.uint8)
    template = cv2.imdecode(img_bytes, cv2.IMREAD_GRAYSCALE)
    return template.astype(np.uint8)


def read_screen():
    screen = pyautogui.screenshot()
    screen_rgb = np.array(screen)
    # 明确从 RGB 转灰度（与模板的 IMREAD_GRAYSCALE 一致）
    screen_gray = cv2.cvtColor(screen_rgb, cv2.COLOR_RGB2GRAY)
    return screen_gray.astype(np.uint8)


def find(template_path, threshold=0.6):
    template = find_template(template_path)
    screen_gray = read_screen()

    # 获取模板尺寸（注意：shape返回的顺序是 [高度, 宽度]）
    h, w = template.shape[:2]  # 修正为 h, w 而不是 w, h

    # 模板匹配
    res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if max_val >= threshold:
        # 提取左上角坐标
        top_left_x, top_left_y = max_loc
        # 计算中心点坐标（修正点）
        center_x = top_left_x + w // 2
        center_y = top_left_y + h // 2

        return center_x, center_y
    else:
        target = template_path.split('/')[1].split('.')[0]
        print(f'没有找到目标 {target}')
        return -1, -1


def wait_find(template_path, threshold=0.6):
    template = find_template(template_path)
    # 统一数据类型
    template = template.astype(np.uint8)
    # 获取模板尺寸（注意：shape返回的顺序是 [高度, 宽度]）
    h, w = template.shape[:2]

    while True:
        screen_gray = read_screen()

        # 模板匹配
        res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val >= threshold:
            # 提取左上角坐标
            top_left_x, top_left_y = max_loc
            # 计算中心点坐标（修正点）
            center_x = top_left_x + w // 2
            center_y = top_left_y + h // 2

            return center_x, center_y
        else:
            target = template_path.split('/')
            print(f"{target} 匹配度不足: {max_val:.2f} < {threshold}")
            time.sleep(1)


def wait_click(template_path, threshold=0.6):
    # 读取模板图片
    template = find_template(template_path)
    # 获取模板尺寸（注意：shape返回的顺序是 [高度, 宽度]）
    h, w = template.shape[:2]

    while True:
        screen_gray = read_screen()
        # 模板匹配
        res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if max_val >= threshold:
            # 提取左上角坐标
            top_left_x, top_left_y = max_loc
            # 计算中心点坐标（修正点）
            center_x = top_left_x + w // 2
            center_y = top_left_y + h // 2
            pyautogui.click(center_x, center_y)
            return
        else:
            target = template_path.split('/')[1].split('.')[0]
            print(f"[{target}]匹配度不足: {max_val:.2f} < {threshold}")
            time.sleep(1)


def click(template_path, threshold=0.6, xs=0):
    # 读取模板图片
    template = find_template(template_path)
    # 获取模板尺寸（注意：shape返回的顺序是 [高度, 宽度]）
    h, w = template.shape[:2]

    screen_gray = read_screen()
    # 模板匹配
    res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if max_val >= threshold:
        # 提取左上角坐标
        top_left_x, top_left_y = max_loc
        # 计算中心点坐标（修正点）
        center_x = top_left_x + w // 2 + xs
        center_y = top_left_y + h // 2
        pyautogui.click(center_x, center_y)
        return
    else:
        target = template_path.split('/')[1].split('.')[0]
        print(f"[{target}]匹配度不足: {max_val:.2f} < {threshold}")
        time.sleep(1)


def attack_3time():
    for i in range(3):
        wait_click_sleep('战斗/攻击.png')
        wait_double_click_sleep('战斗/红色.png', '战斗/攻击.png')


def wait_click_skill_ret():
    time.sleep(2)
    i = 0
    while True:
        i += 1
        x, y = find('战斗/技能.png', 0.5)
        if x != -1:
            pyautogui.click(x, y)
            time.sleep(1)
            return True
        if i > 3:
            success_return()
            x3, y3 = find('主界面/人物.png')
            if x3 != -1:
                return False
            time.sleep(2)
        time.sleep(1)


def do_skill(skill_path):
    success = wait_click_skill_ret()
    if not success:
        return False
    wait_click_sleep(skill_path, 0.5)
    wait_click('战斗/红色.png', 0.5)
    time.sleep(0.5)
    return True


def wait_click_sleep(template_path, threshold=0.6):
    wait_click(template_path, threshold)
    time.sleep(1)
    target = template_path.split('/')[1].split('.')[0]
    print(f'点击移动到-> {target}')


def wait_double_click_sleep(template1_path, template2_path, threshold=0.6, xs=0):
    while True:
        x, y = find(template1_path, threshold)
        if x != -1:
            pyautogui.click(x + xs, y)
            time.sleep(1)
            target = template1_path.split('/')[1].split('.')[0]
            print(f'点击移动到-> {target}')
            return
        x1, y1 = find(template2_path, threshold)
        if x1 != -1:
            pyautogui.click(x1, y1)
        time.sleep(1)


def success_return():
    x1, y1 = find('胜利/胜利下一条.png', 0.5)
    if x1 != -1:
        pyautogui.click(x1, y1)
    x4, y4 = find('胜利/胜利关闭.png', 0.5)
    if x4 != -1:
        pyautogui.click(x4, y4)
    x2, y2 = find('胜利/胜利返回.png', 0.5)
    if x2 != -1:
        pyautogui.click(x2, y2)


def move():
    find('主界面/移动.png')
    wait_click_sleep('主界面/移动.png')
    wait_click_sleep('移动/返回中心陈留.png')
    wait_click_sleep('主界面/设施.png')
    wait_double_click_sleep('设施/医馆.png', '主界面/设施.png')
    wait_click_sleep('设施/全员治疗.png')
    wait_click_sleep('设施/治疗结果.png')
    wait_click_sleep('设施/返回.png')
    wait_click_sleep('主界面/移动.png')
    wait_click_sleep('移动/陈留郊外.png')
    wait_click_sleep('移动/陈留西郊.png')
    wait_click_sleep('移动/先锋一营.png')
    wait_click_sleep('移动/先锋二营.png')
    wait_click_sleep('移动/先锋三营.png')
    wait_click_sleep('移动/先锋四营.png')
    wait_click_sleep('移动/先锋领军.png')
    wait_click_sleep('主界面/人物.png')


def fight():
    x, y = find('怪物/黄巾士兵.png')
    print(x, y)
    wait_double_click_sleep('怪物/黄巾士兵长.png', '主界面/人物.png', 0.5, 130)
    if not do_skill('战斗/舍命一击.png'):
        return
    attack_3time()
    if not do_skill('战斗/力劈华山.png'):
        return
    # attack_3time()
    # if not do_skill('战斗/固若金汤.png'):
    #     return
    wait_click_sleep('战斗/自动出招.png')

    while True:
        success_return()
        x3, y3 = find('主界面/人物.png')
        if x3 != -1:
            return
        time.sleep(2)


def treat():
    wait_click_sleep('主界面/功能.png')
    wait_click_sleep('功能/物品.png')
    wait_click_sleep('功能/快速恢复.png')
    while True:
        x, y = find('功能/确定.png')
        if x != -1:
            pyautogui.click(x, y)
            time.sleep(1)
        x1, y1 = find('功能/返回.png')
        if x1 != -1:
            pyautogui.click(x1, y1)
            time.sleep(1)
        x2, y2 = find('主界面/人物.png')
        if x2 != -1:
            break
        time.sleep(1)


if __name__ == "__main__":
    for i in range(21):
        print(f'第{i + 1}次刷图')
        # move()
        treat()
        print(f'第{i + 1}次刷图')
        fight()
