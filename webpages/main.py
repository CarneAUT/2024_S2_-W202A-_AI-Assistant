import streamlit as st
from functions.theme import *

st.set_page_config(page_title="AI Student Assistant", page_icon=":books:", layout="wide")
st.title("Welcome to AI Student Assistant :speech_balloon:")

st.write("""
The AI Student Assistant is your personal learning companion, leveraging advanced AI technologies to 
revolutionise your educational experience.

# Features:
- :pencil: **Summarise Course Content**: Get concise summaries of your course materials.
- :bar_chart: **Create Study Plans**: Receive personalized study schedules tailored to your needs.
- :books: **Generate Mock Quizzes**: Test your knowledge with AI-generated quizzes.
- :bust_in_silhouette: **Personalised Learning**: Adapt to your unique learning style and pace.

# How It Works:
1. Upload your course materials (PDF or DOCX)
2. Choose the feature you want to use
3. Get instant AI-powered assistance!

# Get Started:
Click on any feature in the sidebar to begin your enhanced learning journey!
""")

st.subheader("Latest Updates")
with st.expander("What's New"):
    st.write("""
    - Enhanced summarisation algorithms for better content overview
    - Improved mock quiz generation with more diverse question types
    - New study plan feature for optimised learning schedules
    - Profile page for personalised settings
    """)

with st.expander("Coming Soon"):
    st.write("""
    - Integration with popular learning management systems
    - Mobile app for on-the-go learning
    - Collaborative study sessions with AI-facilitated group discussions
    - Advanced analytics to track your learning progress
    """)

btn_face = ms.themes["light"]["button_face"] if ms.themes["current_theme"] == "light" else ms.themes["dark"][
    "button_face"]
st.sidebar.button(btn_face, on_click=ChangeTheme)

if not ms.themes["refreshed"]:
    ms.themes["refreshed"] = True
    st.rerun()