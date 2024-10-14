#! /usr/bin/env python3

import requests
import os

path = "supplier-data/images"
file_names = os.listdir(path)
image_names = [img for img in file_names if ".jpeg" in img]
#print(image_names)
url = "http://localhost/upload/"

for image in image_names:
  with open(path + "/" + image, "rb") as opened:                 
    r = requests.post(url, files = {"file":opened})