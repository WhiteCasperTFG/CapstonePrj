from helper_functions.utility import check_password  
from openai import OpenAI
import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import tiktoken
OPENAI_KEY = st.secrets["OPENAI_API_KEY"]
PASSWORD = st.secrets["password"]

# Check if the values are being loaded correctly
st.write("OpenAI API Key loaded successfully!")
st.write("Password loaded successfully!")
# # Check if the password is correct.  
# if not check_password():  
#     st.stop()

# if load_dotenv('.env'):
#    # for local development
#    OPENAI_KEY = os.getenv('OPENAI_API_KEY')
# else:
#    OPENAI_KEY = st.secrets['OPENAI_API_KEY']


# Pass the API Key to the OpenAI Client
client = OpenAI(api_key=OPENAI_KEY)
# Some other code here are omitted for brevity

# Title of the app
st.title("Streamlit Test App 2")

# Some basic text
st.write("Hello, welcome to this Streamlit test app!")

# Adding a button
if st.button('Click me'):
    st.write("Button clicked!")

# A slider
age = st.slider('Select your age', 0, 100, 25)
st.write(f"Your selected age is: {age}")

# Adding a text input field
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")