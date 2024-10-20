import streamlit as st
from pypdf import PdfReader
import docx

def read_pdf(file):
    text = ""
    reader = PdfReader(file)

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text

def read_docx(file):
    doc = docx.Document(file)
    content = []
    for para in doc.paragraphs:
        content.append(para.text)
    return '\n'.join(content)

def extract_text(uploaded_file):
    text = ""

    if uploaded_file.type == "application/pdf":
        text = read_pdf(uploaded_file)

    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        text = read_docx(uploaded_file)

    return text

