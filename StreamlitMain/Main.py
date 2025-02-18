import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
from StreamlitMain.AddPatient import add_new_patient_pop
from Utilise.Patient import Patient
from Utilise.Diagnoses import Diagnoses

patient_class = Patient()
diagnoses_class = Diagnoses()

# Initialize session state
if "patient_info" not in st.session_state:
    st.session_state.patient_info = None
if "uploaded_image" not in st.session_state:
    st.session_state.uploaded_image = None
if "diagnosis_result" not in st.session_state:
    st.session_state.diagnosis_result = None

# Title
st.title("🩺 Patient Skin Cancer Diagnosis System")

# Layout for patient ID input and search button
col1, col2 = st.columns([4, 1])
with col1:
    patient_id = st.text_input("Patient ID", placeholder="Enter Patient ID", label_visibility="collapsed")
with col2:
    search_button = st.button("Search")

# Search for the patient
if search_button:
    patient_info = patient_class.get_patient_info(patient_id)


    if patient_info:
        st.session_state.patient_info = patient_info # Store patient data
        st.session_state.uploaded_image = None
        st.session_state.diagnosis_result = None
        st.rerun()

        st.success(f"✅ Patient Found: {st.session_state.patient_info['name']}")
    else:
        st.session_state.uploaded_image = None
        st.session_state.diagnosis_result = None
        st.session_state.patient_info = None
        add_new_patient_pop(patient_id)

if st.session_state.patient_info:
    patient_info = st.session_state.patient_info

    # Display patient details in two columns
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Patient Number:** {patient_info['patient_number']}")
        st.write(f"**Name:** {patient_info['name']}")
        st.write(f"**Date of Birth:** {patient_info['date_of_birth']}")

    with col2:
        st.write(f"**Gender:** {patient_info['gender']}")
        st.write(f"**Country:** {patient_info['country']}")
        st.write(f"**Occupation:** {patient_info['occupation']}")
        st.write(f"**Ethnicity:** {patient_info['ethnicity']}")

    # Display medical notes separately
    st.write("### 📝 Medical Notes")
    if patient_info["notes"]:
        for note in patient_info["notes"]:
            st.write(f"- {note}")
    else:
         st.write(f"-")


    # Image input selection using st.pills()
    st.write("### 📷 Select Image Input Method")
    option = st.pills("Choose an option:", ["Upload Image", "Take Picture"],default = "Upload Image")

    # Initialize image input
    uploaded_file, camera_file = None, None

    if option == "Upload Image":
        uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "png", "jpeg"],accept_multiple_files = False)
        if uploaded_file:
            st.session_state.uploaded_image = uploaded_file

    elif option == "Take Picture":
        camera_file = st.camera_input("📸 Take a picture")
        if camera_file:
            st.session_state.uploaded_image = camera_file

    if st.session_state.uploaded_image:
        # Diagnosis button
        if st.button("🔬 Diagnose Skin Condition"):
            #  AI model result
            st.session_state.diagnosis_result = diagnoses_class.make_preiction(
                patient_id,
                st.session_state.uploaded_image


            )

        # Display diagnosis results if available
        if st.session_state.diagnosis_result:
            st.write("### 🏥 Diagnosis Result")

            # Convert diagnosis results into a DataFrame for Seaborn
            df = pd.DataFrame(st.session_state.diagnosis_result.items(), columns=["Condition", "Probability"])

            # Define colors for the chart
            colors = ["#4CAF50", "#FF5733"]  # Green for Benign, Red for Malignant

            # Create a stylish modern Pie Chart using Seaborn & Matplotlib
            plt.figure(figsize=(5, 5))
            sns.set_style("whitegrid")

            # Plot Pie Chart
            wedges, texts, autotexts = plt.pie(
                df["Probability"],
                labels=df["Condition"],
                autopct='%1.1f%%',
                colors=colors,
                startangle=140,
                wedgeprops={"edgecolor": "white", "linewidth": 2, "antialiased": True},
                textprops={"fontsize": 12, "weight": "bold"}
            )

            # Set title
            plt.title("Skin Cancer Diagnosis", fontsize=14, weight="bold")

            # Display the pie chart
            plt.show()


            st.pyplot(plt)
            # Layout for patient ID input and search button
            col1, col2 ,col3= st.columns([5 ,1, 1])
            
            with col2:

                if st.button("Clear"):
                    st.session_state.uploaded_image = None
                    st.session_state.patient_info = None
                    st.session_state.diagnosis_result = None
                    
                    st.rerun()
            with col3:
                if st.button("Print"):
                    pass


