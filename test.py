import pyautogui

import Global
import ini


# 截图怪物区域
def screen_monster():
    screen = pyautogui.screenshot(region=(Global.Pos.monster_area()))
    screen.save('picture/alive2_dead2.png')


if __name__ == '__main__':
    ini.init_information()
    # screen_monster()
    screen = pyautogui.screenshot(region=(Global.Pos.win_position_tup()))
    screen.save('picture/加1500.png')
