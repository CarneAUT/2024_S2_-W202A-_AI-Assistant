import streamlit as st
from functions.theme import *
from menu import authenticated_menu


def profile():
    # Sidebar for logged in users
    authenticated_menu()

    st.title(":bust_in_silhouette:Profile Settings Menu")
    selected_option = st.selectbox("Select an option", ["Overview", "Account", "Settings"])

    if st.button("Log out"):
        st.switch_page("pages/sign_in.py")


    # Theme Change
    btn_face = ms.themes["light"]["button_face"] if ms.themes["current_theme"] == "light" else ms.themes["dark"]["button_face"]
    st.button(btn_face, on_click = ChangeTheme)
    # Constant Refresh To Check The Current Theme Against New Theme
    if not ms.themes["refreshed"]:
        ms.themes["refreshed"] = True
        st.rerun()


if __name__ == "__main__":
    profile()