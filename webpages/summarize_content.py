import streamlit as st
from pypdf import PdfReader

from webpages import main
from generate_text import *
from prompts import *

# Upload files
st.header("Upload Files For The AI")
st.write("You can upload either a pdf file below for the AI to look through and summarise for your convenience. It cannot read words on images such as png or jpeg.")

# Create an uploader for files to be uploaded to.
uploader = st.file_uploader(
    "", accept_multiple_files=False, help="Only pdf files can be accepted.",
    type=["pdf"]  # File types allowed
)

# Initialized text variable
text = ""

# When a file is uploaded.
if uploader is not None:
    # Check if the file is a PDF
    if uploader.type == "application/pdf":
        reader = PdfReader(uploader)
        # Page reader reads pages and puts the text into the text variable
        for page in reader.pages:
            text += page.extract_text() + "\n"

# Writes the generated text which uses the text variable
st.write(generate_text(text, summarize_content))

# Light/Dark Mode
ms = st.session_state
btn_face = ms.themes["light"]["button_face"] if ms.themes["current_theme"] == "light" else ms.themes["dark"][
    "button_face"]
st.button(btn_face, on_click=main.ChangeTheme)

if ms.themes["refreshed"] == False:
    ms.themes["refreshed"] = True
    st.rerun()