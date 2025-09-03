import pyautogui

import Global
import ini
from ai4 import count_people_status


# 截图怪物区域
def screen_monster():
    screen = pyautogui.screenshot(region=(Global.Pos.monster_area()))
    screen.save('picture/alive2_dead2.png')


if __name__ == '__main__':
    # ini.init_information()
    count_people_status('picture/alive2_dead2.png')
    # screen_monster()
