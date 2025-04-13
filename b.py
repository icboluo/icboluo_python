import time

import pyautogui

from Tool import find, wait_click, wait_click_sleep, success_return, treat, wait_double_click_sleep


def attack_3time():
    for i in range(3):
        wait_click_sleep('战斗/攻击.png')
        wait_double_click_sleep('战斗/红色.png', '战斗/攻击.png')


def wait_click_skill_ret():
    time.sleep(2)
    i = 0
    while True:
        i += 1
        x, y = find('战斗/技能.png', 0.5)
        if x != -1:
            pyautogui.click(x, y)
            time.sleep(1)
            return True
        if i > 3:
            success_return()
            x3, y3 = find('主界面/人物.png')
            if x3 != -1:
                return False
            time.sleep(2)
        time.sleep(1)


def do_skill(skill_path):
    success = wait_click_skill_ret()
    if not success:
        return False
    wait_click_sleep(skill_path, 0.5)
    wait_click('战斗/红色.png', 0.5)
    time.sleep(0.5)
    return True


def move():
    find('主界面/移动.png')
    wait_click_sleep('主界面/移动.png')
    wait_click_sleep('移动/返回中心陈留.png')
    wait_click_sleep('主界面/设施.png')
    wait_double_click_sleep('设施/医馆.png', '主界面/设施.png')
    wait_click_sleep('设施/全员治疗.png')
    wait_click_sleep('设施/治疗结果.png')
    wait_click_sleep('设施/返回.png')
    wait_click_sleep('主界面/移动.png')
    wait_click_sleep('移动/陈留郊外.png')
    wait_click_sleep('移动/陈留西郊.png')
    wait_click_sleep('移动/先锋一营.png')
    wait_click_sleep('移动/先锋二营.png')
    wait_click_sleep('移动/先锋三营.png')
    wait_click_sleep('移动/先锋四营.png')
    wait_click_sleep('移动/先锋领军.png')
    wait_click_sleep('主界面/人物.png')


def fight():
    x, y = find('怪物/黄巾士兵.png')
    print(x, y)
    wait_double_click_sleep('怪物/黄巾士兵长.png', '主界面/人物.png', 0.5)
    if not do_skill('战斗/舍命一击.png'):
        return
    attack_3time()
    if not do_skill('战斗/力劈华山.png'):
        return
    # attack_3time()
    # if not do_skill('战斗/固若金汤.png'):
    #     return
    wait_click_sleep('战斗/自动出招.png')

    while True:
        success_return()
        x3, y3 = find('主界面/人物.png')
        if x3 != -1:
            return
        time.sleep(2)



if __name__ == "__main__":
    for i in range(21):
        print(f'第{i + 1}次刷图')
        # move()
        treat()
        print(f'第{i + 1}次刷图')
        fight()
