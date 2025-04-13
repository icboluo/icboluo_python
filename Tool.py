import time
from datetime import datetime

import cv2
import numpy as np
import pyautogui
import pygetwindow as gw

win_l = 1
win_t = 1
win_w = 1
win_h = 1


# 发现模版
def find_template(template_path):
    # 读取模板图片
    with open(template_path, 'rb') as f:
        img_bytes = np.frombuffer(f.read(), dtype=np.uint8)
    template = cv2.imdecode(img_bytes, cv2.IMREAD_GRAYSCALE)
    return template.astype(np.uint8)


def read_win_popup_safe():
    target_windows = gw.getWindowsWithTitle('雷电模拟器')
    if not target_windows:
        print("弹窗未找到，请检查标题是否匹配")
        return None

    window = target_windows[0]
    if window.isMinimized:
        window.restore()

        # 截取弹窗区域
    screen = pyautogui.screenshot(region=(window.left, window.top, window.width, window.height))
    global win_l, win_t, win_w, win_h
    win_l = window.left
    win_t = window.top
    win_w = window.width
    win_h = window.height
    screen_gray = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)
    return screen_gray.astype(np.uint8)


# 读取屏幕
def read_screen():
    screen = pyautogui.screenshot()
    screen_rgb = np.array(screen)
    # 明确从 RGB 转灰度（与模板的 IMREAD_GRAYSCALE 一致）
    screen_gray = cv2.cvtColor(screen_rgb, cv2.COLOR_RGB2GRAY)
    return screen_gray.astype(np.uint8)


def find(template_path, threshold=0.6, print_msg=True):
    template = find_template(template_path)
    screen_gray = read_win_popup_safe()

    # 获取模板尺寸（注意：shape返回的顺序是 [高度, 宽度]）
    h, w = template.shape[:2]

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
        if print_msg:
            target = template_path.split('/')[1].split('.')[0]
            print(f'没有找到目标 {target}')
        return -1, -1


