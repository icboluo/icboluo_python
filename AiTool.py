import pyautogui
from ultralytics import YOLO

import Global

model = YOLO('best.pt')
print('加载大模型成功')

def total_num() -> int:
    ad_dict = count_people_status()
    a = ad_dict['alive']
    d = ad_dict['dead']
    return a + d


def alive_num() -> int:
    ad_dict = count_people_status()
    return ad_dict['alive']


def dead_num() -> int:
    ad_dict = count_people_status()
    return ad_dict['dead']


def count_people_status():
    screen = pyautogui.screenshot(region=(Global.Pos.monster_area()))

    a = Global.Pos.name_id_dict['alive']
    d = Global.Pos.name_id_dict['dead']
    results = model(screen, classes=[a, d], save=True)

    # 处理检测结果
    status_count = {"alive": 0, "dead": 0}
    for det in results[0].boxes:
        class_id = int(det.cls)
        if class_id == a:
            status_count['alive'] += 1
        elif class_id == d:
            status_count['dead'] += 1

    print(f"检测结果：存活 {status_count['alive']} 人，死亡 {status_count['dead']} 人")
    return status_count

# if __name__ == '__main__':
#     count_people_status('picture/alive2_dead2.png')
