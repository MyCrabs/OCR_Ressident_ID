from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg
from ultralytics import YOLO
import cv2
from PIL import Image
import matplotlib.pyplot as plt

config = Cfg.load_config_from_name("vgg_seq2seq")
config["cnn"]["pretrained"] = True
config["predictor"]["beamsearch"] = True
config["device"] = "cpu"
detector = YOLO("YOLO/model_28_10.pt")
recognitor = Predictor(config)

def predict(recognitor, detector, input_path, padding = 2, dpi=100):
    img = cv2.cvtColor(cv2.imread(input_path), cv2.COLOR_BGR2RGB)
    detect = detector(img)
    class_indexes = detect[0].boxes.cls.numpy()
    class_names = [detector.names[int(class_index)] for class_index in class_indexes]
    boxes = detect[0].boxes.xyxy.numpy()
    
    result_dict = {name: [] for name in detector.names.values()}
    for i, box in enumerate(boxes):
        box[0] = box[0] - padding
        box[1] = box[1] - padding
        box[2] = box[2] + padding
        box[3] = box[3] + padding   
        x1, y1, x2, y2 = box
        crop_img = img[int(y1):int(y2), int(x1):int(x2)]
        crop_img_rgb = Image.fromarray(crop_img)
        #color = class_colors.get(class_names[i], (255,255,255))
        text = recognitor.predict(crop_img_rgb)
        #img = cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), color = color, thickness=2)
        result_dict[class_names[i]].append(text)
        
    order_texts = [
        ', '.join(result_dict[detector.names[i]]) for i in sorted(detector.names)
    ]
    plt.figure(figsize=(6,6), dpi=dpi)
    plt.imshow(img)
    print(f"Result are: {order_texts}")
    return order_texts

# Predict
input_path = 'imagess/image45.jpg' # Thế path vô chỗ ni
texts = predict(recognitor, detector, input_path, padding=2, dpi=100)