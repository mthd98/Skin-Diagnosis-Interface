import streamlit as st 
from Utilities.Diagnoses import Diagnoses

st.title("Skin Cancer Diagnosis History")


diagnoses_class = Diagnoses()


# show the cesses 


diagnosis_history_data = diagnoses_class.get_cases()

diagnosis_history_df = st.dataframe(data = diagnosis_history_data

)
