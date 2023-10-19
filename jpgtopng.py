import sys
import os
from PIL import Image

Image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for file in os.listdir(Image_folder):
    img = Image.open(f'{Image_folder}{file}')
    clean_name = os.path.splitext(file)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')