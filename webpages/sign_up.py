import streamlit as st
from firebasesdkadmin import register_user, login_user
from functions.theme import *


st.title("AI Student Assistant Sign-up Page")

# dropdown
choice = st.selectbox("Login/Signup", ["Login", "Sign up"])
if choice == "Sign up":
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
else:
    st.write("Login to your AI student assistant account.")

    email = st.text_input("Email Address")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        result = login_user(email, password)
        if result == "Login successful":
            st.success(result)
            st.balloons()
        else:
            st.error(result)

btn_face = ms.themes["light"]["button_face"] if ms.themes["current_theme"] == "light" else ms.themes["dark"]["button_face"]
st.sidebar.button(btn_face, on_click=ChangeTheme)

if not ms.themes["refreshed"]:
    ms.themes["refreshed"] = True
    st.rerun()
