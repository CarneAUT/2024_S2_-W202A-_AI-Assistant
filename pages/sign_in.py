import streamlit as st
from firebasesdkadmin import log_in
from menu import unauthenticated_menu


def sign_in_page():
    # Sidebar for sign-up sign-in
    unauthenticated_menu()

    st.title("AI Student Assistant - Sign-in Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if not username or not password:
            st.error("Please enter both username and password.")
        else:
            if log_in(username, password):
                st.success("Login successful!")
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.switch_page("pages/main.py")
            else:
                st.error("Incorrect username or password.")


if __name__ == '__main__':
    sign_in_page()
