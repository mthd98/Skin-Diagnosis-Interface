import streamlit as st 
from Utilities.Diagnoses import Diagnoses

st.title("Skin Cancer Diagnosis History")


diagnoses_class = Diagnoses()


# show the cesses 


diagnosis_history_data = diagnoses_class.get_cases()
columns_to_show  = ["patient_id","diagnosis","created_at","notes"]
diagnosis_history_df = st.dataframe(data = diagnosis_history_data[columns_to_show],use_container_width=True,
                                    width=1500,height=600)


