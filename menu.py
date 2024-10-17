import streamlit as st


# Show a navigation menu for authenticated users
def authenticated_menu():
    st.sidebar.page_link("pages/main.py", label="Main")
    st.sidebar.page_link("pages/mock_quiz.py", label="Mock Quiz")
    st.sidebar.page_link("pages/study_plan.py", label="Study Plan")
    st.sidebar.page_link("pages/summarize_content.py", label="Summarize Content")
    st.sidebar.page_link("pages/profile.py", label="Profile")


# Show a navigation menu for unauthenticated users
def unauthenticated_menu():
    st.sidebar.page_link("pages/sign_in.py", label="Log in")
    st.sidebar.page_link("pages/sign_up.py", label="Sign up")
