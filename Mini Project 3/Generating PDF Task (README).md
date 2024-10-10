# Automatically Generate a PDF and sending it by E-mail

*From Coursera Google IT Automation with Python Professional Certificate, Course 6, [Module 3](https://www.coursera.org/learn/automating-real-world-tasks-python/ungradedLti/G2lUq/qwiklabs-assessment-automatically-generate-a-pdf-and-send-it-by-email)*

## Introduction

This third mini-project is based in the scenario below. The aim of the task is to process given information, create a PDF file with the summary of the analyzed information, and send it automatically by email. 

Scenario: *You work for a company that sells second hand cars. Management wants to get a summary of the amounts of vehicles that have been sold at the end of every month. The company already has a web service which serves sales data at the end of every month but management wants an email to be sent out with an attached PDF so that data is more easily readable*.

## Tasks

- Write a script that summarizes and processes sales data into different categories
- Generate a PDF using Python
- Automatically send a PDF by email

## Results

The *company* provided 3 files: **reports**, **emails**, and **cars**. The last one had **#TODO** sections that needed to be completed in order to run the program and achieve the desired results.

### Brief description of the programs

The [*reports*](https://github.com/carlos-p-t/Google-IT-Automation-Course/blob/main/Mini%20Project%203/reports.py) file generates PDF reports using the *reportlab* library. PDF reports include a title, additional information, and a table with data. 

The [*emails*](https://github.com/carlos-p-t/Google-IT-Automation-Course/blob/main/Mini%20Project%203/emails.py) file creates and sends an email with an attachment after passing needed data as sender, recipient, body, and the attachment. This file uses *smtplib* to send emails through a local SMTP server.

The [*reports*](https://github.com/carlos-p-t/Google-IT-Automation-Course/blob/main/Mini%20Project%203/reports.py) file's objective is to analyze car sales data and make use of the previous two programs to generate a report and send it by email. The program first loads the car sales data, which is a [JSON file](https://github.com/carlos-p-t/Google-IT-Automation-Course/blob/main/Mini%20Project%203/car_sales.json). The data is processed to find the car model with the most revenue, most sales, and the most popular year for sales. Then, the processed data is summarized and passed to *reports* t generate the PDF report. Lastly, *emails* is used to send this PDF report as an email attachment.

### Output

The first image below shows the inbox in the company's email interface with the last email received opened. There, it is possible to see the information requested as part of the email message and an attachment. The second image shows the attachment, which is the generated PDF report. [This report](https://github.com/carlos-p-t/Google-IT-Automation-Course/blob/main/Mini%20Project%203/report_cars.pdf) can be also displayed to see it with more detail.

<p align="center">
  <img src="https://github.com/carlos-p-t/Google-IT-Automation-Course/blob/main/Mini%20Project%203/inbox.jpg" alt="Description of the image" />
</p>
<p align="center">
  <em>Inbox displaying the last email message received.</em>
</p>

<p align="center">
  <img src="https://github.com/carlos-p-t/Google-IT-Automation-Course/blob/main/Mini%20Project%203/report.jpg" alt="Description of the image" />
</p>
<p align="center">
  <em>Visualzation of the PDF report sent as an attachment.</em>
</p>
