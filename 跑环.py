from pyautogui import moveTo

from Tool import wait_click_sleep, move, read_win_popup_safe


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


def p():
    wait_click_sleep('主界面/人物.png')
    move('npc/糜芳.png')


if __name__ == '__main__':
    xia_pi__xu_chang()
