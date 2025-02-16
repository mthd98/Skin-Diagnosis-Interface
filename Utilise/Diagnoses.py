from Utilise.MakeRequests import make_request
import requests
import streamlit as st

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
           return  response.json()["case"]["diagnosis"]["diagnosis"][-1]  # Assuming the response is JSON
        else:
            return None

