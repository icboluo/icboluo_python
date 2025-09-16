import time

import pyautogui
import pyperclip

import Global
import ini
import z


def paste_at_click_position():
    pyautogui.click(Global.Pos.win_l + 400, Global.Pos.win_t + 1180)
    # 安全设置：增加延迟防止失控
    pyautogui.PAUSE = 0.5
    pyautogui.FAILSAFE = True

    time.sleep(1)
    # 获取当前鼠标位置作为点击目标
    click_x, click_y = pyautogui.position()
    print(f"将在坐标({click_x}, {click_y})执行粘贴")

    # 移动鼠标并点击
    pyautogui.click(click_x, click_y)

    time.sleep(1)
    # 执行粘贴快捷键
    pyautogui.hotkey('ctrl', 'v')

    time.sleep(1)
    pyautogui.click(Global.Pos.win_l + 640, Global.Pos.win_t + 1190)

    time.sleep(1)
    pyautogui.click(Global.Pos.win_l + 630, Global.Pos.win_t + 1180)


if __name__ == "__main__":
    ini.init_information()
    for i in range(10):
        for it in z.tu:
            pyperclip.copy(it)
            paste_at_click_position()
            print("20秒后将获取鼠标点击位置...")
            time.sleep(20)
