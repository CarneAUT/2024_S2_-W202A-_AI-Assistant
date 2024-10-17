import streamlit as st
from generate_text import *
from menu import authenticated_menu
from prompts import *
from read_file import *
from functions.theme import *


def chat():
    # Sidebar for logged in users
    authenticated_menu()

    # Upload files
    st.header("Chat")

    # Create an uploader for files to be uploaded to.
    uploader = st.file_uploader(
        "Upload course content",
        type=["pdf", "docx"]  # File types allowed
    )

    if st.button("Upload"):
        if uploader is not None:
            # When a file is uploaded.
            course_content = extract_text(uploader)
            st.session_state.rag_chain = rag_pipeline(course_content)
        else:
            st.error("Please upload a file first.")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Ask a question about your course content"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response using RAG
        if st.session_state.rag_chain is not None:
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = generate_chat_response(st.session_state.rag_chain, prompt)
                    st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
        else:
            st.error("Please upload and process course content before asking questions.")

    # Theme Change
    btn_face = ms.themes["light"]["button_face"] if ms.themes["current_theme"] == "light" else ms.themes["dark"][
        "button_face"]
    st.button(btn_face, on_click=ChangeTheme)
    # Constant Refresh To Check The Current Theme Against New Theme
    if not ms.themes["refreshed"]:
        ms.themes["refreshed"] = True
        st.rerun()


if __name__ == "__main__":
    chat()
