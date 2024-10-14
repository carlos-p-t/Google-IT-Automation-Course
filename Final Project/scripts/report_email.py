#! /usr/bin/env python3

import os
from datetime import date
import reports
import sys
import emails

def process_data():
  files_path = "supplier-data/descriptions/"
  file_names = os.listdir(files_path)
  summary = []
  for file_name in file_names: 
    with open(files_path + file_name, "r") as file:
      lines = file.readlines()
      summary.append("name: " + lines[0].rstrip() + "<br/>" + "weight: " + lines[1].rstrip() + "<br/>")
  return summary

def main(argv):
  summary = process_data()
  today_date = date.today()
  formatted_today = str(today_date.strftime("%B %d, %Y"))
  #print(summary)
  reports.generate_report("/tmp/processed.pdf", "Processed Update on " + formatted_today, "<br/>".join(summary))
  sender = "automation@example.com"
  receiver = "student@example.com"
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email"
  message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
  emails.send_email(message)

if __name__ == "__main__":
  main(sys.argv)