import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Homepage", page_icon="🏠")

# Use a background image
background_image = "images/homepage.jpg"
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
        if st.button("Eligibility", key="eligibility"):
            st.session_state.page = "eligibility"  # Set the page to eligibility
        if st.button("Grant Calculator", key="calc"):
            st.session_state.page = "calculator"  # Set the page to the calculator
        if st.button("Button 3", key="button3"):
            st.session_state.page = "button3"
        if st.button("Button 4", key="button4"):
            st.session_state.page = "button4"

# Display content based on the selected page
if 'page' in st.session_state:
    if st.session_state.page == "eligibility":
        st.experimental_rerun()  # Refresh to show eligibility page
    elif st.session_state.page == "calculator":
        st.write("Welcome to the Grant Calculator!")
        # Include the calculator functionality here.
    elif st.session_state.page == "button3":
        st.write("You clicked Button 3!")
    elif st.session_state.page == "button4":
        st.write("You clicked Button 4!")
