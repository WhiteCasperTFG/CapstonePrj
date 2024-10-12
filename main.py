import streamlit as st
import streamlit as st  
from helper_functions.utility import check_password  
from openai import OpenAI
import os
from dotenv import load_dotenv

# Check if the password is correct.  
if not check_password():  
    st.stop()

load_dotenv('proj.env')
os.environ['OPENAI_MODEL_NAME'] = "gpt-4o-mini"
API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_kley=API_KEY)

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