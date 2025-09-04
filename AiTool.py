import pyautogui
from ultralytics import YOLO

import Global

model = YOLO('best.pt')
print('加载大模型成功')


# 总数？
def alive_and_dead_is_match(total, alive) -> bool:
    screen = pyautogui.screenshot(region=(Global.Pos.monster_area()))
    image = 'picture/temp1.png'
    screen.save(image)

    ad_dict = count_people_status(image)
    a = ad_dict['alive']
    d = ad_dict['dead']
    return a == alive and d >= total - alive


def total_num() -> int:
    ad_dict = count_people_status()
    a = ad_dict['alive']
    d = ad_dict['dead']
    return a + d


def dead_num() -> int:
    screen = pyautogui.screenshot(region=(Global.Pos.monster_area()))
    results = model(screen, classes=[15, 16, 17, 18], save=True)

    # 处理检测结果
    status_count = {"alive": 0, "dead": 0}
    for det in results[0].boxes:
        class_id = int(det.cls)
        if class_id == 15 or class_id == 17:  # 假设0对应dog
            status_count['alive'] += 1
        elif class_id == 16:  # 假设1对应cat
            status_count['dead'] += 1

    return status_count['dead']


def count_people_status():
    screen = pyautogui.screenshot(region=(Global.Pos.monster_area()))
    results = model(screen, classes=[15, 16, 17, 18], save=True)

    # 处理检测结果
    status_count = {"alive": 0, "dead": 0}
    for det in results[0].boxes:
        class_id = int(det.cls)
        if class_id == 15 or class_id == 17:  # 假设0对应dog
            status_count['alive'] += 1
        elif class_id == 16:  # 假设1对应cat
            status_count['dead'] += 1

    print(f"检测结果：存活 {status_count['alive']} 人，死亡 {status_count['dead']} 人")
    return status_count

# if __name__ == '__main__':
#     count_people_status('picture/alive2_dead2.png')
