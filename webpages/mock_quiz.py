import streamlit as st
from pypdf import PdfReader
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

text = ""

# When a file is uploaded.
if uploader is not None:
    # Check if the file is a PDF
    if uploader.type == "application/pdf":
        reader = PdfReader(uploader)

        for page in reader.pages:
            text += page.extract_text() + "\n"

st.write(generate_text(text, mock_quiz))