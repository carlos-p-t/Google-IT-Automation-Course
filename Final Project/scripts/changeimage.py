#! /usr/bin/env python3

from PIL import Image
import os

path = "supplier-data/images"
file_names = os.listdir(path)
image_names = [img for img in file_names if ".tiff" in img]

for image in image_names:
  file = Image.open(path + "/" + image)
  resized_image = file.resize((600, 400))
  reformatted_image = resized_image.convert("RGB")
  reformatted_image.save(path + "/" + image[:-5] + ".jpeg")