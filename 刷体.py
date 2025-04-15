import time

from Tool import wait_click_sleep, attack_row_sleep, \
    success_return, find, click_global, find_all_matches, wait_is_first_max_match, \
    wait_find_second_when_multiple_click_first, escape
from 回血 import bu_xue1_or_fang_yu, sun_shi_xue_liang, chu_zhao_shun_xu, bu_xue, bu_xue2_or_fang_yu


def zhao_fu_jiang():
    wait_click_sleep('战斗/招将.png')
    time.sleep(1)
    fu_jiang_chu_zhan(2)

    wait_click_sleep('战斗/招将.png')
    time.sleep(1)
    fu_jiang_chu_zhan(1)
    bu_xue1_or_fang_yu()

    wait_click_sleep('战斗/招将.png')
    time.sleep(1)
    fu_jiang_chu_zhan(1)
    bu_xue1_or_fang_yu()
    bu_xue2_or_fang_yu()


def treat():
    while True:
        sun_xue = sun_shi_xue_liang()
        print(f'损失血量为: {sun_xue}')
        arr = chu_zhao_shun_xu(sun_xue)

        all_match_gw = find_all_matches('刷体/羽林军死亡.png')
        for i in range(4):
            if arr[i] == -1 or (i == 0 and len(all_match_gw) < 5):
                wait_click_sleep('战斗/攻击.png')
                wait_click_sleep('战斗/红色.png', threshold=0.7)
            else:
                bu_xue(arr[i])
        while True:
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
    all_find = find_all_matches('副将/出战.png')
    a, b = all_find[row - 1]
    click_global(a, b)
    time.sleep(2)


if __name__ == '__main__':
    while True:
        wait_find_second_when_multiple_click_first('主界面/人物.png', 'npc/战斗.png')
        for i in range(10):
            attack_row_sleep(4)
            x, y = find('npc/确定.png')
            if x != -1:
                click_global(x, y)
            else:
                break
            time.sleep(1)
        is_first_match = wait_is_first_max_match('刷体/羽林军6.png', '刷体/羽林军4.png', '刷体/羽林军2.png')
        if is_first_match:
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
                            wait_click_sleep('战斗/攻击.png')
                            wait_click_sleep('战斗/红色.png')
                    zhao_fu_jiang()
                    treat()
                    break
                time.sleep(1)
        else:
            escape()
