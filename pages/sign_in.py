import streamlit as st
from menu import unauthenticated_menu

def sign_in_page():
    unauthenticated_menu()

    st.title("AI Student Assistant - Sign-in Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if not username or not password:
            st.error("Please enter both username and password.")
        else:

            st.success("Login successful!")
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.session_state['current_page'] = "main"

    if st.button("Forgot Password?"):
        st.session_state['current_page'] = "reset_password"

if __name__ == "__main__":
    sign_in_page()