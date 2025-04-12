import time

import cv2
import numpy as np
import pyautogui
import pygetwindow as gw


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
    screen_gray = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)
    return screen_gray.astype(np.uint8)


# 读取屏幕
def read_screen():
    screen = pyautogui.screenshot()
    screen_rgb = np.array(screen)
    # 明确从 RGB 转灰度（与模板的 IMREAD_GRAYSCALE 一致）
    screen_gray = cv2.cvtColor(screen_rgb, cv2.COLOR_RGB2GRAY)
    return screen_gray.astype(np.uint8)


def find(template_path, threshold=0.6):
    template = find_template(template_path)
    screen_gray = read_win_popup_safe()

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
            # 计算中心点坐标（修正点）
            center_x = top_left_x + w // 2
            center_y = top_left_y + h // 2
            pyautogui.click(center_x, center_y)
            return
        else:
            target = template_path.split('/')[1].split('.')[0]
            print(f"[{target}]匹配度不足: {max_val:.2f} < {threshold}")
            cv2.imwrite("aa.png", template)
            cv2.imwrite("ab.png", screen_gray)
            time.sleep(1)


def click(template_path, threshold=0.6, xs=0):
    # 读取模板图片
    template = find_template(template_path)
    # 获取模板尺寸（注意：shape返回的顺序是 [高度, 宽度]）
    h, w = template.shape[:2]

    screen_gray = read_win_popup_safe()
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


def wait_click_sleep(template_path, threshold=0.6):
    wait_click(template_path, threshold)
    time.sleep(1)
    target = template_path.split('/')[1].split('.')[0]
    print(f'点击移动到-> {target}')


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
        # 计算中心点坐标（修正点）
        center_x = top_left_x + w // 2
        center_y = top_left_y + h // 2

        return pyautogui.moveTo(center_x, center_y, duration=0.5)
    else:
        target = template_path.split('/')[1].split('.')[0]
        print(f'没有找到目标 {target}')
        return -1, -1
