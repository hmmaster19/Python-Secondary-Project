import sys
import os
from PIL import Image

# Create variables for system path and folders
img_folder = sys.argv[1]
save_folder = sys.argv[2]

# Check if folder exists, if not create folder

if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Loop through images in the directory and convert
for file in os.listdir(img_folder):
    img = Image.open(f'{img_folder}{file}')
    clean_name = os.path.splitext(file)[0]
    img.save(f'{save_folder}{clean_name}.png', 'png')
    print('Image converted')
 
#learnt that you have to read module and even the smallest possible error could make coding not work.
