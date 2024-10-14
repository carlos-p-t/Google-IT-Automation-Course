# Automating updation of catalog information

*From Coursera Google IT Automation with Python Professional Certificate, Course 6, [Module 4](https://www.coursera.org/learn/automating-real-world-tasks-python/ungradedLti/TQTMk/qwiklabs-assessment-automate-updates-to-catalog-information)*

## Introduction

The aim of this final project is to combine all tools and knowlegde acquired throughout the lessons and previous tasks. The project is based in the scenario below:

Scenario: *You work for an online fruits store, and you need to develop a system that will update the catalog information with data provided by your suppliers. The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. The contents of the HTML file need to be uploaded to a web service that is already running using Django. You also need to gather the name and weight of all fruits from the .txt files and use a Python request to upload it to your Django server.*

*You will create a Python script that will process the images and descriptions and then update your company's online website to add the new products.*

*Once the task is complete, the supplier should be notified with an email that indicates the total weight of fruit (in lbs) that were uploaded. The email should have a PDF attached with the name of the fruit and its total weight (in lbs).*

*Finally, in parallel to the automation running, we want to check the health of the system and send an email if something goes wrong.* 

## Tasks

- Write a script that summarizes and processes sales data into different categories
- Generate a PDF using Python
- Automatically send a PDF by email
- Write a script to check the health status of the system

## Data

First, the information provided by the supplier was fetched from its storage in a Cloud Storage Bucket. The supplier had sent data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description).

Images cannot be uploaded here since the only way to access them was through Virtual Machines hosted by Google Servers. However, an example of the description of images can be found below:

*Mango* \
*300 lbs* \
*Mango contains higher levels of vitamin C than ordinary fruits. Eating mango can also reduce cholesterol and triglycerides, and help prevent cardiovascular disease. Due to its high level of vitamins, regular consumption of mango play an important role in improving body function and moisturizing the skin.*

The first line contains the name of the fruit followed by the weight of the fruit and finally the description of the fruit.

## Results

### Working with Supplier Images

The first program was written to work with supplier images. The program changes the image resolution from 3000x2000 to 600x400 pixels. It also changes the image format from ".TIFF" to ".JPEG". After executing the program, we can successfully see in the below image that the images were changed as required.

### Uploading Images to Web Server

The aim of the second program is to upload the reformatted images to the web server. The program successfully does that, and the results can be see in the comparison images below.

### Uploading the Descriptions

Following the images description format, the program separates the information into 4 categories: *"name", "weight", "description", and "image_name"*. Then, the information is converted into JSON object, similar to the one shown below:

*{"name": "Watermelon", "weight": 500, "description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of water, which is good for relieving the symptoms of acute fever immediately. The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower blood pressure.", "image_name": "010.jpeg"}*

After executing the program, the server displays the images as shown in the following image.

### Generating a PDF report and send it through email

Now that the images and descriptions are uploaded, the supplier needs to know about this. For that, a PDF file will be sent to the supplier, indicating that the data was correctly processed.

First, a script to generate the PDF report itself was written by using the *reportlab* library. Next, a program to send reports is created. The main function of this program requires 5 arguments: *sender, recipient, email subject, email body, and the path of the report (attachment)*.

Lastly, a last script was written where data is processed, and the main functions of the previous programs are called to generate the PDF report and send it by email. The following images show the online fruit store email system inbox, where it is possible to see that an email with an attachment was received, and the report as an attachment. The report can be displayed with more details here.

### Health Check

The last part of the project consisted on creating a program that runs in the background monitoring some of the system statistics: CPU usage, disk space, available memory and name resolution. If a problem is detected, the program should send a notification by email with details of the problem.

The possible problems that the program can alert about are:

- Error if CPU usage is over 80%
- Error if available disk space is lower than 20%
- Error if available memory is less than 100MB
- Error if the hostname "localhost" cannot be resolved to "127.0.0.1"

The program was written considering the above. Since the program will be running in the backrground, it will be executed every 60 seconds. Once an error is detected, an email will be sent as the image shown below: