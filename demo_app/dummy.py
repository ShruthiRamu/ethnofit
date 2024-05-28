"""Python file to serve as the frontend"""
import sys
import os

sys.path.append(os.path.abspath('.'))

import streamlit as st
import time
from demo_app.components.sidebar import sidebar
import openai
import requests
from PIL import Image  

openai_api_key = "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"
openai_api_base = "https://api.openai.com/v1"
#image_dir = "/Users/macuser/Documents/GenAIProjects/ImageGeneration/demo_app/images"
image_dir = "./demo_app/images"
prompt = "A cyberpunk monkey hacker dreaming of a beautiful bunch of bananas, digital art"

# def load_chain():
#     """Logic for loading the chain you want to use should go here."""
#     llm = OpenAI(openai_api_key=st.session_state.get("OPENAI_API_KEY"), temperature=0)
#     chain = ConversationChain(llm=llm)
#     return chain


# def get_text():
#     input_text = st.text_input("You: ", "Hello, how are you?", key="input")
#     return input_text

def generate_image(user_input: str, imagesize: str ="1024x1024", num_images: int = 1):
   
    openai.api_type = "openai"
    openai.api_version = '2020-11-07'
    openai.api_key = openai_api_key
    openai.api_base = openai_api_base

    response = openai.images.generate(
                        prompt = user_input,
                        # prompt="Realistic fitness picture of indian man",
                        n=num_images,
                        size=imagesize)
    print("Response\n")
    print(response)
    image_url = response.data[0].url
    #image_urls = [data['url'] for data in response['data']]

    # save the images
    generate_urls = [datum.url for datum in response.data]  # extract URLs
    generate_images = [requests.get(url).content for url in generate_urls]  # download images
    generate_image_names = [f"generate_image_{i}.png" for i in range(len(generate_images))]  # create names
    generate_image_filepaths = [os.path.join(image_dir, name) for name in generate_image_names]  # create filepaths
    for image, filepath in zip(generate_images, generate_image_filepaths):  # loop through the variations
        with open(filepath, "wb") as image_file:  # open the file
            image_file.write(image)  # write the image to the file

    # print the generated image
    for generate_image_filepaths in generate_image_filepaths:
        print(generate_image_filepaths)
        image = (Image.open(generate_image_filepaths)) 
        st.image(image, caption='Generated Image')
        image.show()   
    
    return image_url

def create_image_variation(image_file: str, imagesize: str ="256x256", num_images: int = 1):
   
    openai.api_type = "openai"
    openai.api_version = '2020-11-07'
    openai.api_key = openai_api_key
    openai.api_base = openai_api_base

    response = openai.images.create_variation(
                        image=open(image_file, "rb"),
                        n=num_images,
                        size=imagesize)
    print("Response\n")
    print(response)
    image_url = response.data[0].url
    #image_urls = [data['url'] for data in response['data']]

    # save the images
    variation_urls = [datum.url for datum in response.data]  # extract URLs
    variation_images = [requests.get(url).content for url in variation_urls]  # download images
    variation_image_names = [f"variation_image_{i}.png" for i in range(len(variation_images))]  # create names
    variation_image_filepaths = [os.path.join(image_dir, name) for name in variation_image_names]  # create filepaths
    for image, filepath in zip(variation_images, variation_image_filepaths):  # loop through the variations
        with open(filepath, "wb") as image_file:  # open the file
            image_file.write(image)  # write the image to the file

    # print the original image
    print("Original Image : /Users/macuser/Documents/GenAIProjects/ImageGeneration/demo_app/johndoe.png")
    #image = (Image.open("/Users/macuser/Documents/GenAIProjects/ImageGeneration/demo_app/johndoe.png"))
    image = (Image.open("./demo_app/johndoe.png"))
    image.show()

    # print the new variations
    for variation_image_filepaths in variation_image_filepaths:
        print(variation_image_filepaths)
        image = (Image.open(variation_image_filepaths)) 
        image.show()   
    
    return image_url


def edit_image(image_file: str, imagesize: str ="256x256", num_images: int = 1):
   
    openai.api_type = "openai"
    openai.api_version = '2020-11-07'
    openai.api_key = openai_api_key
    openai.api_base = openai_api_base

    # create a mask
    width = 852
    height = 946
    mask = Image.new("RGBA", (width, height), (0, 0, 0, 1))  # create an opaque image mask

    # set the bottom half to be transparent
    for x in range(width):
        for y in range(height // 2, height):  # only loop over the bottom half of the mask
            # set alpha (A) to zero to turn pixel transparent
            alpha = 0
            mask.putpixel((x, y), (0, 0, 0, alpha))

    # save the mask
    mask_name = "bottom_half_mask.png"
    print("image_dir: " + image_dir)
    mask_filepath = os.path.join(image_dir, mask_name)
    print("os.path.join(image_dir, mask_name) = " + mask_filepath)
    mask.save(mask_filepath)

    response = openai.images.edit(
                        image=open(image_file, "rb"),
                        mask = open(mask_filepath, "rb"),
                        prompt="An indian man without shirt in his 30's who is fit and healthy",
                        n=num_images,
                        size=imagesize)
    print("Response\n")
    print(response)
    image_url = response.data[0].url
    #image_urls = [data['url'] for data in response['data']]

    # save the images
    edit_urls = [datum.url for datum in response.data]  # extract URLs
    edit_images = [requests.get(url).content for url in edit_urls]  # download images
    edit_image_names = [f"edit_image_{i}.png" for i in range(len(edit_images))]  # create names
    edit_image_filepaths = [os.path.join(image_dir, name) for name in edit_image_names]  # create filepaths
    for image, filepath in zip(edit_images, edit_image_filepaths):  # loop through the variations
        with open(filepath, "wb") as image_file:  # open the file
            image_file.write(image)  # write the image to the file

    # print the original image
    print("Original Image : /Users/macuser/Documents/GenAIProjects/ImageGeneration/demo_app/manbefore.png")
    #image = (Image.open("/Users/macuser/Documents/GenAIProjects/ImageGeneration/demo_app/johndoe.png"))
    image = (Image.open("./demo_app/manbefore.png"))
    st.image(image, caption='Original Image')
    image.show()

    # print the new variations
    for edit_image_filepaths in edit_image_filepaths:
        print(edit_image_filepaths)
        image = (Image.open(edit_image_filepaths)) 
        st.image(image, caption='Edited Image')
        image.show()   
    
    return image_url

if __name__ == "__main__":

    st.set_page_config(
        page_title="EthnoFit: Demo",
        page_icon=":biceps:",
        layout="wide",
        initial_sidebar_state="expanded", )
    st.header("EthnoFit")
    sidebar()

    if not st.session_state.get("open_api_key_configured"):
        st.error("Please configure your API Keys!")
    else:

        # imagefile="./demo_app/manbefore.png"
        # image_url = generate_image(imagefile)
        # print("Response Image URL = " +  image_url)

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
                    full_response = generate_image(user_input)
                # Simulate stream of response with milliseconds delay
                # for chunk in assistant_response.split():
                #     full_response += chunk + " "
                #     time.sleep(0.05)
                #     # Add a blinking cursor to simulate typing
                #     message_placeholder.markdown(full_response + "▌")
                    message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        
        #imagefile="/Users/macuser/Documents/GenAIProjects/ImageGeneration/demo_app/johndoe.png"
        #imagefile="./demo_app/johndoe.png"
        #image_url = create_image_variation(imagefile)
        #image_url = edit_image(imagefile)
        #print("Response Image URL = " +  image_url)
        #for image_url in image_urls:
        #    print(image_url)