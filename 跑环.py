import time

from Tool import wait_click_sleep, success_return, find
from 回血 import get_xue_liang
from 战斗 import attack_in_success


# 许昌--->陈留
def xu_chang__xia_pi():
    wait_click_sleep('主界面/设施.png')
    wait_click_sleep('设施/馆驿.png')
    wait_click_sleep('设施/城市传送.png')
    wait_click_sleep('设施/向北往永州.png')
    wait_click_sleep('设施/确定传送.png')


# 陈留--->许昌
def xia_pi__xu_chang():
    wait_click_sleep('主界面/设施.png')
    wait_click_sleep('设施/馆驿.png')
    wait_click_sleep('设施/城市传送.png')
    wait_click_sleep('设施/向南往豫州.png')
    wait_click_sleep('设施/确定传送.png')


def move12_to_huang_jin_qi_bing():
    wait_click_sleep('主界面/移动.png')
    wait_click_sleep('移动/陈留郊外.png')
    wait_click_sleep('移动/定陶.png')
    wait_click_sleep('移动/濮阳南郊.png')
    wait_click_sleep('移动/濮阳郊外.png')
    wait_click_sleep('移动/白马.png')
    return 3, 4


def move13_to_du_xing_da_dao():
    wait_click_sleep('主界面/移动.png')
    wait_click_sleep('移动/陈留郊外.png')
    wait_click_sleep('移动/定陶.png')
    wait_click_sleep('移动/濮阳南郊.png')
    return 3, 4


# 5个怪物
def move14_to_lv_ling_da_dao():
    wait_click_sleep('主界面/移动.png')
    wait_click_sleep('移动/陈留郊外.png')
    wait_click_sleep('移动/定陶.png')
    wait_click_sleep('移动/濮阳南郊.png')
    wait_click_sleep('移动/濮阳郊外.png')
    return 4, 5


# 6个怪物
def move15_to_kuang_shi_da_dao():
    wait_click_sleep('主界面/移动.png')
    wait_click_sleep('移动/陈留郊外.png')
    wait_click_sleep('移动/陈留西郊.png')
    return 3, 4


# 6个怪物
def move16_to_bai_ying_da_dao():
    wait_click_sleep('主界面/移动.png')
    wait_click_sleep('移动/陈留郊外.png')
    wait_click_sleep('移动/定陶.png')
    return 3, 4


def treat_or_attach():
    wait_click_sleep('战斗/物品.png', sleep_time=0.5, threshold=0.7)
    wait_click_sleep('战斗/加2000.png', sleep_time=0.5)
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
    # if fight_time % 3 == 0:
    #     treat_or_attach()
    wait_click_sleep('战斗/自动出招.png')
    time.sleep(5)
    for j in range(1, 100):
        success_return()
        x3, y3 = find('主界面/人物.png', print_msg=j % 3 == 0)
        if x3 != -1:
            break
        time.sleep(2)


def attack_then_return(a, b):
    for i in range(10):
        fight_time_add_print()
        attack(a)
        fight_time_add_print()
        attack(b)
    wait_click_sleep('主界面/移动.png')
    wait_click_sleep('移动/返回中心陈留.png')


def attack_not_return(a, b, times):
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


def move_3to_hu_bao_qi():
    wait_click_sleep('主界面/移动.png')
    wait_click_sleep('移动/许昌郊外.png')
    wait_click_sleep('移动/颍阳.png')
    wait_click_sleep('移动/蔡县.png')
    return 4, -1


def move_4to_fu_ru():
    wait_click_sleep('主界面/移动.png')
    wait_click_sleep('移动/许昌郊外.png')
    wait_click_sleep('移动/陈.png')
    wait_click_sleep('移动/谯郡.png')
    wait_click_sleep('移动/南顿.png')
    return 3, -1


def move_5to_jie_fei():
    wait_click_sleep('主界面/移动.png')
    wait_click_sleep('移动/许昌郊外.png')
    wait_click_sleep('移动/许昌西郊.png')
    return 3, -1


def move_6to_tan_guan():
    wait_click_sleep('主界面/移动.png')
    wait_click_sleep('移动/许昌郊外.png')
    wait_click_sleep('移动/陈.png')
    return 3, -1


def move_7to_suan_ding():
    wait_click_sleep('主界面/移动.png')
    wait_click_sleep('移动/许昌郊外.png')
    wait_click_sleep('移动/陈.png')
    wait_click_sleep('移动/谯郡.png')
    return 3, -1


def move_8to_xiang_shen():
    wait_click_sleep('主界面/移动.png')
    wait_click_sleep('移动/许昌郊外.png')
    wait_click_sleep('移动/陈.png')
    wait_click_sleep('移动/谯郡.png')
    wait_click_sleep('移动/颖水.png')
    return 3, -1


