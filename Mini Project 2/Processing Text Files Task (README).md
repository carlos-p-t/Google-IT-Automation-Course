# Processing Text Files with Python Dictionaries and Uploading to Running Web Service

*From Coursera Google IT Automation with Python Professional Certificate, Course 6, [Module 2](https://www.coursera.org/learn/automating-real-world-tasks-python/ungradedLti/8A6mT/qwiklabs-assessment-process-text-files-with-python-dictionaries-and-upload-to)*.

## Introduction

This second mini-project is based on the scenario below. The objective is to interact with the operative system to process files and upload their content to a running web service.

Scenario: *You're working at a company that sells second-hand cars. Your company constantly collects feedback in the form of customer reviews. Your manager asks you to take those reviews (saved as .txt files) and display them on your company's website. To do this, you'll need to write a script to convert those .txt files and process them into Python dictionaries, then upload the data onto your company's website (currently using Django).*

## Tasks

- Use the Python OS module to process a directory of text files
- Manage information stored in Python dictionaries
- Use the Python requests module to upload content to a running Web service
- Understand basic operations for Python requests like GET and POST methods

## Results

Through the python OS module, the data in the .txt files was retrieved and stored in dictionaries as shown in the code. Since dictionaries are key-value data structures, they can be easily converted to JSON format. The program does that when making an HTTP POST request to the server. The following images show the before and after the program was executed.