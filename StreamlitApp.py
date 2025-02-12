import streamlit as st

from pathlib import Path




if "JWT" not in st.session_state:
    st.session_state.jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjNhZDRmZmU2LTNiZmEtNGU1Yy05NWNkLTM4MzFmYTE2NjVmMCIsImVtYWlsIjoidGVzdDAwMUB0ZXN0LmNvbSIsImV4cCI6MTczOTM4NTE4MX0.ZuxaaYbYu15ycoFa85DI2XaWZDcwVTwOfw3tYmnY1tY"



base_path = str(Path(__file__).parent)



if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Log in"):
       
        st.session_state.logged_in = True
        st.rerun()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()




login_page = st.Page(login, title="Log in", icon=":material/login:")


logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

main = st.Page(
    base_path+"/streamlitMain/Main.py", title="Main", icon=":material/dashboard:"
)


cases = st.Page(
    base_path+"/streamlitMain/Cases.py", title="Cases", icon=":material/dashboard:"

)


settings = st.Page(
    base_path+"/streamlitMain/Settings.py", title="Settings", icon=":material/settings:"
)


if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Dashboard": [main,cases],
            "Manage":[settings]
         
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()
