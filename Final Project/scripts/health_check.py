#! /usr/bin/env python3

import shutil
import psutil
import socket
import time
import sys
import emails

def check_cpu_usage():
  cpu_usage = psutil.cpu_percent(interval = 1)
  return cpu_usage

def check_disk_space():
  total, used, free = shutil.disk_usage("/")
  free_percent = (free/total)*100
  return free_percent

def check_memory():
  available_memory = psutil.virtual_memory().available / (1024**2)
  return available_memory

def check_hostname_resolution():
  resolved_ip = socket.gethostbyname("localhost")
  return resolved_ip

def main(argv):
  while True:
    cpu_usage = check_cpu_usage()
    free_percent = check_disk_space()
    available_memory = check_memory()
    resolution = check_hostname_resolution()
  
    if cpu_usage > 80:
      #case = "CPU usage is over 80%"
      subject = "Error - CPU usage is over 80%"
    elif free_percent < 20:
      #case = "Available disk space is lower than 20%"
      subject = "Error - Available disk space is less than 20%"
    elif available_memory < 100:
      #case = "available memory is less than 100MB"
      subject = "Error - Available memory is less than 100MB"
    elif resolution != "127.0.0.1":
      #case = "hostname 'localhost' cannot be resolved to '127.0.0.1'"
      subject = "Error - localhost cannot be resolved to 127.0.0.1"

    sender = "automation@example.com"
    receiver = "student@example.com"
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_error_report(sender, receiver, subject, body)
    emails.send_email(message)
    time.sleep(60)

if __name__ == "__main__":
  main(sys.argv)