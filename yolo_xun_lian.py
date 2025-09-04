from ultralytics import YOLO

model = YOLO('yolo11n.pt')
model.train(
    data='data.yml',
    epochs=200,  # 训练次数
    imgsz=640,  # 图片尺寸，会进行统一转换
    batch=16,
    device='cpu'  # gpu->0,cpu->'CPU'
)
print('模型训练完毕')
