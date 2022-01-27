from unittest import expectedFailure
import requests
import json
import os
from utils import login,file_upload,form_get,form_submit,insert_data_to_form
if __name__=="__main__":
    file = open('config.json')
    config = json.load(file)    
    user=config["user"]
    password=config["password"]
    session = requests.Session()
    data =['test name', 30, 'Trivandrum, Kerala', 'Cochin, Kerala']     #initializing data for form submission
    form_get_status=True
    try:
        login_status=login(session,user,password)
        if login_status=="Success":
            file_path='input/utilityBill.png'                            #file path to upload files
            file_id,file_name=file_upload(session,config,file_path)
            if not os.path.exists("sample.json"):
                form_get_status=form_get(session,config)
            if form_get_status:
                with open('sample.json') as f:
                    form_json = json.load(f)                
                    form_data = insert_data_to_form(config,form_json, data,file_id,file_name)            
                    formdata = json.dumps(form_data)
                    form_submit_status=form_submit(session, config,formdata)
                    if form_submit_status:
                        print('Form Submission completed')
    except Exception:
        print("Form submission Failure!!")