import streamlit as st

main = st.Page("main.py", title="Main")
summarize_content = st.Page("webpages/summarize_content.py", title="Summarize Course Content", icon=":material/add_circle:")
mock_quiz = st.Page("webpages/mock_quiz.py", title="Mock Quizzes")
study_plan = st.Page("webpages/study_plan.py", title="Study Plans")
profile = st.Page("webpages/profile.py", title="Profile")

pg = st.navigation([main, summarize_content, mock_quiz, study_plan, profile])
pg.run()