import streamlit as st

# Theme Change
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
