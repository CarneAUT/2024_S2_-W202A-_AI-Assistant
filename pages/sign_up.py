import streamlit as st
from firebasesdkadmin import register_user
from menu import unauthenticated_menu


def sign_up():
    # Sidebar for sign-up sign-in
    unauthenticated_menu()

    st.title("AI Student Assistant - Sign-up Page")

    st.write("Create an AI student assistant account.")

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Sign-up"):
        if not username or not email or not password:
            st.error("Please fill in all fields.")
        else:
            result = register_user(username, password, email)
            if result == "User registered successfully":
                st.success(result)
                st.info("You can now log in with your new account.")
            else:
                st.error(result)


if __name__ == "__main__":
    sign_up()
