import time

import cv2
import numpy as np
import pyautogui
import pytesseract

from Tool import find_zuo_biao, wait_click_sleep, find_all_matches, click_global, find, success_return

# 配置路径
pytesseract.pytesseract.tesseract_cmd = r'D:\game\Tesseract-OCR\tesseract.exe'  # Tesseract路径


def get_xue_liang():
    left, top, width, height = find_zuo_biao()
    screenshot = pyautogui.screenshot(region=(left + 316, top + 420, width // 6, height // 25))
    screenshot.save("aa.png")

    img = cv2.imread('aa.png')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 定义淡红色范围（低饱和度）
    lower_light_red1 = np.array([0, 40, 150])  # 色调0-10°, 饱和度较低
    upper_light_red1 = np.array([10, 120, 255])
    lower_light_red2 = np.array([170, 40, 150])  # 色调170-180°
    upper_light_red2 = np.array([180, 120, 255])

    # 定义深红色干扰背景范围（高饱和度）
    lower_dark_red = np.array([0, 120, 50])
    upper_dark_red = np.array([180, 255, 200])

    # 生成淡红掩膜并排除深红背景
    mask_light_red = cv2.inRange(hsv, lower_light_red1, upper_light_red1) | \
                     cv2.inRange(hsv, lower_light_red2, upper_light_red2)
    mask_dark_red = cv2.inRange(hsv, lower_dark_red, upper_dark_red)
    final_mask = cv2.subtract(mask_light_red, mask_dark_red)
    # OCR 识别
    config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'
    text = pytesseract.image_to_string(mask_dark_red, config=config)
    return int(text.strip())

def bu_xue1():
    wait_click_sleep('战斗/物品.png')
    wait_click_sleep('战斗/加2000.png', threshold=0.8)
    xue = get_xue_liang()
    print("识别结果:", xue)
    if 12595 - xue > 4000:
        wait_click_sleep('战斗/红色.png')
        return True
    return False


def bu_xue2():
    for i in range(10):
        x, y = find('战斗/红色.png')
        if x != -1:
            wait_click_sleep('副将/吕布.png')
            time.sleep(1)
            xue = get_xue_liang()
            print("识别结果:", xue)
            if 17828 - xue > 4000:
                wait_click_sleep('战斗/红色.png')
                return True
            else:
                return False
        x, y = find('战斗/物品.png')
        if x != -1:
            wait_click_sleep('战斗/物品.png')
            wait_click_sleep('战斗/加2000.png', threshold=0.8)
        time.sleep(1)
    return False


def bu_xue3():
    for i in range(10):
        x, y = find('战斗/红色.png')
        if x != -1:
            all_match = find_all_matches('副将/龙飞.png')
            a, b = all_match[0]
            click_global(a, b)
            time.sleep(1)
            xue = get_xue_liang()
            print("识别结果:", xue)
            if 17945 - xue > 4000:
                wait_click_sleep('战斗/红色.png')
                return True
            else:
                return False
        x, y = find('战斗/物品.png')
        if x != -1:
            wait_click_sleep('战斗/物品.png')
            wait_click_sleep('战斗/加2000.png', threshold=0.8)
        time.sleep(1)
    return False


def bu_xue4():
    for i in range(10):
        x, y = find('战斗/红色.png')
        if x != -1:
            all_match = find_all_matches('副将/龙飞.png')
            a, b = all_match[1]
            click_global(a, b)
            time.sleep(1)
            xue = get_xue_liang()
            print("识别结果:", xue)
            if 9658 - xue > 4000:
                wait_click_sleep('战斗/红色.png')
                return True
            else:
                return False
        time.sleep(1)
        x, y = find('战斗/物品.png')
        if x != -1:
            wait_click_sleep('战斗/物品.png')
            wait_click_sleep('战斗/加2000.png', threshold=0.8)
    return False


def bu_xue1_or_attack():
    is_treat = bu_xue1()
    if not is_treat:
        wait_click_sleep('战斗/返回.png')
        wait_click_sleep('战斗/攻击.png')
        wait_click_sleep('战斗/红色.png')


def bu_xue2_or_fang_yu():
    is_treat = bu_xue2()
    if not is_treat:
        wait_click_sleep('战斗/返回.png')
        wait_click_sleep('战斗/防御.png')


def chu_zhao(i):
    if i == 1:
        wait_click_sleep('战斗/攻击.png')
        wait_click_sleep('战斗/红色.png')
        return
    if i == 2:
        wait_click_sleep('战斗/攻击.png')
        wait_click_sleep('战斗/红色.png')
    if i == 3:
        is_treat = bu_xue1()
        if not is_treat:
            is_treat = bu_xue3()
            if not is_treat:
                wait_click_sleep('战斗/返回.png')
                wait_click_sleep('战斗/攻击.png')
                wait_click_sleep('战斗/红色.png')
        return
    if i == 4:
        is_treat = bu_xue2()
        if not is_treat:
            is_treat = bu_xue4()
            if not is_treat:
                wait_click_sleep('战斗/返回.png')
                wait_click_sleep('战斗/攻击.png')
                wait_click_sleep('战斗/红色.png')

    return

# if __name__ == "__main__":
#     while True:
#         for i in range(1, 5):
#             chu_zhao(i)
#         success_return()
#         time.sleep(1)
