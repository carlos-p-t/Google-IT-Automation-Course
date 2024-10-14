#! /usr/bin/env python3

import os
import requests

files_path = "supplier-data/descriptions" 
file_names = os.listdir(files_path)
headers = ["name", "weight", "description", "image_name"]

for file_name in file_names:
  with open(files_path + "/" + file_name, "r") as file:
    lines = file.readlines()
    info = {}
    for i in range(len(headers)):
      if i == 1:
        info[headers[i]] = int(lines[i][:-5])
      elif i == 3:
        info[headers[i]] = file_name[:-4] + ".jpeg"
      else:
        info[headers[i]] = lines[i].rstrip()
    #print(info)
    response = requests.post("http://34.169.31.139/fruits/", json = info)
    print(response.ok, response.status_code)