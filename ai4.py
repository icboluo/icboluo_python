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

            # 可视化标记
            color = (0, 255, 0) if status == "alive" else (0, 0, 255)
            cv2.rectangle(result.orig_img, (x1, y1), (x2, y2), color, 2)
            cv2.putText(result.orig_img, status, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    # 保存结果图像
    cv2.imwrite('output.jpg', result.orig_img)
    print(f"检测结果：存活 {status_count['alive']} 人，死亡 {status_count['dead']} 人")
    return status_count
