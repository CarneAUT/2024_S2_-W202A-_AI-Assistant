import streamlit as st
from generate_text import *
from menu import authenticated_menu
from prompts import *
from read_file import *
from functions.theme import *


def study_plan():
    # Sidebar for logged in users
    authenticated_menu()

    # Upload files
    st.header("Create Study Plan")

    # Create an uploader for files to be uploaded to.
    uploader = st.file_uploader(
        "Upload course content to generate a study plan",
        type=["pdf", "docx"]  # File types allowed
    )

    if st.button("Generate"):
        if uploader is not None:
            # When a file is uploaded.
            course_content = extract_text(uploader)

            st.write(generate_text(course_content, study_plan))

    # Theme Change
    btn_face = ms.themes["light"]["button_face"] if ms.themes["current_theme"] == "light" else ms.themes["dark"][
        "button_face"]
    st.button(btn_face, on_click=ChangeTheme)
    # Constant Refresh To Check The Current Theme Against New Theme
    if not ms.themes["refreshed"]:
        ms.themes["refreshed"] = True
        st.rerun()


if __name__ == "__main__":
    study_plan()