def move_9to_jia_dao_xue():
    wait_click_sleep('主界面/移动.png')
    wait_click_sleep('移动/许昌郊外.png')
    wait_click_sleep('移动/许昌西郊.png')
    wait_click_sleep('移动/长社.png')
    return 3, 4


def move_10to_wu_li():
    wait_click_sleep('主界面/移动.png')
    wait_click_sleep('移动/许昌郊外.png')
    wait_click_sleep('移动/许昌西郊.png')
    wait_click_sleep('移动/长社.png')
    wait_click_sleep('移动/中牟.png')
    return 3, 4


def move_11to_lu_ba():
    wait_click_sleep('主界面/移动.png')
    wait_click_sleep('移动/许昌郊外.png')
    wait_click_sleep('移动/颍阳.png')
    wait_click_sleep('移动/颍川.png')
    return 3, -1


def attack_xian_feng():
    wait_click_sleep('主界面/移动.png')
    wait_click_sleep('移动/陈留郊外.png')
    # 矿石大盗、宝石大盗 100/6
    wait_click_sleep('移动/陈留西郊.png')
    attack_not_return(3, 4, 17)
    # 力士、斧手
    wait_click_sleep('移动/先锋一营.png')
    attack_not_return(4, 5, 60 / 4)
    # 恶仆、女贼
    wait_click_sleep('移动/先锋二营.png')
    attack_not_return(4, 5, 60 / 4)
    # 败类、凶徒
    wait_click_sleep('移动/先锋三营.png')
    attack_not_return(4, 5, 60 / 4)
    # 恶棍、囚徒
    wait_click_sleep('移动/先锋四营.png')
    attack_not_return(4, 5, 60 / 4)
    # 黄巾士兵、黄巾精兵
    wait_click_sleep('移动/先锋领军.png')
    attack_not_return(4, 5, 100 / 5)
    wait_click_sleep('移动/返回中心陈留.png')


def attack_pan_jun():
    wait_click_sleep('主界面/移动.png')
    # 地痞
    wait_click_sleep('移动/许昌郊外.png')
    attack_not_return(4, -1, 5)
    # 屯田兵
    wait_click_sleep('移动/颍阳.png')
    attack_not_return(3, -1, 5)
    wait_click_sleep('移动/叛军一营.png')
    # 道士、老道
    wait_click_sleep('移动/叛军二营.png')
    attack_not_return(3, 4, 15)
    # 术士、妖人
    wait_click_sleep('移动/叛军三营.png')
    attack_not_return(3, 4, 15)
    # 恶僧、头陀
    wait_click_sleep('移动/叛军四营.png')
    attack_not_return(3, 4, 15)
    # 僵尸、游魂
    wait_click_sleep('移动/叛军五营.png')
    attack_not_return(3, 4, 15)
    print('叛军五营刷完一遍')
    wait_click_sleep('移动/返回中心许昌.png')


def attack_chen_liu():
    a, b = move12_to_huang_jin_qi_bing()
    attack_then_return(a, b)
    a, b = move13_to_du_xing_da_dao()
    attack_then_return(a, b)
    a, b = move14_to_lv_ling_da_dao()
    attack_then_return(a, b)
    a, b = move15_to_kuang_shi_da_dao()
    attack_then_return(a, b)
    a, b = move16_to_bai_ying_da_dao()
    attack_then_return(a, b)


def attack_then_return_xu_chang(a, b):
    for i in range(5):
        fight_time_add_print()
        attack(a)
        if b != -1:
            fight_time_add_print()
            attack(b)
    wait_click_sleep('主界面/移动.png')
    wait_click_sleep('移动/返回中心许昌.png')


def attack_10():
    a, b = move_3to_hu_bao_qi()
    attack_then_return_xu_chang(a, b)
    a, b = move_4to_fu_ru()
    attack_then_return_xu_chang(a, b)
    a, b = move_5to_jie_fei()
    attack_then_return_xu_chang(a, b)
    a, b = move_6to_tan_guan()
    attack_then_return_xu_chang(a, b)
    a, b = move_7to_suan_ding()
    attack_then_return_xu_chang(a, b)
    a, b = move_8to_xiang_shen()
    attack_then_return_xu_chang(a, b)
    a, b = move_9to_jia_dao_xue()
    attack_then_return_xu_chang(a, b)
    a, b = move_10to_wu_li()
    attack_then_return_xu_chang(a, b)
    a, b = move_11to_lu_ba()
    attack_then_return_xu_chang(a, b)


if __name__ == '__main__':
    for i in range(100):
        attack_pan_jun()
