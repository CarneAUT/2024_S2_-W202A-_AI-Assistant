import streamlit as st
from functions.theme import *


st.title("AI Student Assistant 💬")
st.write("The AI Student Assistant tool aims to leverage AI technologies, specifically a large language model,"
         " to revolutionize the way students interact with course content. The tool's primary functions"
         " ary functions include summarizing course content, creating mock quizzes to aid with learning, "
         "offering concise and accessible insights.")


st.write("Features")
st.write("answer questions about student features, issues, and more")
st.expander("#### Updates!")
selected_option = st.selectbox("", ["What's coming next?", "Updates"])

if selected_option == "Updates":
    with st.expander("Updates"):
        st.write(""" updated site with summarized course content, mock quiz, study plans and profile """)
    with st.expander("What's coming next?"):
        st.write(""" alot more incoming """)



st.write("#### Get started!")



# Theme Change
btn_face = ms.themes["light"]["button_face"] if ms.themes["current_theme"] == "light" else ms.themes["dark"]["button_face"]
st.button(btn_face, on_click = ChangeTheme)
# Constant Refresh To Check The Current Theme Against New Theme
if not ms.themes["refreshed"]:
    ms.themes["refreshed"] = True
    st.rerun()