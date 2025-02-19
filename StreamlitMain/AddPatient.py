import streamlit as st
import pycountry
import datetime
from Utilities.Patient import Patient

patient_class = Patient()

# Define your own date range:
min_date = datetime.date(1960, 1, 1)
max_date = datetime.date(2030, 12, 31)


# Initialize session state
if "patient_info" not in st.session_state:
    st.session_state.patient_info = None

if "uploaded_image" not in st.session_state:
    st.session_state.uploaded_image = None
if "diagnosis_result" not in st.session_state:
    st.session_state.diagnosis_result = None



# Define the dialog function using the decorator.
@st.dialog("Patient Registration", width="large")
def add_new_patient_pop(patient_number:str):
    with st.form("reg_form"):
        st.header("Patient Registration Form")
        
        # patinet id number 
        patient_number = patient_number
        # Input for patient's name
        name = st.text_input("Name")
        
        # Date input for patient's date of birth
        date_of_birth = st.date_input("Date of Birth",value=datetime.date.today(),min_value=min_date,max_value=max_date)
        
        # Use pycountry to generate a list of countries
        countries = sorted([country.name for country in pycountry.countries])
        country = st.selectbox("Country", countries)
        
        # Gender input as a radio button (ensuring single selection)
        gender = st.radio("Gender", options=["Male", "Female"])
        
        # Input for occupation and ethnicity
        occupation = st.text_input("Occupation")
        ethnicity = st.text_input("Ethnicity")
        
        # Submit button for the form
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            # TODO We need to make Request to api to create the new patient
            info = {
        "patient_number": str(patient_number),
        "name": name,
        "date_of_birth":  str(date_of_birth),
        "gender": gender,
        "country":country,
        "occupation": occupation,
        "ethnicity": ethnicity,
        "notes": [],
    }
            
            patient_class.add_new_patinet(info)
            
            st.session_state.patient_info = info
            # add the patient to the database 
            
            st.success("Patient information submitted!")
            st.rerun()
            

            

"""# Check if the patient ID exists in session state; if not, show the dialog.
if "patient_id" not in st.session_state:
    add_new_patient()"""