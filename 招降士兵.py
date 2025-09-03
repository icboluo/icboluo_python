import time

from Tool import wait_click_sleep, attack_row_sleep, success_return, find, any_match


def zhao_xiang():
    wait_click_sleep('主界面/人物.png')
    for i in range(10):
        print(f'第{i + 1}次刷图')
        attack_row_sleep(2)
        time.sleep(1)
        while True:
            if any_match('战斗/自动出招.png', '战斗/手动出招.png'):
                x1, y1 = find('野怪/军官.png')
                if x1 == -1:
                    wait_click_sleep('战斗/自动出招.png')
                else:
                    break
            success_return()
            x3, y3 = find('主界面/主界面.png')
            if x3 != -1:
                break
            time.sleep(2)


if __name__ == '__main__':
    zhao_xiang()
