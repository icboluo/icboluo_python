import time

import cv2

from Tool import find_template, read_win_popup_safe, wait_click_sleep, wait_double_find_sleep, attack_row_sleep, \
    success_return, find_match_max_val, find, click_global, find_all_matches
from 回血 import chu_zhao, bu_xue1_or_attack, bu_xue2_or_attack


def ylj(template1_path, template2_path, threshold=0.6, print_msg=True):
    screen_gray = read_win_popup_safe()

    a1 = find_match_max_val(template1_path)
    a2 = find_match_max_val(template2_path)
    if a1 < threshold or a1 < a2:
        return -1, -1

    template = find_template(template1_path)
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
            target = template1_path.split('/')[1].split('.')[0]
            print(f'没有找到目标 {target}')
        return -1, -1


def zhao_lv_bu():
    wait_click_sleep('战斗/招将.png')
    time.sleep(1)
    fu_jiang_chu_zhan(2)
    wait_click_sleep('战斗/招将.png')
    time.sleep(1)
    fu_jiang_chu_zhan(1)
    bu_xue1_or_attack()
    wait_click_sleep('战斗/招将.png')
    time.sleep(1)
    fu_jiang_chu_zhan(1)
    bu_xue2_or_attack()
    chu_zhao(3)


def treat():
    while True:
        for i in range(1, 5):
            chu_zhao(i)
        while True:
            time.sleep(10)
            x, y = find('战斗/攻击.png')
            if x != -1:
                break
            success_return()
            x, y = find('主界面/主界面.png')
            if x != -1:
                break
            time.sleep(1)
        x, y = find('主界面/主界面.png')
        if x != -1:
            return


def fu_jiang_chu_zhan(row):
    all_find = find_all_matches('副将/出战.png', 0.7)
    a, b = all_find[row - 1]
    click_global(a, b)
    time.sleep(2)


if __name__ == '__main__':
    while True:
        wait_click_sleep('主界面/人物.png')
        wait_double_find_sleep('npc/战斗.png', '主界面/人物.png')
        attack_row_sleep(2)
        time.sleep(3)
        x, y = ylj('刷体/羽林军6.png', '刷体/羽林军4.png')
        if x != -1:
            wait_click_sleep('战斗/自动出招.png')
            time.sleep(2)
            while True:
                all_match = find_all_matches('刷体/羽林军死亡.png', threshold=0.8)
                if len(all_match) >= 4:
                    wait_click_sleep('战斗/手动出招.png')
                    zhao_lv_bu()
                    treat()
                    break
                time.sleep(1)
        else:
            while True:
                x3, y3 = find('战斗/逃跑.png')
                if x3 != -1:
                    click_global(x3, y3)
                    time.sleep(2)
                success_return()
                x4, y4 = find('主界面/人物.png')
                if x4 != -1:
                    break
                time.sleep(1)
