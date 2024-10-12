import streamlit as st

# Title of the app
st.title("Streamlit Test App")

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