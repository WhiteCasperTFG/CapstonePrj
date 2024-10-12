import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Homepage", page_icon="🏠")

# Use a background image
background_image = "images/homepage.jpg"

# Add custom CSS for the background image and button styling
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url({background_image});
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    .button-container {{
        display: flex;
        flex-direction: column;
        gap: 20px; /* Spacing between buttons */
        align-items: center; /* Center buttons horizontally */
    }}

    .stButton {{
        width: 200px; /* Set a fixed width for buttons */
        height: 50px; /* Set a fixed height for buttons */
        font-size: 20px; /* Increase font size */
        background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent white */
        border-radius: 10px; /* Rounded corners */
        border: none; /* Remove border */
        cursor: pointer; /* Change cursor to pointer */
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Create a title for the app
st.title("Welcome to the Grant Application Portal")

# Create a container for the buttons
with st.container():
    button_container = st.empty()
    with button_container:
        # Create the button container div with the button-container class
        button_html = """
        <div class="button-container">
            <button class="stButton" onclick="window.location.href='/grant-calculator'">Grant Calculator</button>
            <button class="stButton" onclick="window.location.href='/eligibility'">Eligibility</button>
            <button class="stButton" onclick="window.location.href='/button3'">Button 3</button>
            <button class="stButton" onclick="window.location.href='/button4'">Button 4</button>
        </div>
        """
        st.markdown(button_html, unsafe_allow_html=True)

# Display content based on the selected page
if 'page' in st.session_state:
    if st.session_state.page == "grant-calculator":
        st.write("Welcome to the Grant Calculator!")
        # Include the calculator functionality here.
    elif st.session_state.page == "eligibility":
        st.write("Eligibility information goes here!")
    elif st.session_state.page == "button3":
        st.write("You clicked Button 3!")
    elif st.session_state.page == "button4":
        st.write("You clicked Button 4!")
