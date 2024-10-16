import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import openai  # Make sure to install openai library
from dotenv import load_dotenv  # Import to load .env variables
from helper_functions.utility import check_password  


# Check if the password is correct.  
if not check_password():  
    st.stop()
    
# Load the .env file for local development
load_dotenv('.env')  # Load the environment variables from .env
OPENAI_KEY = os.getenv('OPENAI_API_KEY')  # Get the API key from the environment

# Pass the API Key to the OpenAI Client
openai.api_key = OPENAI_KEY  # Set the OpenAI API key

# Load grant amounts from CSV file
grant_data = pd.read_csv('data/grant_amounts.csv')

def get_llm_response(user_input):
    # Create the prompt for the model
    prompt = f"You are an assistant knowledgeable about HDB grants and home buying in Singapore. Answer the user's question: {user_input}"

    # Call the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or the model you're using
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # Extract and return the assistant's reply
    return response.choices[0].message['content']

# Function to calculate EHG (Enhanced CPF Housing Grant)
def calculate_ehg(income, marital_status):
    if marital_status == 'Single':
        if income <= 1500:
            return 40000
        elif income <= 2000:
            return 37500
        elif income <= 2500:
            return 35000
        elif income <= 3000:
            return 32500
        elif income <= 3500:
            return 30000
        elif income <= 4000:
            return 27500
        elif income <= 4500:
            return 25000
        elif income <= 5000:
            return 22500
        elif income <= 5500:
            return 20000
        elif income <= 6000:
            return 17500
        elif income <= 6500:
            return 15000
        elif income <= 7000:
            return 12500
        elif income <= 7500:
            return 10000
        elif income <= 8000:
            return 7500
        elif income <= 8500:
            return 5000
        elif income <= 9000:
            return 2500
        else:
            return 0
    elif marital_status == 'Married':
        if income <= 1500:
            return 80000
        elif income <= 2000:
            return 75000
        elif income <= 2500:
            return 70000
        elif income <= 3000:
            return 65000
        elif income <= 3500:
            return 60000
        elif income <= 4000:
            return 55000
        elif income <= 4500:
            return 50000
        elif income <= 5000:
            return 45000
        elif income <= 5500:
            return 40000
        elif income <= 6000:
            return 35000
        elif income <= 6500:
            return 30000
        elif income <= 7000:
            return 25000
        elif income <= 7500:
            return 20000
        elif income <= 8000:
            return 15000
        elif income <= 8500:
            return 10000
        elif income <= 9000:
            return 5000
        else:
            return 0
    else:
        return 0

# Function to calculate CPF Housing Grant
def calculate_cpf_grant(flat_size, first_time_buyer):
    if first_time_buyer == 'No':
        return 0  # Not eligible if not a first-time buyer

    # Get the grant amount based on the flat size
    grant_amount = grant_data.loc[grant_data['Flat Size'] == flat_size, 'CPF Housing Grant Amount']
    if not grant_amount.empty:
        return grant_amount.values[0]  # Return the grant amount as an integer
    return 0

# Function to calculate Proximity Housing Grant (PHG)
def calculate_phg(proximity, buying_with_family):
    if proximity == 'within 4km' and buying_with_family:
        return 20000  # Example PHG amount
    return 0

# Streamlit app interface
st.title("HDB Resale Grant Eligibility & Estimator")

# Step 1: Display Step-by-Step Process Flow
st.subheader("Buying Process Overview")
st.write("""\
1. **Check Eligibility for Grants**
2. **Determine Your Budget**
3. **Search for Available Flats**
4. **View and Shortlist Potential Flats**
5. **Make an Offer**
6. **Complete the Purchase Paperwork**
7. **Finalize the Financing**
8. **Move In**
""")

# Step 2: Input form for user details
st.subheader("Provide Your Details")

# Step 3: Marital Status
marital_status = st.selectbox("Marital Status", ['Married', 'Single'])

# Step 4: Citizenship based on marital status
citizenship = st.selectbox("Your Citizenship", ['Singaporean', 'Permanent Resident', 'Foreigner'])

# Show "Your Spouse's Citizenship" only if married
spouse_citizenship = None  # Initialize with None
if marital_status == 'Married':
    spouse_citizenship = st.selectbox("Your Spouse's Citizenship", ['Singaporean', 'Permanent Resident', 'Foreigner'])

