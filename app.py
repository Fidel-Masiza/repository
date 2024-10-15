import os
from dotenv import load_dotenv
import streamlit as st
import requests

# Load environment variables from .env file
load_dotenv()

# Retrieve the Hugging Face API key from environment variables
HUGGING_FACE_API_KEY = os.getenv("HUGGING_FACE_API_KEY")

# Function to get responses from Hugging Face model
def get_hugging_face_response(question):
    # Specify the model endpoint (you can change this to any supported model)
    API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"
    
    headers = {"Authorization": f"Bearer {HUGGING_FACE_API_KEY}"}
    payload = {"inputs": question}

    response = requests.post(API_URL, headers=headers, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.json()}

# Initialize our Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

input_text = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# If ask button is clicked
if submit:
    response = get_hugging_face_response(input_text)
    st.subheader("The Response is")
    
    # Display the response or error message
    if "error" in response:
        st.write(f"Error: {response['error']}")
    else:
        st.write(response)