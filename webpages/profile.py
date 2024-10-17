import streamlit as st
from functions.theme import *

# Check if user is logged in
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.warning("Please log in/register to access the content.")
    st.stop()

st.title("👤Profile Settings Menu")
selected_option = st.selectbox("Select an option", ["Overview", "Account", "Settings"])

# Theme Change
btn_face = ms.themes["light"]["button_face"] if ms.themes["current_theme"] == "light" else ms.themes["dark"]["button_face"]
st.button(btn_face, on_click = ChangeTheme)
# Constant Refresh To Check The Current Theme Against New Theme
if not ms.themes["refreshed"]:
    ms.themes["refreshed"] = True
    st.rerun()