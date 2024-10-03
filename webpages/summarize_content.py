import streamlit as st
from generate_text import *
from prompts import *
from read_file import *

# Upload files
st.header("Summarize Course Content")

# Create an uploader for files to be uploaded to.
uploader = st.file_uploader(
    "Upload course content to generate a summary of the course content",
    type=["pdf", "docx"]  # File types allowed
)

if st.button("Generate"):
    if uploader is not None:
        # When a file is uploaded.
        course_content = extract_text(uploader)

        st.write(generate_text(course_content, summarize_content))