import os
from PIL import Image

# Đường dẫn đến folder chứa ảnh
folder_path = 'C:\\Users\\ADMIN\\Desktop\\Slide_School\\SlideKy7\\PBL6\\image_21_10'

# Kích thước mới
new_size = (640, 640)

# Tạo folder mới để lưu ảnh sau khi resize (nếu chưa có)
output_folder = 'C:\\Users\\ADMIN\\Desktop\\Slide_School\\SlideKy7\\PBL6\\image_21_10_640'
os.makedirs(output_folder, exist_ok=True)

# Lặp qua tất cả các file trong folder
for filename in os.listdir(folder_path):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):  # Chỉ lấy file ảnh
        img_path = os.path.join(folder_path, filename)
        
        # Mở ảnh và thay đổi kích thước
        with Image.open(img_path) as img:
            resized_img = img.resize(new_size)
            
            # Lưu ảnh đã resize vào folder mới
            resized_img.save(os.path.join(output_folder, filename))

print("Đã resize xong tất cả các ảnh.")
