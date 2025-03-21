import streamlit as st
import json 
from decouple import config
import requests 



def make_request(request_type,enpoint,data,file=None):
        main_url = config("SYSTEMAPI")

        url = main_url + enpoint
       

        # Headers with JWT token
        headers = {
            "Authorization": f"Bearer {st.session_state.jwt_token}",
            "Content-Type": "application/json"
        }
        if request_type == "get":
            # Sending a GET request
            response = requests.get(url+f"/{data}", headers=headers)

        elif request_type == "post":
            # Sending a GET request
            response = requests.post(url,json=data, headers=headers,files=file)
             

        
        return  response 
       
