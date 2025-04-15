import pyautogui
import pygetwindow as gw
import pytesseract
from PIL import ImageEnhance, ImageFilter

# 配置路径
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Tesseract路径


def click_chinese_in_window(target_text):
    win = find_win()

    # 截取窗口区域
    left, top = win.left, win.top
    width, height = win.width, win.height
    screenshot = pyautogui.screenshot(region=(left, top, width, height))

    # 图像预处理
    processed = preprocess_image(screenshot)
    processed.save("processed_test.png")

    # OCR识别
    data = pytesseract.image_to_data(processed, lang="chi_sim", config="--psm 11 --oem 3",
                                     output_type=pytesseract.Output.DICT)

    # 查找目标文字
    for i in range(len(data["text"])):
        text = data["text"][i].strip()
        if text == target_text:
            x = left + data["left"][i] + data["width"][i] // 2
            y = top + data["top"][i] + data["height"][i] // 2
            pyautogui.click(x, y)
            return True
    return False


def preprocess_image(img):
    # 转灰度图 + 对比度增强
    gray = img.convert("L")
    enhancer = ImageEnhance.Contrast(gray)
    enhanced = enhancer.enhance(3.0)  # 增强对比度至300%
    # 二值化处理（阈值可调）
    binary = enhanced.point(lambda x: 255 if x > 180 else 0)
    # 锐化边缘
    sharpened = binary.filter(ImageFilter.SHARPEN)
    # 去噪（中值滤波）
    denoised = sharpened.filter(ImageFilter.MedianFilter(size=3))
    return denoised


def find_win():
    # 定位窗口
    windows = gw.getWindowsWithTitle('雷电模拟器')
    if not windows:
        return False
    win = windows[0]

    # 激活窗口
    win.restore()
    win.activate()
    pyautogui.sleep(0.5)

    return win


if __name__ == "__main__":
    # 执行查找点击（可设置尝试次数）
    click_chinese_in_window('虎')
