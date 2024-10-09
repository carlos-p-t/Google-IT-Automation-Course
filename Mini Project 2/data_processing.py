import os
import requests

# Defining path to retrieve information from files
path = "/data/feedback/"
file_names = os.listdir(path)
headers = ['title', 'name', 'date', 'feedback'] # Contents 

# Going through all files
for f in file_names:
  with open(path + f, "r") as file:
    lines = file.readlines()
    info = {}
    for i in range(len(headers)):
      info[headers[i]] = lines[i].rstrip() # Previously visualized, information was stored in each line of the text file
    response = requests.post("http://34.145.100.170/feedback/", json = info)
    print(response.ok, response.status_code)