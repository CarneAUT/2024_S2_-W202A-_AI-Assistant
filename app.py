import streamlit as st
from pages.sign_in import sign_in_page
from pages.main import main
from menu import unauthenticated_menu, authenticated_menu


def app():
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = "sign_in"

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if st.session_state['current_page'] == "sign_in":
        sign_in_page()
    elif st.session_state['current_page'] == "main":
        main()


if __name__ == "__main__":
    app()