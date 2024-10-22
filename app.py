import streamlit as st
from pages.sign_in import sign_in_page
from pages.reset_password import reset_password_page
from pages.main import main

if 'current_page' not in st.session_state:
    st.session_state['current_page'] = "sign_in"

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if st.session_state['logged_in']:
    if st.session_state['current_page'] == "main":
        main()
else:
    if st.session_state['current_page'] == "sign_in":
        sign_in_page()
    elif st.session_state['current_page'] == "reset_password":
        reset_password_page()