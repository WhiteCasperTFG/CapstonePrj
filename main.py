import streamlit as st

# Set page title and layout
st.set_page_config(page_title="HDB Resale Flat Eligibility Checker", layout="centered")

# Home Page title
st.title("HDB Resale Flat Eligibility Checker")

# Description of the app
st.write("""
Welcome to the HDB Resale Flat Eligibility Checker!
Use this tool to check your eligibility for buying an HDB flat in the resale market and discover available housing grants.
Please fill in the details below to get personalized information.
""")

# Input Form
with st.form("eligibility_form"):
    st.subheader("Enter Your Details")
    
    # Citizenship status
    citizenship = st.selectbox("Select your citizenship status:", 
                               options=["Singapore Citizen", "Permanent Resident"])
    
    # Household income
    income = st.number_input("Enter your household monthly income (SGD):", min_value=0, step=100)
    
    # Family nucleus status
    family_nucleus = st.selectbox("Do you have a family nucleus?", 
                                  options=["Yes", "No"])
    
    # Flat type
    flat_type = st.selectbox("Select the type of flat you are interested in:", 
                             options=["2-room", "3-room", "4-room", "5-room", "Executive"])
    
    # Submit button
    submit_button = st.form_submit_button("Check Eligibility")

# Process the form submission
if submit_button:
    st.subheader("Eligibility Results")
    
    # Check eligibility based on input (simplified logic for demo)
    if citizenship == "Singapore Citizen" and income < 14000 and family_nucleus == "Yes":
        st.success(f"You are eligible to buy an HDB resale flat and may qualify for grants based on your household income of ${income} and your choice of a {flat_type}.")
    elif citizenship == "Permanent Resident" and income < 14000 and family_nucleus == "Yes":
        st.warning(f"PR households may face restrictions when buying an HDB resale flat. Please visit the HDB website for more details.")
    else:
        st.error("You may not be eligible for grants or resale flat purchases. Please check HDB’s eligibility criteria.")
