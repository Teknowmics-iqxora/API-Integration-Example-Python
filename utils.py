

import json
def insert_data_to_form(config,form,data,fileid,filename):
    for primekey, value in form.items():
        form_data = form[primekey]       
        for idx, items in enumerate(form_data):
            for key in items.keys():
                if items[key] == config["name_key"]:
                    items['value'] = data[0]
                if items[key] == config["age_key"]:
                    items['value'] = data[1]
                if items[key] == config["current_address_key"]:
                    items['value'] = data[2]
                if items[key] == config["new_address_key"]:
                    items['value'] = data[3]
                if items[key] == config["proof_key"]:
                    tmp = items
                    for tmpkey in tmp.keys():
                        if tmpkey == 'fileList':
                            if fileid and filename:
                                tmp['fileList'][0]['fileId'] =fileid
                                tmp['fileList'][0]['fileName'] = filename
                            else:
                                tmp['fileList'] = []
                    items = tmp
            form_data[idx] = items
    form[primekey] = form_data
    return form

def form_get(session,config):
    from constants import formget_url
    status=False
    params={"actionId":config["actionId"],"actionType":config["actionType"],"formId":config["formId"],
    "formName":config["formName"]}
    try:
        response=session.get(formget_url,params=params)       
        json_data = json.loads(response.text)
        data=json.loads(json_data['Items'][0]["details"])        
        data=data["components"]    
        filtered_json=[]
        for elems in data:
            if elems["type"]=="FILE":                
                res = {key: elems[key] for key in elems.keys()
                                    & {'label', 'type','key',"modelFieldKey","required"}}
                res["fileList"]= [{
                    "fileId": "",
                    "fileName": ""
                }]
            else:
                res = {key: elems[key] for key in elems.keys()
                                    & {'label', 'type','key',"modelFieldKey","minValue","maxValue","required"}}
                res["value"]=""
            filtered_json.append(res)

        # print(data3)
        final_json={"components":filtered_json}
        with open("sample.json", "w") as outfile:
            outfile.write(json.dumps(final_json,indent =2))
        status=True
    except Exception:
        return status
    return status

def form_submit(session,config,formdata):
    from constants import form_submit_url
    params = {"actionId": config["actionId"], "action": config["action"], "formName": config["formName"],
                      "formId": config["formId"],
                      "actionType": config["actionType"], "formVersion": config["formVersion"], "formData": formdata}
   
    
    status=False
    try:
        response = session.post(form_submit_url, data=params)
        response = json.loads(response.text)
        response = response["header"]["message"]
        if response=="Success":
            status=True
            return status
        else:
            return status
    except:
        return status

def file_upload(session,config,file_path):
    from constants import file_upload_url
    files = {"workflowFile": open(file_path, 'rb')}
    values = {"formTaskMapId": config["formtaskmapid"]}
    try:
        response = session.post(file_upload_url, files=files, data=values)        
        response = response.text
        response = json.loads(response)
        response = response["Items"][0]
        file_id = response['fileId']
        file_name = response['fileName']
    except Exception:
        file_id,file_name=None
    return file_id,file_name
def login(session,user,password):
    from constants import login_url 
    try:
        loginRequest = session.post(login_url, data={"loginName": user, "password": password}, verify=False)
        loginStatus = json.loads(loginRequest.text)
        loginStatus = loginStatus["header"]["message"]
        return loginStatus
    except Exception:
        return None