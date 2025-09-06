import math
import time

import ini
from Tool import wait_click_sleep, success_return, find
from 回血 import get_xue_liang
from 战斗 import attack_in_success

# 许昌--->陈留
def xu_chang__chen_liu():
    wait_click_sleep('主界面/设施.png')
    wait_click_sleep('设施/馆驿.png')
    wait_click_sleep('设施/城市传送.png')
    wait_click_sleep('设施/向北往永州.png')
    wait_click_sleep('设施/确定传送.png')


# 陈留--->许昌
def chen_liu__xu_chang():
    wait_click_sleep('主界面/设施.png')
    wait_click_sleep('设施/馆驿.png')
    wait_click_sleep('设施/城市传送.png')
    wait_click_sleep('设施/向南往豫州.png')
    wait_click_sleep('设施/确定传送.png')


def treat_or_attach():
    wait_click_sleep('战斗/物品.png', sleep_time=0.5, threshold=0.7)
    wait_click_sleep('战斗/加1500.png', sleep_time=0.5)
    xue = get_xue_liang()
    print("血量剩余:", xue)
    if xue < 500:
        wait_click_sleep('战斗/红色.png', threshold=0.7)
    else:
        wait_click_sleep('战斗/返回.png', sleep_time=0.5, threshold=0.7)
        wait_click_sleep('战斗/攻击.png', sleep_time=0.5, threshold=0.7)
        wait_click_sleep('战斗/红色.png', threshold=0.7)


def attack(row):
    attack_in_success(row)
    if fight_time % 3 == 0:
        treat_or_attach()
    time.sleep(2)
    wait_click_sleep('战斗/自动出招.png')
    time.sleep(5)
    for j in range(1, 100):
        success_return()
        x3, y3 = find('主界面/人物.png', print_msg=j % 3 == 0)
        if x3 != -1:
            break
        time.sleep(2)


def attack_not_return(a, b, need_num, one_num):
    times = math.ceil(need_num / one_num)
    # times = 1
    for i in range(times):
        fight_time_add_print()
        attack(a)
        if b != -1:
            fight_time_add_print()
            attack(b)
    wait_click_sleep('主界面/移动.png')


fight_time = 0


def fight_time_add_print():
    global fight_time
    fight_time += 1
    print(f'第{fight_time}次刷图')


def attack_xu_chang_pan_jun():
    wait_click_sleep('主界面/移动.png')
    # 地痞
    wait_click_sleep('移动/许昌郊外.png')
    attack_not_return(4, -1, 10, 4)
    # 屯田兵
    wait_click_sleep('移动/颍阳.png')
    attack_not_return(3, -1, 10, 4)
    wait_click_sleep('移动/叛军一营.png')
    # 道士、老道
    wait_click_sleep('移动/叛军二营.png')
    attack_not_return(3, 4, 30, 4)
    # 术士、妖人
    wait_click_sleep('移动/叛军三营.png')
    attack_not_return(3, 4, 30, 4)
    # 恶僧、头陀
    wait_click_sleep('移动/叛军四营.png')
    attack_not_return(3, 4, 30, 4)
    # 僵尸、游魂
    wait_click_sleep('移动/叛军五营.png')
    attack_not_return(3, 4, 30, 4)
    print('许昌--->叛军五营 刷完一遍')
    wait_click_sleep('移动/返回中心许昌.png')


