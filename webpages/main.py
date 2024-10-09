import streamlit as st



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



# Dark/Light Mode
ms = st.session_state
if "themes" not in ms:
    ms.themes = {"current_theme": "dark",
                 "refreshed": True,

                 "light": {"theme.base": "dark",
                           "theme.backgroundColor": "black", # Background Colour, Primary Colour
                           "theme.primaryColor": "#ebab66", # Button Outline colour
                           "theme.secondaryBackgroundColor": "#ebab66", # Navbar/Button Backgrounds, Secondary Colour
                           "theme.textColor": "white", # Text Colour
                           "button_face": "Dark Mode"}, # Text on Button

                 "dark": {"theme.base": "light",
                          "theme.backgroundColor": "white", # Background Colour, Primary Colour
                          "theme.primaryColor": "#66e9eb", # Button Outline Colour
                          "theme.secondaryBackgroundColor": "#66e9eb", # Navbar/Button Backgrounds, Secondary Colour
                          "theme.textColor": "#0a1464", # Text Colour
                          "button_face": "Light Mode"}, # Text on Button
                 }

# ChangeTheme Function For Other Pages
def ChangeTheme():
    previous_theme = ms.themes["current_theme"]
    tdict = ms.themes["light"] if ms.themes["current_theme"] == "light" else ms.themes["dark"]
    for vkey, vval in tdict.items():
        if vkey.startswith("theme"): st._config.set_option(vkey, vval)

    ms.themes["refreshed"] = False
    if previous_theme == "dark":
        ms.themes["current_theme"] = "light"
    elif previous_theme == "light":
        ms.themes["current_theme"] = "dark"


btn_face = ms.themes["light"]["button_face"] if ms.themes["current_theme"] == "light" else ms.themes["dark"][
    "button_face"]
st.button(btn_face, on_click=ChangeTheme)

if ms.themes["refreshed"] == False:
    ms.themes["refreshed"] = True
    st.rerun()