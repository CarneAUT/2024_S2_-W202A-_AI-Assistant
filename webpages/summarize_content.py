import streamlit as st
from pypdf import PdfReader

# Upload files
st.header("Upload Files For The AI")
st.write("You can upload either a pdf or docx file below for the AI to look through and summarise for your convenience. It cannot read words on images such as png or jpeg.")

# Create an uploader for files to be uploaded to.
uploader = st.file_uploader(
    "", accept_multiple_files=False, help="Only pdf or docx files can be accepted.",
    type=["pdf", "docx"]  # File types allowed
)

# When a file is uploaded.
if uploader is not None:
    # Check if the file is a PDF
    if uploader.type == "application/pdf":
        reader = PdfReader(uploader)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"  # Extract text from each page
