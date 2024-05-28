import streamlit as st
from PIL import Image
import numpy as np
from demo_app.components.faq import faq
import main

image_dir = "./demo_app/images"

def fitness_sidebar():
    with st.sidebar:
        if not st.session_state.get("open_api_key_configured"):
            st.error("Please configure your Open API key!")
        else:
            uploaded_files = st.file_uploader("Upload your fitness images", accept_multiple_files=True)
            for uploaded_file in uploaded_files:
                im = Image.open(uploaded_file)
                image = np.array(im)
                st.image(image)
                st.write("Image Uploaded Successfully")
                #im.save("uploaded_file.png")
            
            calorie_intake_input = st.text_input(
                "Calorie Tracker",
                placeholder="Link to your apple/fitbit",
            )

            workout_tracker = st.text_input(
                "Workout(in minutes)",
                placeholder="Link to your apple/fitbit"
            )

            sex = st.selectbox(
                "Sex", 
                ("Female", "Male"),
                placeholder="Link to your apple/fitbit"
            )

            height = st.text_input(
                "Height(in cm)", 
                placeholder="Link to your apple/fitbit"
            )

            weight = st.text_input(
                "Weight(in lb)", 
                placeholder="Link to your apple/fitbit"
            )

            bmi = st.text_input(
                "BMI", 
                placeholder="Link to your apple/fitbit"
            )

            if "messages" not in st.session_state:
                st.session_state["messages"] = [
                {"role": "assistant", "content": "How can I help you?"}]
        
            # Display chat messages from history on app rerun
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])
            
            if user_input := st.chat_input("Message EthnoFit"):
                # Add user message to chat history
                st.session_state.messages.append({"role": "user", "content": user_input})
                # Display user message in chat message container
                with st.chat_message("user"):
                    st.markdown(user_input)

                with st.chat_message("assistant"):
                    message_placeholder = st.empty()
                    full_response = ""

                with st.chat_message("assistant"):
                    message_placeholder = st.empty()
                    full_response = ""

                    with st.spinner('CHAT-BOT is at Work ...'):
                        # assistant_response = openai.chat.completions.create(model="dall-e-3",
                        #                             messages=[{"role": "user", "content": user_input}])
                        full_response = main.generate_image(user_input)
                    # Simulate stream of response with milliseconds delay
                    # for chunk in assistant_response.split():
                    #     full_response += chunk + " "
                    #     time.sleep(0.05)
                    #     # Add a blinking cursor to simulate typing
                    #     message_placeholder.markdown(full_response + "▌")
                        message_placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
        
        #faq()