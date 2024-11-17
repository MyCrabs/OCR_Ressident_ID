# def count_lines(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         line_count = sum(1 for line in file)
#     return line_count

# # Ví dụ sử dụng
# file_path = "C:\\Users\\ADMIN\\Desktop\\meta\\rec\\rec_gt_train.txt"
# num_lines = count_lines(file_path)
# print(f"Số dòng trong file là: {num_lines}")
import os

def count_image_files(folder_path):
    image_extensions = ('.jpg', '.jpeg', '.png')
    image_count = sum(1 for file in os.listdir(folder_path) if file.lower().endswith(image_extensions))
    return image_count

# Ví dụ sử dụng
folder_path = 'C:\\Users\\ADMIN\\Desktop\\meta\\rec\\train'
num_images = count_image_files(folder_path)
print(f"Số lượng file ảnh trong thư mục là: {num_images}")

