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
    background-size: auto;
    background-repeat: no-repeat;
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
            #st.image(image, caption='Image uploaded')
            set_background('./demo_app/images/uploaded_file.png')

        # st.markdown(
        #     """
        #     <style>
        #     div[data-testid="stAppViewContainer"]{
        #         position:fixed;
        #         bottom:18%;
        #         padding: 10px;
        #     }
        #     div[data-testid="stForm"]{
        #         position:fixed;
        #         right: 10%;
        #         left: 10%;
        #         bottom: 2%;
        #         border: 2px solid green;
        #         padding: 10px;
        #         z-index: 10;
        #     }
        #     </style>
        #     """, unsafe_allow_html=True
        # )

        col1, col2 = st.columns([2,1])
        with col1:
            #timeline = st.slider("See how you look in future (in months)", min_value=0, max_value=12, value=0, step=3)
            # left_co, cent_co,last_co = st.columns(3)
            # with left_co:
                if st.button("3 Months"):
                    image = (Image.open("./demo_app/mexicanman_before.png"))
                    #st.image(image)
                    set_background("./demo_app/mexicanman_before.png")
                if st.button("6 Months"):
                    image = (Image.open("./demo_app/mexicanman_1.png"))
                    #st.image(image)
                    set_background("./demo_app/mexicanman_1.png")
                if st.button("9 Months"):
                    image = (Image.open("./demo_app/mexicanman_2.png"))
                    #st.image(image)
                    set_background("./demo_app/mexicanman_2.png")
                if st.button("12 Months"):
                    image = (Image.open("./demo_app/mexicanman_3.png"))
                    #st.image(image)
                    set_background("./demo_app/mexicanman_3.png")
            
            # if timeline == 3:
            #     image = (Image.open("./demo_app/mexicanman_before.png"))
            #     #st.image(image)
            #     set_background("./demo_app/mexicanman_before.png")
            # if timeline == 6:
            #     image = (Image.open("./demo_app/mexicanman_1.png"))
            #     #st.image(image)
            #     set_background("./demo_app/mexicanman_1.png")
            # if timeline == 9:
            #     image = (Image.open("./demo_app/mexicanman_2.png"))
            #     #st.image(image)
            #     set_background("./demo_app/mexicanman_2.png")
            # if timeline == 12:
            #     image = (Image.open("./demo_app/mexicanman_3.png"))
            #     #st.image(image)
            #     set_background("./demo_app/mexicanman_3.png")
        with col2:
            with st.expander("Show Workout Plan"):
                st.write("Here is your customised workout plan")
            with st.expander("Show Meal Plan"):
                st.write("Here is your customized meal plan")
            
        
        #timeline = st.slider("See how you look in future (in months)", min_value=0, max_value=12, value=0, step=3)
        # if timeline == 3:
        #     image = (Image.open("./demo_app/mexicanman_before.png"))
        #     #st.image(image)
        #     set_background("./demo_app/mexicanman_before.png")
        # if timeline == 6:
        #     image = (Image.open("./demo_app/mexicanman_1.png"))
        #     #st.image(image)
        #     set_background("./demo_app/mexicanman_1.png")
        # if timeline == 9:
        #     image = (Image.open("./demo_app/mexicanman_2.png"))
        #     #st.image(image)
        #     set_background("./demo_app/mexicanman_2.png")
        # if timeline == 12:
        #     image = (Image.open("./demo_app/mexicanman_3.png"))
        #     #st.image(image)
        #     set_background("./demo_app/mexicanman_3.png")