def attack_xu_chang_xi_jiao():
    wait_click_sleep('主界面/移动.png')
    wait_click_sleep('移动/许昌郊外.png')
    # 街匪
    wait_click_sleep('移动/许昌西郊.png')
    attack_not_return(3, -1, 10, 4)
    # 贪官、假道学
    wait_click_sleep('移动/长社.png')
    attack_not_return(3, 4, 10, 4)
    # 污吏、酷吏
    wait_click_sleep('移动/中牟.png')
    attack_not_return(3, 4, 10, 4)

    wait_click_sleep('移动/返回中心许昌.png')
    wait_click_sleep('移动/许昌郊外.png')
    wait_click_sleep('移动/许昌西郊.png')
    # 路霸
    wait_click_sleep('移动/颍川.png')
    attack_not_return(3, -1, 10, 4)
    # 屯田兵
    wait_click_sleep('移动/颍阳.png')
    attack_not_return(3, -1, 10, 4)
    print('许昌西郊 刷完一遍')
    wait_click_sleep('移动/返回中心许昌.png')


def attack_xu_chang_cheng():
    wait_click_sleep('主界面/移动.png')
    wait_click_sleep('移动/许昌郊外.png')
    # 贪官
    wait_click_sleep('移动/陈.png')
    attack_not_return(3, -1, 10, 4)
    # 酸丁
    wait_click_sleep('移动/谯郡.png')
    attack_not_return(3, -1, 10, 4)
    # 乡绅
    wait_click_sleep('移动/颖水.png')
    attack_not_return(3, -1, 10, 4)

    wait_click_sleep('移动/返回中心许昌.png')
    wait_click_sleep('移动/许昌郊外.png')
    wait_click_sleep('移动/陈.png')
    # 虎豹骑
    wait_click_sleep('移动/蔡县.png')
    attack_not_return(4, -1, 10, 4)
    # 腐儒
    wait_click_sleep('移动/颍阳.png')
    attack_not_return(3, -1, 10, 4)
    print('许昌--->陈 刷完一遍')
    wait_click_sleep('移动/返回中心许昌.png')


def attack_chen_liu_xi_jiao():
    wait_click_sleep('主界面/移动.png')
    wait_click_sleep('移动/陈留郊外.png')
    # 矿石大盗、宝石大盗
    wait_click_sleep('移动/陈留西郊.png')
    attack_not_return(3, 4, 50, 6)
    # 力士、斧手
    wait_click_sleep('移动/先锋一营.png')
    attack_not_return(4, 5, 30, 4)
    # 恶仆、女贼
    wait_click_sleep('移动/先锋二营.png')
    attack_not_return(4, 5, 30, 4)
    # 败类、凶徒
    wait_click_sleep('移动/先锋三营.png')
    attack_not_return(4, 5, 30, 4)
    # 恶棍、囚徒
    wait_click_sleep('移动/先锋四营.png')
    attack_not_return(4, 5, 30, 4)
    # 黄巾士兵、黄巾精兵
    wait_click_sleep('移动/先锋领军.png')
    attack_not_return(4, 5, 50, 5)
    print('陈留西郊 刷完一遍')
    wait_click_sleep('移动/返回中心陈留.png')


def attack_chen_liu_ding_tao():
    wait_click_sleep('主界面/移动.png')
    wait_click_sleep('移动/陈留郊外.png')
    # 白银大盗、黄金大盗
    wait_click_sleep('移动/定陶.png')
    attack_not_return(3, 4, 50, 6)
    # 独行大盗、采花大盗

    wait_click_sleep('移动/濮阳南郊.png')
    attack_not_return(3, 4, 50, 6)
    # 绿林大盗、江洋大盗
    wait_click_sleep('移动/濮阳郊外.png')
    attack_not_return(4, 5, 50, 6)
    # 黄巾骑士、黄巾头领
    wait_click_sleep('移动/白马.png')
    attack_not_return(3, 4, 50, 5)
    print('陈留--->定陶 刷完一遍')
    wait_click_sleep('移动/返回中心陈留.png')


if __name__ == '__main__':
    ini.init_information()
    for i in range(10):
        attack_xu_chang_pan_jun()
        attack_xu_chang_xi_jiao()
        attack_xu_chang_cheng()
        xu_chang__chen_liu()

        attack_chen_liu_xi_jiao()
        attack_chen_liu_ding_tao()
        chen_liu__xu_chang()
