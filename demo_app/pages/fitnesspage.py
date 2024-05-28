import base64
import os
import numpy as np
import streamlit as st
import components.fitness_sidebar
import components.sidebar
from PIL import Image

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .main {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    background-attachment: local;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


if __name__ == "__main__":

    st.set_page_config(
        page_title="EthnoFit",
        page_icon=":biceps:",
        layout="wide",
        initial_sidebar_state="expanded", )
    st.header("EthnoFit")
    components.fitness_sidebar.fitness_sidebar()

    if not st.session_state.get("open_api_key_configured"):
        st.error("Please configure your API Keys!")
    else:
        #st.markdown("Welcome to the fitness page!!!")

        if os.path.isfile("./demo_app/images/uploaded_file.png"): 
            image = (Image.open("./demo_app/images/uploaded_file.png"))
            #st.image(image, caption='Current Image')
            set_background('./demo_app/images/uploaded_file.png')
        
        timeline = st.slider("See how you look in future (in months)", min_value=0, max_value=12, value=0, step=3)
        if timeline == 3:
            image = (Image.open("./demo_app/mexicanmanbefore.png"))
            #st.image(image)
            set_background("./demo_app/mexicanmanbefore.png")
        if timeline == 6:
            image = (Image.open("./demo_app/jane-doe.png"))
            #st.image(image)
            set_background("./demo_app/jane-doe.png")
        if timeline == 9:
            image = (Image.open("./demo_app/johndoe.png"))
            #st.image(image)
            set_background("./demo_app/johndoe.png")
        if timeline == 12:
            image = (Image.open("./demo_app/human_back.jpg"))
            #st.image(image)
            set_background("./demo_app/human_back.jpg")
