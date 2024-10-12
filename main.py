import streamlit as st

# Function to calculate Enhanced CPF Housing Grant (EHG) based on income
def calculate_ehg(income):
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

# Function to calculate CPF Housing Grant based on flat size
def calculate_cpf_grant(flat_size):
    if flat_size == '4-room or smaller':
        return 50000
    elif flat_size == '5-room':
        return 40000
    else:
        return 0

# Function to calculate Proximity Housing Grant based on distance
def calculate_phg(proximity):
    if proximity == 'within 4km':
        return 30000
    else:
        return 0

# Streamlit app interface
st.title("HDB Resale Grant Eligibility & Estimator")

# Input form for user details
with st.form("grant_form"):
    st.subheader("Provide Your Details")
    income = st.number_input("Household Monthly Income (SGD)", min_value=0, step=500)
    flat_size = st.selectbox("Flat Type", ['4-room or smaller', '5-room', 'Other'])
    first_time_buyer = st.radio("Are you a first-time buyer?", ['Yes', 'No'])
    proximity = st.radio("Do you live within 4km of your parents or children?", ['within 4km', 'more than 4km'])
    submit = st.form_submit_button("Check Eligibility")

# If the form is submitted, calculate eligibility and grants
if submit:
    # Calculate the grants
    ehg = calculate_ehg(income)
    cpf_grant = calculate_cpf_grant(flat_size)
    phg = calculate_phg(proximity)

    # Display the results
    st.subheader("Grant Eligibility Results")
    if first_time_buyer == 'Yes':
        st.write(f"**CPF Housing Grant**: SGD {cpf_grant}")
    else:
        st.write("You are not eligible for the CPF Housing Grant (for resale flats) as you're not a first-time buyer.")
    
    st.write(f"**Enhanced CPF Housing Grant (EHG)**: SGD {ehg}")
    st.write(f"**Proximity Housing Grant (PHG)**: SGD {phg}")
    
    total_grant = ehg + cpf_grant + phg
    st.write(f"**Total Estimated Grant Amount**: SGD {total_grant}")

    # Suggestions for optimizing eligibility
    if total_grant == 0:
        st.warning("You are not eligible for any grants. Consider adjusting your inputs (e.g., income, proximity) to see how it affects grant eligibility.")
    else:
        st.success(f"Based on your input, you could receive up to SGD {total_grant} in grants for your HDB resale flat purchase.")
