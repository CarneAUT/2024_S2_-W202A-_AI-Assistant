import streamlit as st

# Upload files
import streamlit as st

# Upload files
st.header("This is the Upload File Page")
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras lacinia mi eu arcu egestas posuere. Vivamus at nibh placerat, aliquet urna in, commodo velit. Nulla facilisi. Mauris a maximus diam. Maecenas elementum sed felis nec facilisis. Donec nibh orci, egestas eu dui a, tempor consequat magna.")

uploader = st.file_uploader(
    "Upload Image", accept_multiple_files=False, help="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras lacinia mi eu arcu egestas posuere. Vivamus at nibh placerat, aliquet urna in, commodo velit. Nulla facilisi. Mauris a maximus diam. Maecenas elementum sed felis nec facilisis. Donec nibh orci, egestas eu dui a, tempor consequat magna.",
    type=["png", "jpeg"] #File types allowed
)
if uploader is not None:
    uploaded_image = uploader.read()
    st.image(uploaded_image)