import time

from Tool import wait_find_second_when_multiple_click_first, attack_row_sleep, find, click_global, wait_find_all_matches


# 攻击进入副本
def attack_in_success(row, total=0):
    wait_find_second_when_multiple_click_first('主界面/人物.png', 'npc/战斗.png')
    for i in range(10):
        if total != 0:
            arr = wait_find_all_matches('npc/战斗.png')
            if len(arr) != total:
                raise ValueError
        attack_row_sleep(row)
        x, y = find('npc/确定.png')
        if x != -1:
            click_global(x, y)
        else:
            break
        time.sleep(1)
