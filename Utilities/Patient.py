
from Utilities.MakeRequests import make_request


class Patient():
    def __init__(self):
        pass

    

    def get_patient_info(self,patient_number:str)-> dict:

        response = make_request('get','/users/patients',patient_number)

       
        # Checking response
        if response.status_code == 200:
           return  response.json()["patient"]  # Assuming the response is JSON
        else:
            return None
        
    
    def add_new_patinet(
            self,
            info:dict,
           
                            ) -> dict:
        
        
        response =make_request("post","/users/register-patient",info)


        # Checking response
        if response.status_code == 200:
           return  response.json()  # Assuming the response is JSON
        else:
            return None

        


        

            