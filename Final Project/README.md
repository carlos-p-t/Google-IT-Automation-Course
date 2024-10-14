# Automating updation of catalog information

*From Coursera Google IT Automation with Python Professional Certificate, Course 6, [Module 4](https://www.coursera.org/learn/automating-real-world-tasks-python/ungradedLti/TQTMk/qwiklabs-assessment-automate-updates-to-catalog-information)*

## Introduction

The aim of this final project is to combine all the tools and knowlegde acquired throughout the lessons and previous tasks. The project is based in the scenario below:

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

First, the information provided by the supplier was fetched from its storage in a Cloud Storage Bucket. The supplier sent data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description).

Images cannot be uploaded here since the only way to access them was through Virtual Machines hosted by Google Servers. However, an example of the description of images can be found below:

*Mango* \
*300 lbs* \
*Mango contains higher levels of vitamin C than ordinary fruits. Eating mango can also reduce cholesterol and triglycerides, and help prevent cardiovascular disease. Due to its high level of vitamins, regular consumption of mango play an important role in improving body function and moisturizing the skin.*

The first line contains the name of the fruit followed by the weight of the fruit and finally the description of the fruit.

## Results

### Working with Supplier Images

The [first program](https://github.com/carlos-p-t/Google-IT-Automation-Course/blob/main/Final%20Project/scripts/changeimage.py) was written to work with the supplier images. The program changes the image resolution from 3000x2000 to 600x400 pixels. It also changes the image format from ".TIFF" to ".JPEG". After executing the program, we can successfully see in the below image that the images were changed as required.

<p align="center">
  <img src="https://github.com/carlos-p-t/Google-IT-Automation-Course/blob/main/Final%20Project/images/imagechange.jpg" alt="Description of the image" />
</p>
<p align="center">
  <em>Console result showing the size and type of the reformatted images.</em>
</p>

### Uploading Images to Web Server

The aim of the [second program](https://github.com/carlos-p-t/Google-IT-Automation-Course/blob/main/Final%20Project/scripts/supplier_image_upload.py) is to upload the reformatted images to the web server. The program successfully achieves this, and the results can be observed below.

<div align="center">
  <table>
    <tr>
      <td align="center">
        <img src="https://github.com/carlos-p-t/Google-IT-Automation-Course/blob/main/Final%20Project/images/index_before.jpg" alt="Before" width="500">
        <br>
      </td>
      <td align="center">
        <img src="https://github.com/carlos-p-t/Google-IT-Automation-Course/blob/main/Final%20Project/images/index_after.jpg" alt="After" width="500">
        <br>
      </td>
    </tr>
  </table>
</div>
<p align="center">
  <em>The index of images before (left) and after (right) executing the program.</em>
</p>

### Uploading the Descriptions

Following the images description format, [the program](https://github.com/carlos-p-t/Google-IT-Automation-Course/blob/main/Final%20Project/scripts/run.py) separates the information into 4 categories: *"name", "weight", "description", and "image_name"*. Then, the information is converted into JSON object, similar to the one shown below:

*{"name": "Watermelon", "weight": 500, "description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of water, which is good for relieving the symptoms of acute fever immediately. The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower blood pressure.", "image_name": "010.jpeg"}*

After executing the program, the server displays the images and their descriptions.  Below, there are two images which show the before and the after executing this program.

<p align="center">
  <img src="https://github.com/carlos-p-t/Google-IT-Automation-Course/blob/main/Final%20Project/images/server_before.jpg" alt="Description of the image" />
</p>
<p align="center">
  <em>The main page in the server did not have any images or descriptions before.</em>
</p>

<p align="center">
  <img src="https://github.com/carlos-p-t/Google-IT-Automation-Course/blob/main/Final%20Project/images/sever_after.jpg" alt="Description of the image" />
</p>
<p align="center">
  <em>After executing the program, descriptions were uploaded and now they are displayed in the main page of the server.</em>
</p>

### Generating a PDF report and send it through email

Now that the images and descriptions were uploaded, the supplier needs to be notified about our work. For that, a PDF file will be sent to the supplier, indicating that the data was correctly processed.

First, a script to [generate the PDF report](https://github.com/carlos-p-t/Google-IT-Automation-Course/blob/main/Final%20Project/scripts/reports.py) itself was written by using the *reportlab* library. Next, a program to [send reports](https://github.com/carlos-p-t/Google-IT-Automation-Course/blob/main/Final%20Project/scripts/emails.py) is created. The main function of this program requires 5 arguments: *sender, recipient, email subject, email body, and the path of the report (attachment)*.

Lastly, a [last script](https://github.com/carlos-p-t/Google-IT-Automation-Course/blob/main/Final%20Project/scripts/report_email.py) was written where data is processed, and the main functions of the previous programs are called to generate the PDF report and send it by email. The following images show the online fruit store email system inbox, where it is possible to see that an email with an attachment was received, and the report as an attachment. The report can be displayed with more details [here](https://github.com/carlos-p-t/Google-IT-Automation-Course/blob/main/Final%20Project/report.pdf).

<p align="center">
  <img src="https://github.com/carlos-p-t/Google-IT-Automation-Course/blob/main/Final%20Project/images/inbox.jpg" alt="Description of the image" />
</p>
<p align="center">
  <em>Fruit Store email system's inbox. It shows the email received with the update and an attached file (report).</em>
</p>

<p align="center">
  <img src="https://github.com/carlos-p-t/Google-IT-Automation-Course/blob/main/Final%20Project/images/report.jpg" alt="Description of the image" />
</p>
<p align="center">
  <em>A preview of the report.</em>
</p>


### Health Check

The last part of the project consisted on creating a program that runs in the background monitoring some of the system statistics: CPU usage, disk space, available memory and name resolution. If a problem is detected, the program should send a notification by email with details of the problem.

The possible problems that the program can alert about are:

- Error if CPU usage is over 80%
- Error if available disk space is lower than 20%
- Error if available memory is less than 100MB
- Error if the hostname "localhost" cannot be resolved to "127.0.0.1"

[The program](https://github.com/carlos-p-t/Google-IT-Automation-Course/blob/main/Final%20Project/scripts/health_check.py) was written considering the above. Since the program will be running in the backrground, it will be executed every 60 seconds. Once an error is detected, an email will be sent as the image shown below:

<p align="center">
  <img src="https://github.com/carlos-p-t/Google-IT-Automation-Course/blob/main/Final%20Project/images/errors.jpg" alt="Description of the image" />
</p>
<p align="center">
  <em>The inbox also displaying error messages received after the program detects problems within the system's computer.</em>
</p>