def find_match(template_path):
    screen_gray = read_win_popup_safe()

    template1 = find_template(template_path)
    # 获取模板尺寸（注意：shape返回的顺序是 [高度, 宽度]）
    h, w = template1.shape[:2]
    # 模板匹配
    res = cv2.matchTemplate(screen_gray, template1, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    return max_val


def wait_find(template_path, threshold=0.6):
    template = find_template(template_path)
    # 统一数据类型
    template = template.astype(np.uint8)
    # 获取模板尺寸（注意：shape返回的顺序是 [高度, 宽度]）
    h, w = template.shape[:2]

    while True:
        screen_gray = read_win_popup_safe()

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
        screen_gray = read_win_popup_safe()
        # 模板匹配
        res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if max_val >= threshold:
            # 提取左上角坐标
            top_left_x, top_left_y = max_loc
            center_x = top_left_x + w // 2
            center_y = top_left_y + h // 2
            click_global(center_x, center_y)
        else:
            target = template_path.split('/')[1].split('.')[0]
            print(f"[{target}]匹配度不足: {max_val:.2f} < {threshold}")
            # t = datetime.now().strftime("%M_%S_%f")
            # cv2.imwrite("temp/tem" + t + ".png", template)
            # cv2.imwrite("temp/win" + t + ".png", screen_gray)
            time.sleep(1)


def wait_click_sleep(template_path, threshold=0.6):
    wait_click(template_path, threshold)
    time.sleep(1)
    target = template_path.split('/')[1].split('.')[0]
    print(f'点击移动到-> {target}')


def click_sleep(template_path, threshold=0.6):
    x, y = find(template_path, threshold)
    if x != -1:
        click_global(x, y)
    time.sleep(1)
    target = template_path.split('/')[1].split('.')[0]
    print(f'点击移动到-> {target}')


def wait_double_click_sleep(template1_path, template2_path, threshold=0.6):
    while True:
        x, y = find(template1_path, threshold)
        if x != -1:
            click_global(x, y)
            time.sleep(1)
            target = template1_path.split('/')[1].split('.')[0]
            print(f'点击移动到-> {target}')
            return
        x1, y1 = find(template2_path, threshold)
        if x1 != -1:
            click_global(x1, y1)
        time.sleep(1)


def wait_double_find_sleep(template1_path, template2_path, threshold=0.6):
    while True:
        x, y = find(template1_path, threshold)
        if x != -1:
            return
        x1, y1 = find(template2_path, threshold)
        if x1 != -1:
            click_global(x1, y1)
        time.sleep(1)


def move(template_path, threshold=0.6):
    template = find_template(template_path)
    screen_gray = read_win_popup_safe()

    # 获取模板尺寸（注意：shape返回的顺序是 [高度, 宽度]）
    h, w = template.shape[:2]

    # 模板匹配
    res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if max_val >= threshold:
        # 提取左上角坐标
        top_left_x, top_left_y = max_loc
        global win_l, win_t
        # 计算中心点坐标（修正点）
        center_x = win_l + top_left_x + w // 2
        center_y = win_t + top_left_y + h // 2

        return pyautogui.moveTo(center_x, center_y, duration=0.5)
    else:
        target = template_path.split('/')[1].split('.')[0]
        print(f'没有找到目标 {target}')
        return -1, -1


def click_global(x, y):
    global win_l, win_t
    a = win_l + x
    b = win_t + y
    # pyautogui.moveTo(a, b, 1)
    return pyautogui.click(a, b)


def find_all_matches(template_path, threshold=0.6, overlap_threshold=0.3):
    template = find_template(template_path)
    screen_gray = read_win_popup_safe()
    # 获取模板尺寸
    h, w = template.shape[:2]

    # 模板匹配
    res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)

    # 获取所有匹配位置坐标
    match_y, match_x = np.where(res >= threshold)

    # 转换为矩形列表 (x, y, w, h)
    rectangles = [(x, y, w, h) for x, y in zip(match_x, match_y)]

    # 非极大值抑制去重
    nms_indices = cv2.dnn.NMSBoxes(rectangles, [1.0] * len(rectangles), threshold, overlap_threshold)

    # 提取最终坐标
    final_matches = []
    if nms_indices is not None:
        if type(nms_indices) is tuple:
            return []
        nms_indices = nms_indices.flatten()  # 降维处理
        for idx in nms_indices:
            x, y, _, _ = rectangles[idx]
            final_matches.append((x + w // 2, y + h // 2))

    return final_matches


# 一行点击最后面
def one_row_click_end(row_template_path, end_template_path, threshold=0.6):
    x, y = find(row_template_path, threshold)
    all_find = find_all_matches(end_template_path, threshold)
    for i in range(len(all_find)):
        a, b = all_find[i]
        if abs(b - y) < 30:
            return click_global(a, b)
            break


def attack_sleep(row):
    all_find = find_all_matches('npc/战斗.png', 0.7)
    a, b = all_find[row - 1]
    click_global(a, b)
    time.sleep(2)


def next_step(template_path):
    for i in range(10):
        cx, cy = find(template_path)
        if cx != -1:
            click_global(cx, cy)
        time.sleep(1)


def success_return():
    x3, y3 = find('胜利/胜利下一条.png', print_msg=False)
    if x3 != -1:
        click_global(x3, y3)
    x1, y1 = find('胜利/胜利下一条.png', print_msg=False)
    if x1 != -1:
        click_global(x1, y1)
    x4, y4 = find('胜利/胜利关闭.png', print_msg=False)
    if x4 != -1:
        click_global(x4, y4)
    x2, y2 = find('胜利/胜利返回.png', print_msg=False)
    if x2 != -1:
        click_global(x2, y2)


def treat():
    wait_click_sleep('主界面/功能.png')
    wait_click_sleep('功能/物品.png')
    wait_click_sleep('功能/快速恢复.png')
    while True:
        x, y = find('功能/确定.png')
        if x != -1:
            click_global(x, y)
            time.sleep(1)
        x1, y1 = find('功能/返回.png')
        if x1 != -1:
            click_global(x1, y1)
            time.sleep(1)
        x2, y2 = find('主界面/人物.png')
        if x2 != -1:
            break
        time.sleep(1)
