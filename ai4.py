import cv2
from ultralytics import YOLO


def analyze_person_status(roi):
    """分析人物区域状态（存活/死亡）"""
    # 姿势特征分析（宽高比）
    aspect_ratio = roi.shape[1] / roi.shape[0]

    # 综合判断（阈值可调整）
    if aspect_ratio > 1.5:
        return "dead"
    return "alive"


def count_people_status(image_path):
    """主检测函数"""
    model = YOLO('yolo11n.pt')
    results = model(image_path, classes=[0])

    status_count = {"alive": 0, "dead": 0}

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            person_img = cv2.imread(image_path)[y1:y2, x1:x2]

            status = analyze_person_status(person_img)
            status_count[status] += 1

    print(f"检测结果：存活 {status_count['alive']} 人，死亡 {status_count['dead']} 人")
    return status_count


if __name__ == '__main__':
    analyzer = GameCharacterAnalyzer()
    alive, dead = analyzer.detect_status("picture/alive2_dead2.png")
    print(f"检测完成：存活角色 {alive} 个，死亡角色 {dead} 个")
