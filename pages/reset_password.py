import streamlit as st
from firebasesdkadmin import reset_password_email
from menu import unauthenticated_menu

def reset_password_page():
    unauthenticated_menu()

    st.title("AI Student Assistant - Reset Password Page")

    email = st.text_input("Enter your email to reset your password")

    if st.button("Submit"):
        if not email:
            st.error("Please enter your email.")
        else:
            if reset_password_email(email):
                st.success("Password reset email sent! Check your inbox.")
            else:
                st.error("Failed to send reset email. Try again.")

if __name__ == "__main__":
    reset_password_page()