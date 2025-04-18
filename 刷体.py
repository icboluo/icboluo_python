import datetime
import time

from Tool import wait_click_sleep, success_return, find, click_global, find_all_matches, wait_is_first_max_match, \
    escape, any_match, wait_find_all_matches
from 回血 import bu_xue1_or_zhan_dou_fang_yu, sun_shi_xue_liang, chu_zhao_shun_xu, bu_xue, bu_xue2_or_zhan_dou_fang_yu
from 战斗 import attack_in_success


def zhao_fu_jiang():
    wait_click_sleep('战斗/招将.png')
    fu_jiang_chu_zhan(2)

    wait_click_sleep('战斗/招将.png')
    fu_jiang_chu_zhan(1)
    bu_xue1_or_zhan_dou_fang_yu()

    wait_click_sleep('战斗/招将.png')
    fu_jiang_chu_zhan(1)
    bu_xue1_or_zhan_dou_fang_yu(is_fight=True)
    bu_xue2_or_zhan_dou_fang_yu(is_fight=True)


def treat():
    while True:
        sun_xue = sun_shi_xue_liang()
        print(f'损失血量为: {sun_xue}')
        arr = chu_zhao_shun_xu(sun_xue)

        all_match_gw = find_all_matches('刷体/羽林军死亡.png')
        for i in range(4):
            if arr[i] == -1 or (i == 0 and len(all_match_gw) < 5):
                wait_click_sleep('战斗/攻击.png', sleep_time=0.5)
                wait_click_sleep('战斗/红色.png', threshold=0.7, print_msg=False)
            else:
                bu_xue(arr[i])
        time.sleep(1)
        after_chu_zhao()
        x, y = find('主界面/主界面.png')
        if x != -1:
            return


def fu_jiang_chu_zhan(row):
    all_find = wait_find_all_matches('副将/出战.png', print_msg=False)
    a, b = all_find[row - 1]
    click_global(a, b)
    time.sleep(1)


fight_time = 0
escape_time = 0


def fight_time_add_print(start):
    global fight_time
    fight_time += 1
    t = (datetime.datetime.now() - start).total_seconds()
    print(f'第{fight_time}次刷图, 已逃跑{escape_time}次, 共花费{t}秒')


def escape_time_add_print(start):
    global escape_time
    escape_time += 1
    t = (datetime.datetime.now() - start).total_seconds()
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


if __name__ == '__main__':
    start = datetime.datetime.now()
    while True:
        attack_in_success(1)
        is_first_match = wait_is_first_max_match('刷体/羽林军6.png', '刷体/羽林军4.png', '刷体/羽林军2.png')
        if is_first_match:
            fight_time_add_print(start)
            wait_click_sleep('战斗/自动出招.png')
            time.sleep(2)
            while True:
                all_match = find_all_matches('刷体/羽林军死亡.png')
                if len(all_match) >= 3:
                    wait_click_sleep('战斗/手动出招.png')
                    while True:
                        time.sleep(1)
                        all_match = find_all_matches('刷体/羽林军死亡.png')
                        if len(all_match) >= 4:
                            break
                        else:
                            wait_click_sleep('战斗/攻击.png', sleep_time=0.5)
                            wait_click_sleep('战斗/红色.png', threshold=0.7, print_msg=False)
                    zhao_fu_jiang()
                    treat()
                    break
                time.sleep(1)
        else:
            escape_time_add_print(start)
            escape()
