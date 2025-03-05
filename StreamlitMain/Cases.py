import streamlit as st
import datetime
from Utilities.Diagnoses import Diagnoses
import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt
from Utilities.Patient import Patient

patient_class = Patient()


@st.dialog("Diagnosis Result", width="large")
def show_diagnosis_popup(patient_info:dict ,diagnosis_result:dict):
    """
    Displays a modal popup with:
      1) Two-column layout for patient info
      2) A 'Medical Notes' section
      3) A bar chart showing diagnosis probabilities
    """
    patient_info = patient_class.get_patient_info(patient_info["patient_number"])
    # --- Patient Information in Two Columns ---
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

    # --- Medical Notes ---
    st.write("### 📝 Medical Notes")
    # If your data has multiple notes, adjust as needed (e.g., loop through them).
    st.write(patient_info["notes"])

    # --- Diagnosis Result (Bar Chart) ---
    st.write("### 🏥 Diagnosis Result")

    # Convert the dictionary { "Malignant": 0.8, "Benign": 0.2 } into a DataFrame
    df = pd.DataFrame(diagnosis_result.items(), columns=["Condition", "Probability"])
    df["Probability"] *= 100  # Convert to percentage

    print(df)

    # Basic color mapping
    colors = {"malignant": "#FF5733", "benign": "#4CAF50"}


    # Plot using matplotlib + seaborn
    plt.figure(figsize=(6, 4))
    sns.set_style("whitegrid")
    sns.barplot(y=df["Condition"], x=df["Probability"], palette=colors, orient='h')
    plt.xlabel("Probability (%)")
    plt.ylabel("Condition")
    plt.title("Skin Cancer Diagnosis", fontsize=14, weight="bold")

    # Add percentage labels on each bar
    for index, value in enumerate(df["Probability"]):
        plt.text(value + 1, index, f"{value:.1f}%", va='center')

    st.pyplot(plt)
   
st.title("Skin Cancer Diagnosis History")

diagnoses_class = Diagnoses()


if st.button("Refresh"):
    st.session_state.diagnosis_history_data = diagnoses_class.get_cases()
    st.rerun()
if "diagnosis_history_data" not in st.session_state:
    st.session_state.diagnosis_history_data = diagnoses_class.get_cases()
    print(st.session_state.diagnosis_history_data[-1])

columns_to_show = ["patient_number", "diagnosis", "created_at", "notes"]

# Display the dataframe with row selection enabled.
select_row = st.dataframe(
    data=st.session_state.diagnosis_history_data[columns_to_show],
    use_container_width=True,
    selection_mode="single-row",
    width=1500,
    height=600,
    on_select="rerun"
)

# When a row is selected, call the dialog function to show the popup.
if select_row["selection"]["rows"]:
    selected_index = select_row["selection"]["rows"][0]
    row_data = st.session_state.diagnosis_history_data.iloc[selected_index]
    print(
        row_data.to_dict(),
    )
    show_diagnosis_popup(
        patient_info=row_data.to_dict(),
        diagnosis_result=row_data["diagnosis"]
    )