# Step 5: Other relevant details
income = st.number_input("Household Monthly Income (SGD)", min_value=0, step=500)
flat_size = st.selectbox("Flat Type", ['4-room or smaller', '5-room', 'Executive'])
first_time_buyer = st.radio("Are you a first-time buyer?", ['Yes', 'No'])
proximity = st.radio("Do you live within 4km of your parents or children?", ['within 4km', 'more than 4km'])
buying_with_family = st.radio("Are you buying the flat with family (parents/children)?", ['Yes', 'No'])

# Submit button to process the inputs
if st.button("Check Eligibility"):
    # Ineligibility checks
    ineligible_reasons = []
    
    # Citizenship check
    if citizenship == 'Foreigner':
        ineligible_reasons.append("Foreigners are not eligible to buy HDB flats.")
    elif marital_status == 'Married' and spouse_citizenship == 'Foreigner':
        ineligible_reasons.append("Both buyers must be Singaporean citizens or Permanent Residents to qualify for grants.")

    # Income check
    income_limit = 8000  # Example limit for grant eligibility
    if income > income_limit:
        ineligible_reasons.append("Your household income exceeds the limit for grant eligibility.")
    
    # First-time buyer check
    if first_time_buyer == 'No':
        if flat_size != 'Other':
            ineligible_reasons.append("You are not eligible for the CPF Housing Grant as you're not a first-time buyer.")

        # Adjusted Family Grant ineligibility logic
        if marital_status == 'Married' and buying_with_family == 'No':
            ineligible_reasons.append("You are not eligible for the Family Grant as you must be purchasing with parents or children to qualify.")

    # Calculate grants if eligible
    if not ineligible_reasons:
        ehg = calculate_ehg(income, marital_status)
        cpf_grant = calculate_cpf_grant(flat_size, first_time_buyer)
        phg = calculate_phg(proximity, buying_with_family == 'Yes')

        # Display the results
        st.subheader("Grant Eligibility Results")
        
        if first_time_buyer == 'Yes':
            st.write(f"**CPF Housing Grant**: SGD {cpf_grant}")
        else:
            st.write("You are not eligible for the CPF Housing Grant as you're not a first-time buyer.")
        
        st.write(f"**Enhanced CPF Housing Grant (EHG)**: SGD {ehg}")
        st.write(f"**Proximity Housing Grant (PHG)**: SGD {phg}")

        total_grant = ehg + cpf_grant + phg
        st.write(f"**Total Estimated Grant Amount**: SGD {total_grant}")

        # Load EHG data from the CSV file
        ehg_data = pd.read_csv('data/Enhance_CPF_Housing_Grant_Data.csv')

        # Filter the data based on marital status
        if marital_status == 'Single':
            filtered_data = ehg_data[ehg_data['Marital Status'] == 'Single']
        else:
            filtered_data = ehg_data[ehg_data['Marital Status'] == 'Married']

        # Plotting the chart based on filtered data
        st.subheader("Grant Visualization")
        fig, ax = plt.subplots()
        ax.bar(filtered_data['Grant Type'], filtered_data['Amount (SGD)'])
        ax.set_title('Grant Distribution')
        ax.set_xlabel('Grant Type')
        ax.set_ylabel('Amount (SGD)')
        st.pyplot(fig)

        # Suggestions for optimizing eligibility
        if total_grant == 0:
            if income == 0:
                st.warning("You have a household income of SGD 0. You may still be eligible for some grants, especially if you are a first-time buyer. Consider reaching out to HDB for detailed assistance.")
            else:
                st.warning("You are not eligible for any grants. Consider adjusting your inputs (e.g., income, marital status) and check your eligibility again.")
        else:
            st.success("Congratulations! You are eligible for grants. Review your financial planning to maximize your benefits.")

        # Personalized Recommendations
        st.subheader("Personalized Recommendations")
        user_query = st.text_input("Ask for personalized advice (e.g., tips for buying a flat):")
        if user_query:
            recommendation = get_llm_response(user_query)
            st.write(recommendation)

        # Interactive Tutorials
        st.subheader("Interactive Tutorials")
        tutorial_topic = st.selectbox("Select a tutorial topic:", ["HDB Buying Process", "Grant Eligibility", "Financing Options"])
        if st.button("Get Tutorial"):
            tutorial_response = get_llm_response(f"Provide an interactive tutorial on {tutorial_topic}.")
            st.write(tutorial_response)

    else:
        st.error("You are not eligible for any grants:")
        for reason in ineligible_reasons:
            st.write(f"- {reason}")
