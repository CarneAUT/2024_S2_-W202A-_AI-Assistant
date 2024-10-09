import streamlit as st
from webpages import main

st.title("👤Profile Settings Menu")
selected_option = st.selectbox("Select an option", ["Overview", "Account", "Settings"])

# Light/Dark Mode
ms = st.session_state
btn_face = ms.themes["light"]["button_face"] if ms.themes["current_theme"] == "light" else ms.themes["dark"][
    "button_face"]
st.button(btn_face, on_click=main.ChangeTheme)

if ms.themes["refreshed"] == False:
    ms.themes["refreshed"] = True
    st.rerun()