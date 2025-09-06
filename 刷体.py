import datetime
import time

import ini
from AiTool import dead_num, total_num
from Tool import wait_click_sleep, success_return, find, click_global, find_all_matches, any_match, \
    wait_find_all_matches, escape
from 回血 import bu_xue1_or_zhan_dou_fang_yu, sun_shi_xue_liang, chu_zhao_shun_xu, bu_xue, bu_xue2_or_zhan_dou_fang_yu
from 战斗 import attack_in_success


def zhao_fu_jiang():
    wait_click_sleep('战斗/招将.png')
    fu_jiang_chu_zhan(1)

    wait_click_sleep('战斗/招将.png')
    fu_jiang_chu_zhan(1)
    bu_xue1_or_zhan_dou_fang_yu()

    wait_click_sleep('战斗/招将.png')
    fu_jiang_chu_zhan(1)
    bu_xue1_or_zhan_dou_fang_yu(is_fight=True)
    bu_xue2_or_zhan_dou_fang_yu()


def treat():
    while True:
        sun_xue = sun_shi_xue_liang()
        print(f'损失血量为: {sun_xue}')
        arr = chu_zhao_shun_xu(sun_xue)

        dead = dead_num()
        for i in range(4):
            if arr[i] == -1 or (i == 0 and dead < 5):
                wait_click_sleep('战斗/攻击.png', sleep_time=0.5)
                wait_click_sleep('战斗/红色.png', threshold=0.7, print_msg=False)
            else:
                bu_xue(arr[i])
        time.sleep(1)
        while True:
            after_chu_zhao()
            x, y = find('主界面/主界面.png')
            if x != -1:
                return
            x, y = find('战斗/物品.png')
            if x != -1:
                break


def fu_jiang_chu_zhan(row):
    all_find = wait_find_all_matches('副将/出战.png', print_msg=False)
    a, b = all_find[row - 1]
    click_global(a, b)
    time.sleep(1)


start_time = datetime.datetime.now()
fight_time = 0
escape_time = 0


def fight_time_add_print():
    global start_time, fight_time
    fight_time += 1
    t = (datetime.datetime.now() - start_time).total_seconds()
    print(f'第{fight_time}次刷图, 已逃跑{escape_time}次, 共花费{t}秒')


def escape_time_add_print():
    global start_time, escape_time
    escape_time += 1
    t = (datetime.datetime.now() - start_time).total_seconds()
    print(f'第{escape_time}次逃跑, 已刷图{fight_time}次, 共花费{t}秒')


def after_chu_zhao():
    while True:
        is_fight = any_match('战斗/攻击.png', '战斗/物品.png')
        if is_fight:
            return
        success_return()
        is_main = any_match('主界面/主界面.png', '主界面/人物.png')
        if is_main:
            return
        time.sleep(1)


def attack_one():
    attack_in_success(4, 5)
    time.sleep(3)
    if not total_num() == 5:
        escape_time_add_print()
        escape()
        return
    fight_time_add_print()
    wait_click_sleep('战斗/自动出招.png')
    time.sleep(2)
    while True:
        dead = dead_num()
        if dead >= 3:
            wait_click_sleep('战斗/手动出招.png')
            while True:
                time.sleep(1)
                dead = dead_num()
                if dead >= 4:
                    break
                else:
                    wait_click_sleep('战斗/攻击.png', sleep_time=0.5)
                    wait_click_sleep('战斗/红色.png', threshold=0.7, print_msg=False)
            zhao_fu_jiang()
            # treat()
            break
        time.sleep(1)


if __name__ == '__main__':
    ini.init_information()
    while True:
        attack_one()
