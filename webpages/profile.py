import streamlit as st
from functions.theme import *

st.title("👤Profile Settings Menu")
selected_option = st.selectbox("Select an option", ["Overview", "Account", "Settings"])

# Theme Change
btn_face = ms.themes["light"]["button_face"] if ms.themes["current_theme"] == "light" else ms.themes["dark"]["button_face"]
st.button(btn_face, on_click = ChangeTheme)
# Constant Refresh To Check The Current Theme Against New Theme
if not ms.themes["refreshed"]:
    ms.themes["refreshed"] = True
    st.rerun()