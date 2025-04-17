import time

from Tool import wait_click_sleep, attack_row_sleep, success_return, find, wait_double_find_sleep
from 回血 import get_xue_liang
from 战斗 import attack_in_success


def da_guai():
    attack_in_success(3)
    wait_click_sleep('战斗/物品.png', threshold=0.7)
    wait_click_sleep('战斗/加2000.png', sleep_time=0.5)
    xue = get_xue_liang()
    print("血量剩余:", xue)
    if xue < 500:
        wait_click_sleep('战斗/红色.png', threshold=0.7)
    else:
        wait_click_sleep('战斗/返回.png', threshold=0.7)
        wait_click_sleep('战斗/攻击.png', threshold=0.7)
        wait_click_sleep('战斗/红色.png', threshold=0.7)

    wait_click_sleep('战斗/自动出招.png')
    time.sleep(5)
    for j in range(1, 100):
        success_return()
        x3, y3 = find('主界面/人物.png', print_msg=j % 3 == 0)
        if x3 != -1:
            break
        time.sleep(2)


def da_guai2():
    wait_click_sleep('主界面/人物.png')
    wait_double_find_sleep('npc/战斗.png', '主界面/人物.png')
    attack_row_sleep(4)
    wait_click_sleep('战斗/自动出招.png')
    time.sleep(5)
    for j in range(1, 100):
        success_return()
        x3, y3 = find('主界面/人物.png', print_msg=j % 3 == 0)
        if x3 != -1:
            break
        time.sleep(2)


if __name__ == '__main__':
    for i in range(1, 200):
        print(f'第{i * 2 - 1}次刷图')
        da_guai()
        print(f'第{i * 2}次刷图')
        da_guai2()
