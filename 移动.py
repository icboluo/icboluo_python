# 许昌--->洛阳
from Tool import wait_click_sleep


# 洛阳--->函谷关
def luo_yang__han_gu_guan():
    wait_click_sleep('主界面/移动.png')
    wait_click_sleep('移动/洛阳郊外.png')
    wait_click_sleep('移动/弘农.png')
    wait_click_sleep('移动/函谷关.png')


if __name__ == '__main__':
    luo_yang__han_gu_guan()
