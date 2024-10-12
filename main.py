import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Homepage", page_icon="🏠")

# Specify the path to the background image
background_image = "image/homepage.jpg"  # Ensure this path is correct relative to your project structure

# Add custom CSS for the background image
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url({background_image});
        background-size: cover; /* Cover the entire area */
        background-repeat: no-repeat; /* No repeating */
        background-attachment: fixed; /* Fixed background */
        height: 100vh; /* Full viewport height */
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Create a title for the app
st.title("Welcome to the Grant Application Portal")

# Create buttons
st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
if st.button("Grant Calculator"):
    st.session_state.page = "grant_calculator"
    st.experimental_rerun()
if st.button("Eligibility"):
    st.session_state.page = "eligibility"
    st.experimental_rerun()
if st.button("Button 3"):
    st.session_state.page = "button3"
    st.experimental_rerun()
if st.button("Button 4"):
    st.session_state.page = "button4"
    st.experimental_rerun()
st.markdown('</div>', unsafe_allow_html=True)

# Check which page to display
if 'page' not in st.session_state:
    st.session_state.page = 'homepage'

if st.session_state.page == 'eligibility':
    st.write("Welcome to the Eligibility Page!")
    # Include eligibility logic here
elif st.session_state.page == 'grant_calculator':
    st.write("Welcome to the Grant Calculator!")
    # Include calculator logic here
elif st.session_state.page == 'button3':
    st.write("You clicked Button 3!")
elif st.session_state.page == 'button4':
    st.write("You clicked Button 4!")
else:
    st.write("Welcome to the Homepage!")

