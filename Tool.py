import time

import cv2
import numpy as np
import pyautogui
import pygetwindow as gw
import win32con
import win32gui

win_l = 1
win_t = 1
win_w = 1
win_h = 1
glo_ren_wu_x = 1
glo_ren_wu_y = 1


def find_zuo_biao():
    global win_l, win_t, win_w, win_h
    return win_l, win_t, win_w, win_h


# 发现模版
def find_template(template_path):
    # 读取模板图片
    with open(template_path, 'rb') as f:
        img_bytes = np.frombuffer(f.read(), dtype=np.uint8)
    template = cv2.imdecode(img_bytes, cv2.IMREAD_GRAYSCALE)
    return template.astype(np.uint8)


def read_win_popup_safe():
    target_windows = gw.getWindowsWithTitle('夜神模拟器')
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


def find(template_path, threshold=0.8, print_msg=True):
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
            print(f'没有找到目标 {path_str(template_path)},匹配度不足: {max_val:.2f} < {threshold}')
        return -1, -1


def find_match_max_val(template_path):
    screen_gray = read_win_popup_safe()

    template1 = find_template(template_path)
    # 模板匹配
    res = cv2.matchTemplate(screen_gray, template1, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    return max_val


def wait_find(template_path, threshold=0.8, print_msg=True):
    template = find_template(template_path)
    # 统一数据类型
    template = template.astype(np.uint8)
    # 获取模板尺寸（注意：shape返回的顺序是 [高度, 宽度]）
    h, w = template.shape[:2]

    for i in range(100):
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
            if print_msg:
                print(f'没有找到目标 {path_str(template_path)},匹配度不足: {max_val:.2f} < {threshold}')
            # t = datetime.now().strftime("%M_%S_%f")
            # cv2.imwrite("temp/tem" + t + ".png", template)
            # cv2.imwrite("temp/win" + t + ".png", screen_gray)
            time.sleep(0.5)
    raise ValueError


def wait_click_sleep(template_path, threshold=0.8, sleep_time=1, print_msg=True):
    if print_msg:
        print(f'等待点击-> {path_str(template_path)}')
    x, y = wait_find(template_path, threshold)
    click_global(x, y)
    time.sleep(sleep_time)


def click_sleep(template_path, threshold=0.8):
    x, y = find(template_path, threshold)
    if x != -1:
        click_global(x, y)
        print(f'点击移动到-> {path_str(template_path)}')
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


def click_global(x, y):
    global win_l, win_t
    a = win_l + x
    b = win_t + y
    # pyautogui.moveTo(a, b, 1)
    return pyautogui.click(a, b)


def find_all_matches(template_path, threshold=0.8, overlap_threshold=0.3):
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


def wait_find_all_matches(template_path, threshold=0.8, print_msg=True):
    wait_find(template_path, threshold, print_msg)
    return find_all_matches(template_path, threshold)


# 一行点击最后面
def one_row_click_end(row_template_path, end_template_path, threshold=0.6):
    x, y = find(row_template_path, threshold)
    all_find = find_all_matches(end_template_path, threshold)
    for i in range(len(all_find)):
        a, b = all_find[i]
        if abs(b - y) < 30:
            return click_global(a, b)
            break


def attack_row_sleep(row):
    all_find = wait_find_all_matches('npc/战斗.png')
    a, b = all_find[row - 1]
    click_global(a, b)
    time.sleep(2)


def success_return():
    x1, y1 = find('胜利/胜利下一条.png', print_msg=False)
    if x1 != -1:
        click_global(x1, y1)
    x4, y4 = find('胜利/胜利关闭.png', print_msg=False)
    if x4 != -1:
        click_global(x4, y4)
    x3, y3 = find('胜利/败北.png', print_msg=False)
    global glo_ren_wu_x, glo_ren_wu_y
    if x3 != -1:
        click_global(glo_ren_wu_x, glo_ren_wu_y)
    x5, y5 = find('胜利/胜利.png', print_msg=False)
    if x5 != -1:
        click_global(glo_ren_wu_x, glo_ren_wu_y)


def any_match(*arr_path, threshold=0.8):
    for path in arr_path:
        x, y = find(path, threshold, print_msg=False)
        if x != -1:
            return True
    return False


# 返回图片后缀
def path_str(template_path):
    return template_path.split('/')[1].split('.')[0]


# 等待 是否第一个是最匹配的，如果没有任何一个匹配，报错
def wait_is_first_max_match(template1_path, template2_path, template3_path, threshold=0.8):
    is_find = False
    for i in range(10):
        a1 = find_match_max_val(template1_path)
        a2 = find_match_max_val(template2_path)
        a3 = find_match_max_val(template3_path)
        if a1 >= threshold or a2 >= threshold or a3 >= threshold:
            is_find = True
            break
        time.sleep(1)
        if i % 3 == 0:
            print(f'没有找到目标 {path_str(template1_path)},匹配度不足: {a1:.2f} < {threshold}')
    if not is_find:
        raise ValueError(
            f'图片{path_str(template1_path)},{path_str(template2_path)},{path_str(template3_path)}均不匹配')

    a1 = find_match_max_val(template1_path)
    a2 = find_match_max_val(template2_path)
    a3 = find_match_max_val(template3_path)
    if a1 < a2 or a1 < a3:
        return False
    return True


# 等待 发现第二个的时候返回，否则点击第一个图片进行尝试
def wait_find_second_when_multiple_click_first(template1_path, template2_path, threshold=0.8):
    for i in range(10):
        x1, y1 = find(template1_path, threshold)
        if x1 != -1:
            click_global(x1, y1)
        x2, y2 = find(template2_path, threshold)
        if x2 != -1:
            return
        time.sleep(1)


def print_template(template):
    cv2.imwrite("a_template.png", template)


def print_win_pop(win_pop):
    cv2.imwrite("a_win_pop.png", win_pop)


# 逃跑
def escape():
    j = 0
    for i in range(100):
        x1, y1 = find('战斗/逃跑.png', print_msg=False)
        if x1 != -1:
            j += 1
            print(f'第{j}次点击逃跑')
            click_global(x1, y1)
            time.sleep(1)
        success_return()
        x2, y2 = find('主界面/人物.png', print_msg=False)
        if x2 != -1:
            return
        time.sleep(1)


def init_zuo_biao():
    x, y = wait_find('主界面/人物.png')
    global glo_ren_wu_x, glo_ren_wu_y
    glo_ren_wu_x = x
    glo_ren_wu_y = y


# 初始化坐标
init_zuo_biao()
