import pyautogui

import Global
from ai4 import count_people_status


def alive_and_dead_is_match(total, alive) -> bool:
    screen = pyautogui.screenshot(region=(Global.Pos.monster_area()))
    image = 'picture/temp1.png'
    screen.save(image)

    ad_dict = count_people_status(image)
    a = ad_dict['alive']
    d = ad_dict['dead']
    return a == alive and d >= total - alive


def dead_num() -> int:
    screen = pyautogui.screenshot(region=(Global.Pos.monster_area()))
    image = 'picture/temp1.png'
    screen.save(image)

    ad_dict = count_people_status(image)
    a = ad_dict['alive']
    d = ad_dict['dead']
    return d
