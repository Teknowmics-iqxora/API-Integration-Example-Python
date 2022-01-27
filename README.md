# API-Integration-Example-Python
 This is simple python script which introduce the smartdocs api such as user login, fileUpload, formGet and formSubmit to smartdocs application.
 
 Install the required libraries in **requirements.txt**.

 All the api urls are provided in **"constants.py"** file.
 
 All other settings are provided in **"config.py"** file.
 
 Run file **"main.py** to start" .
 
 ## Steps in the script file:
 
 1. Login to smartdocs using login api with credentials.

 2. After succesful login use fileUpload api for uploading files to application. This step is required only if the form contains file fields.

 3. Successful upload of files will return fileId and fileName.

 4. To access the application formdata use formGet api.

 5. Filer the neccesary fields from obtained json and save it as "sample.json".

 6. Create a sample data for uploading to formfields.

 7. Insert the sample data and fileId, fileName  to "sample.json".

 8. Use formSubmit api to submit the form to smartdocs application.
 
 **Verify the data by logging in to the smartdocs application**
 
 ## IQXORA application for Python API integration
 
 An application is created in IQXORA for testing API integration. This application is a simple address change request. There are five form fields. The model of the application is given below.

![Model](/images/model.png)

On clicking **Address Change** tab on the left the form fields of the application will appear on the right.

![forms](/images/form.PNG)
 
 There are five form fields. We use formGet api on python to retrieve form field variables of this form and insert values to form json along with file information and call formSubmit api to complete the form submission. The list view of the submitted form data is given below.
 
![List](/images/List.PNG)
 
 Documents will appear on the **documents** tab on list view.
 
![documents](/images/documents.PNG)

## How to get variable id for form fields

To get the variable id of a particular form field Open Studio, Open Form Design. Then in the FormFields tab variable id is available against each form fields.

![variableid](/images/form_variable.png)

## How to get variable id for form actions

To get the action id of a particular form action Open Studio, Open Screens / List Design. Then in the Actions tab variable id is available against each actions.

![actionid](/images/action_variable.png)

To get formId and formName of an application Open Studio, Open Form Design . Then in Info formName and formId will be listed

![formid](/images/formid.png)
