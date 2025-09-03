from ultralytics import YOLO

model = YOLO('yolo11n.pt')

image = '刷体/temp1.png'

results = model(image, show=True, save=True)


