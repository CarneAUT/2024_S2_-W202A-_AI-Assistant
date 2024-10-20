import streamlit as st
from pages.sign_in import sign_in_page

if 'current_page' not in st.session_state:
    st.session_state['current_page'] = "sign_in"

if st.session_state['current_page'] == "sign_in":
    sign_in_page()