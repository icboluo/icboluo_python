import time

from Tool import wait_click_sleep, attack_row_sleep, success_return, find, treat, wait_find, wait_double_click_sleep, \
    wait_double_find_sleep, wait_click


def da_guai():
    wait_click_sleep('主界面/人物.png')
    wait_double_find_sleep('npc/战斗.png', '主界面/人物.png')
    attack_row_sleep(4)
    wait_click_sleep('战斗/自动出招.png')
    time.sleep(15)
    for j in range(1, 100):
        success_return()
        x3, y3 = find('主界面/人物.png', print_msg=j % 3 == 0)
        if x3 != -1:
            break
        time.sleep(2)


def yong_yao_da_guai():
    wait_click_sleep('主界面/人物.png')
    wait_double_find_sleep('npc/战斗.png', '主界面/人物.png')
    attack_row_sleep(3)
    wait_click_sleep('战斗/物品.png')
    wait_click_sleep('战斗/加2000.png')
    wait_click_sleep('战斗/红色.png', 0.5)
    wait_click_sleep('战斗/自动出招.png')
    time.sleep(15)
    for j in range(1, 100):
        success_return()
        x3, y3 = find('主界面/人物.png', print_msg=j % 3 == 0)
        if x3 != -1:
            break
        time.sleep(2)


if __name__ == '__main__':
    for i in range(1, 100):
        for j in range(1, 4):
            print(f'第{i * 4 + j - 4}次刷图')
            da_guai()
        yong_yao_da_guai()
