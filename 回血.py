import time

import cv2
import numpy as np
import pyautogui
import pytesseract

from Tool import wait_click_sleep, find_all_matches, click_global, find, find_zuo_biao, wait_find_all_matches, wait_find

# 配置路径
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Tesseract路径

a1 = 13695
a2 = 19321
a3 = 19439
a4 = 10569


def get_xue_liang():
    wait_find('战斗/红色.png')
    time.sleep(0.3)
    left, top, width, height = find_zuo_biao()
    screenshot = pyautogui.screenshot(region=(left + 280, top + 375, width // 6, height // 27))
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


def bu_xue1_or_zhan_dou_fang_yu(is_fight=False):
    wait_click_sleep('战斗/物品.png', sleep_time=0.5, threshold=0.7)
    wait_click_sleep('战斗/加2000.png', sleep_time=0.5)
    global a1
    if a1 - get_xue_liang() > 400:
        wait_click_sleep('战斗/红色.png', threshold=0.7, print_msg=False)
        return
    wait_click_sleep('战斗/返回.png', sleep_time=0.5)
    if is_fight:
        wait_click_sleep('战斗/攻击.png', sleep_time=0.5)
        wait_click_sleep('战斗/红色.png', threshold=0.7, print_msg=False)
    else:
        wait_click_sleep('战斗/防御.png')


def bu_xue2_or_zhan_dou_fang_yu(is_fight=False):
    wait_click_sleep('战斗/物品.png', sleep_time=0.5, threshold=0.7)
    wait_click_sleep('战斗/加2000.png', sleep_time=0.5)
    wait_click_sleep('副将/吕布.png', sleep_time=0.5, threshold=0.7)
    global a2
    if a2 - get_xue_liang() > 400:
        wait_click_sleep('战斗/红色.png', threshold=0.7, print_msg=False)
        return
    wait_click_sleep('战斗/返回.png', sleep_time=0.5)
    if is_fight:
        wait_click_sleep('战斗/攻击.png')
        wait_click_sleep('战斗/红色.png', threshold=0.7, print_msg=False)
    else:
        wait_click_sleep('战斗/防御.png')


def chu_zhao_shun_xu(sun_shi):
    arr = [-1, -1, -1, -1]
    arr[3] = sun_shi_max_bu_xue(sun_shi)
    arr[2] = sun_shi_max_bu_xue(sun_shi)
    arr[1] = sun_shi_max_bu_xue(sun_shi)
    arr[0] = sun_shi_max_bu_xue(sun_shi)
    return arr


# 损失最大的补血，并且返回损血最大的编号
def sun_shi_max_bu_xue(sun_shi):
    idx = 0
    sun_max = 0
    for i in range(4):
        if sun_shi[i] > sun_max:
            sun_max = sun_shi[i]
            idx = i
    if sun_max <= 400:
        return -1
    sun_shi[idx] -= 2000
    return idx + 1


def bu_xue(i):
    wait_click_sleep('战斗/物品.png', sleep_time=0.5, threshold=0.7)
    x, y = find('战斗/物品.png')
    if x != -1:
        wait_click_sleep('战斗/物品.png', sleep_time=0.5, threshold=0.7)
    wait_click_sleep('战斗/加2000.png')
    if i == 2:
        wait_click_sleep('副将/吕布.png', sleep_time=0.5, threshold=0.7)
    elif i == 3:
        all_match = wait_find_all_matches('副将/龙飞.png', threshold=0.7)
        while len(all_match) == 0:
            all_match = wait_find_all_matches('副将/龙飞.png', threshold=0.7)
        a, b = all_match[0]
        click_global(a, b)
        time.sleep(0.5)
    elif i == 4:
        all_match = wait_find_all_matches('副将/龙飞.png', threshold=0.7)
        while len(all_match) == 0:
            all_match = wait_find_all_matches('副将/龙飞.png', threshold=0.7)
        a, b = all_match[1]
        click_global(a, b)
        time.sleep(0.5)
    wait_click_sleep('战斗/红色.png', sleep_time=0.5, threshold=0.7)


def shen_yu_xue_liang():
    global a1, a2, a3, a4
    arr = [a1, a2, a3, a4]
    wait_click_sleep('战斗/物品.png')
    wait_click_sleep('战斗/加2000.png', sleep_time=0.5, threshold=0.8)
    a = get_xue_liang()
    arr[0] = a

    wait_click_sleep('副将/吕布.png', threshold=0.7)
    b = get_xue_liang()
    arr[1] = b

    all_match = wait_find_all_matches('副将/龙飞.png', threshold=0.7)
    x, y = all_match[0]
    click_global(x, y)
    c = get_xue_liang()
    arr[2] = c

    all_match = wait_find_all_matches('副将/龙飞.png', threshold=0.7)
    if len(all_match) == 1:
        return arr
    x, y = all_match[1]
    click_global(x, y)
    d = get_xue_liang()
    arr[3] = d
    return arr


def sun_shi_xue_liang():
    global a1, a2, a3, a4
    arr = [a1, a2, a3, a4]
    arr2 = shen_yu_xue_liang()
    for i in range(10):
        x, y = find('战斗/返回.png')
        if x != -1:
            click_global(x, y)
            break
        time.sleep(1)

    for i in range(4):
        arr[i] -= arr2[i]
    return arr
