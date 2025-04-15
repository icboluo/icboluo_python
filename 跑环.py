import time

from Tool import wait_click_sleep, one_row_click_end, next_step, success_return, find, \
    attack_row_sleep


# 许昌--->下邳
def xu_chang__xia_pi():
    wait_click_sleep('主界面/设施.png')
    wait_click_sleep('设施/馆驿.png')
    wait_click_sleep('设施/城市传送.png')
    wait_click_sleep('设施/向东往徐州.png')
    wait_click_sleep('设施/确定传送.png')


# 下邳--->许昌
def xia_pi__xu_chang():
    wait_click_sleep('主界面/设施.png')
    wait_click_sleep('设施/馆驿.png')
    wait_click_sleep('设施/城市传送.png')
    wait_click_sleep('设施/向西往豫州.png')
    wait_click_sleep('设施/确定传送.png')


# 许昌--->洛阳
def xu_chang__luo_yang():
    wait_click_sleep('主界面/设施.png')
    wait_click_sleep('设施/馆驿.png')
    wait_click_sleep('设施/城市传送.png')
    wait_click_sleep('设施/向西北往司隶.png')
    wait_click_sleep('设施/确定传送.png')


def py():
    wait_click_sleep('主界面/人物.png')
    one_row_click_end('npc/糜芳.png', 'npc/对话.png')


def ph():
    wait_click_sleep('主界面/人物.png')
    one_row_click_end('npc/跑环使者.png', 'npc/对话.png')
    next_step('npc/跑环点击.png')


def da_guai():
    wait_click_sleep('主界面/人物.png')
    for i in range(9):
        print(f'第{i + 1}次刷图')
        attack_row_sleep(4)
        time.sleep(1)
        wait_click_sleep('战斗/自动出招.png')
        while True:
            success_return()
            x3, y3 = find('主界面/人物.png')
            if x3 != -1:
                break
            time.sleep(2)


if __name__ == '__main__':
    xu_chang__luo_yang()
