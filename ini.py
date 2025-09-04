from ultralytics import YOLO

from Global import Pos
from Tool import win_popup, wait_find


def init_information():
    window = win_popup()
    Pos.update_position(window.left, window.top, window.width, window.height)
    print(f'读取窗口成功，窗口位置：{Pos.win_position()}')
    x, y = wait_find('主界面/人物.png')
    Pos.update_figure(x, y)
    print(f'读取人物栏位置成功, 人物栏中心位置：{Pos.figure_position()}')
    print('初始化完成')

# if __name__ == '__main__':
#     init_information()
