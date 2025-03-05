from Utilities.MakeRequests import make_request
import requests
import streamlit as st
import pandas as pd 
class Diagnoses():
    def __init__(self):
        pass


    def make_preiction(self,patient_number,image):
        url = "http://127.0.0.1:8080/cases/new_case"
        
        # Prepare data for request
        data = {"patient_number": str(patient_number)}
        files = {"file": (image.name, image, image.type)}

        
        headers = {
            "Authorization": f"Bearer { st.session_state.jwt_token }",

            "accept": "application/json"
        }
        
        response = requests.post(url, headers=headers, files=files, data=data)
        print(response.json())
       
        # Checking response
        if response.status_code == 201:
           return  response.json()["case"]["diagnosis"]  # Assuming the response is JSON
        else:
            return None
        
    def get_cases(self):
        
        # response = make_request(request_type="get",
        #                         enpoint="/cases/get_cases",
        #                         data=None
        #                         )
        # print(response.json())
        # if response.status_code == 201:
        #     return response.json()["cases"]
        # else:
        #     return None

        url = "http://127.0.0.1:8080/cases/get_cases"

        
        headers = {
            "Authorization": f"Bearer { st.session_state.jwt_token }",

            "accept": "application/json"
        }
        
        response = requests.get(url, headers=headers, data=None)
       
        # Checking response
        if response.status_code == 200:
            print(response.json()["cases"][-1])
            data =  pd.DataFrame(response.json()["cases"],) # Assuming the response is JSON
            return data

        else:
            return None
        

    def get_case(self,case_id,image_id):
        url_case = "http://127.0.0.1:8080/cases/cases/{case_id}"
        url_image = "http://127.0.01:8080/cases/images/{image_id}"

        


