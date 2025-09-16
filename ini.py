import yaml

from Global import Pos
from Tool import win_popup, wait_find


def init_information():
    window = win_popup()
    Pos.update_position(window.left, window.top, window.width, window.height)
    print(f'读取窗口成功，窗口位置：{Pos.win_position()}')
    x, y = wait_find('主界面/人物.png')
    Pos.update_figure(x, y)
    print(f'读取人物栏位置成功, 人物栏中心位置：{Pos.figure_position()}')
    ini_data()
    print('读取data.yml成功')
    print('初始化完成')


def ini_data():
    with open('data.yml', 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    result_dict = {item: idx for idx, item in enumerate(data['names'])}
    Pos.name_id_dict = result_dict


if __name__ == '__main__':
    ini_data()
    a = Pos.name_id_dict['dead']
    b = Pos.name_id_dict['alive']
    print()
