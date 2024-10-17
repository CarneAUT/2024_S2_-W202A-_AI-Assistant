import streamlit as st
from firebasesdkadmin import log_in

st.title("AI Student Assistant - Sign-in Page")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if not username or not password:
        st.error("Please enter both username and password.")
    else:
        if log_in(username, password):
            st.success("Login successful!")
        else:
            st.error("Incorrect username or password.")