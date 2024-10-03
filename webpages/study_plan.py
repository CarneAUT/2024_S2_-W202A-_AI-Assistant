import streamlit as st
from generate_text import *
from prompts import *
from read_file import *

# Upload files
st.header("Upload Files For The AI")
# st.write("You can upload either a pdf file below for the AI to look through and summarise for your convenience. It cannot read words on images such as png or jpeg.")

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