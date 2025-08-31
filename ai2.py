import cv2
from ultralytics import YOLO


def detect_monsters(image_path):
    # 加载图像
    image = cv2.imread(image_path)
    if image is None:
        print("无法加载图像，请检查路径")
        return

    # 加载YOLO模型
    model = YOLO('yolov8n.pt')  # 或使用自定义训练模型

    # 进行推理
    results = model.predict(source=image, conf=0.45, iou=0.6, imgsz=640)

    # 统计怪物数量
    monster_count = 0
    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls = int(box.cls)
            if model.names[cls] == 'monster':  # 根据实际类别标签调整
                monster_count += 1
                # 可选：在图像上绘制检测框
                xyxy = box.xyxy[0].cpu().numpy()
                cv2.rectangle(image, (int(xyxy[0]), int(xyxy[1])),
                              (int(xyxy[2]), int(xyxy[3])), (0, 255, 0), 2)

    print(f"检测到的怪物数量: {monster_count}")

    # 可选：显示带检测框的图像
    cv2.imshow('Detection Results', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect_monsters('game_screenshot.png')
