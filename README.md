# API-Integration-Example-Python
 This is simple python script which introduce the smartdocs api such as user login, fileUpload, formGet and formSubmit to smartdocs application.
 
 Install the required libraries in **requirements.txt**.

 All the api urls are provided in **"constants.py"** file.
 
 All other settings are provided in **"config.py"** file.
 
 Run file **"main.py** to start" .
 
 ## Steps in the script file:
 
 1.Login to smartdocs using login api with credentials.

 2.After succesful login use fileUpload api for uploading files to application.

 3.successful upload of files will return fileId and fileName.

 4.To access the application formdata use formGet api.

 5.Filer the neccesary fields from obtained json and save it as "sample.json".

 6.Create a sample data for uploading to formfields.

 7.Insert the sample data and fileId, fileName  to "sample.json".

 8.Use formSubmit api to submit the form to smartdocs application.
 
 **Verify the data by logging in to the smartdocs application**
