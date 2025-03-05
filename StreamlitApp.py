import streamlit as st

from pathlib import Path
from Utilities.MakeRequests import make_request



if "jwt_token" not in st.session_state:
    st.session_state.jwt_token = None



base_path = str(Path(__file__).parent)



if "logged_in" not in st.session_state:
    st.session_state.logged_in = False



def login():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Log in"):
        login_data = {
            "email": username,
            "password": password
        }

        jwt_token = make_request('post', "/users/login", login_data)
        
        if jwt_token.status_code == 200:
            st.session_state.jwt_token = jwt_token.json().get("access_token")
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.session_state.logged_in = False
            
            error_message = jwt_token.json().get("detail", "Login failed. Please try again.")
            st.error(error_message)  # Display the error message to the user

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.session_state.uploaded_image = None
        st.session_state.patient_info = None
        st.session_state.diagnosis_result = None
        st.session_state.jwt_token = None

        st.rerun()




login_page = st.Page(login, title="Log in", icon=":material/login:")


logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

main = st.Page(
    base_path+"/streamlitMain/Main.py", title="Main", icon=":material/dashboard:"
)


cases = st.Page(
    base_path+"/streamlitMain/Cases.py", title="Cases", icon=":material/dashboard:"

)


if st.session_state.logged_in:
    pg = st.navigation(
        {

            "Dashboard": [main,cases],
            "Account": [logout_page],
           
         
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()
