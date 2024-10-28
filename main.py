import os
import cv2
import matplotlib.pyplot as plt
from PIL import Image
from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg
from paddleocr import PaddleOCR, draw_ocr


detector = PaddleOCR(use_angle_cls = False, lang = "vi", use_gpu = False, show_log=False)
FONT = "C:\\Users\\ADMIN\\Desktop\\Slide_School\\SlideKy7\\PBL6\\Preparation\\latin.ttf"

config = Cfg.load_config_from_name('vgg_transformer')
config['cnn']['pretrained'] = True
config['predictor']['beamsearch'] = True
config['device'] = 'cpu' # mps
recognitor = Predictor(config)

def predict(recognitor, detector, img_path, save_path, padding=4, dpi=100):
    img = cv2.imread(img_path)
    result = detector.ocr(img_path, cls=False, det=True, rec=False)
    result = result[:][:][0]

    boxes = []
    for line in result:
        boxes.append([[int(line[0][0]), int(line[0][1])], [int(line[2][0]), int(line[2][1])]])
    boxes = boxes[::-1]

    padding = 4
    for box in boxes:
        box[0][0] = box[0][0] - padding
        box[0][1] = box[0][1] - padding
        box[1][0] = box[1][0] + padding
        box[1][1] = box[1][1] + padding

    texts = []
    for box in boxes:
        cropped_image = img[box[0][1]:box[1][1], box[0][0]:box[1][0]]
        try:
            cropped_image = Image.fromarray(cropped_image)
        except:
            continue
        rec_result = recognitor.predict(cropped_image)
        text = rec_result
        texts.append(text)
    print("Result are: \n")
    for text in texts:
        print(text)
        
    return texts

# Predict
input_path = './images/image4.jpg' # Thế path vô chỗ ni
output_path = './output'
texts = predict(recognitor, detector, input_path, output_path, padding=2, dpi=100)