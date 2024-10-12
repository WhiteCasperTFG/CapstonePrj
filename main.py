import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    if flat_size == '4-room or smaller':
        return 50000  # Example grant for 4-room flats
    elif flat_size == '5-room':
        return 30000  # Example grant for 5-room flats
    else:
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
st.write("""
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
flat_size = st.selectbox("Flat Type", ['4-room or smaller', '5-room', 'Other'])
first_time_buyer = st.radio("Are you a first-time buyer?", ['Yes', 'No'])
proximity = st.radio("Do you live within 4km of your parents or children?", ['within 4km', 'more than 4km'])
buying_with_family = st.radio("Are you buying the flat with family (parents/children)?", ['Yes', 'No'])

# Step 6: Display Grant Eligibility Criteria Visuals
st.subheader("Grant Eligibility Criteria")
st.write("### Enhanced CPF Housing Grant (EHG) Amounts based on Monthly Household Income:")

# Load EHG data from CSV file
ehg_data = pd.read_csv('ehg_data.csv')

# Extract income and EHG data from the DataFrame
income_brackets = ehg_data['Income'].values
ehg_single = ehg_data['Single_EHG'].values
ehg_married = ehg_data['Married_EHG'].values

# Create a bar chart
fig, ax = plt.subplots(figsize=(10, 6))
width = 0.35  # the width of the bars

# Bar positions
x_single = np.arange(len(income_brackets))
x_married = x_single + width

# Plotting the bars
bars1 = ax.bar(x_single, ehg_single, width, label='Single', color='blue')
bars2 = ax.bar(x_married, ehg_married, width, label='Married', color='green')

# Adding labels and title
ax.set_xlabel('Monthly Household Income (SGD)')
ax.set_ylabel('Enhanced CPF Housing Grant Amount (SGD)')
ax.set_title('Enhanced CPF Housing Grant Amounts by Income Bracket')
ax.set_xticks(x_single + width / 2)
ax.set_xticklabels(income_brackets)
ax.legend()

# Annotate bars with values
for bar in bars1:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval}', ha='center', va='bottom')

for bar in bars2:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval}', ha='center', va='bottom')

# Display the chart in Streamlit
st.pyplot(fig)

# Step 7: Submit button to process the inputs
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
    else:
        # Display ineligibility reasons
        st.warning("You are not eligible for the following reasons:")
        for reason in ineligible_reasons:
            st.write(f"- {reason}")

# Step 8: Display Financial Calculators
st.subheader("Financial Calculators")

# Example calculator for estimating monthly mortgage payments
st.write("### Estimate Your Monthly Mortgage Payment")
principal = st.number_input("Loan Amount (SGD)", min_value=0, step=5000)
interest_rate = st.number_input("Interest Rate (Annual %)", min_value=0.0, max_value=100.0, step=0.1)
loan_term = st.number_input("Loan Term (Years)", min_value=1, max_value=30, step=1)

# Calculate and display monthly payment
if st.button("Calculate Monthly Payment"):
    monthly_interest_rate = interest_rate / 100 / 12
    months = loan_term * 12
    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -months)
    st.success(f"Estimated Monthly Payment: SGD {monthly_payment:.2f}")

# Comparison Chart
st.subheader("Comparison of Grants")
comparison_data = {
    "Grant Type": ["Enhanced CPF Housing Grant (EHG)", "CPF Housing Grant", "Proximity Housing Grant (PHG)"],
    "Eligibility": ["Based on income", "First-time buyer", "Based on proximity"],
    "Amount (SGD)": [ehg, cpf_grant, phg]
}
comparison_df = pd.DataFrame(comparison_data)
st.write(comparison_df)

# Suggestions for further information
st.subheader("Need More Information?")
st.write("""
- Visit the [HDB Official Website](https://www.hdb.gov.sg) for more details on eligibility criteria and grants.
- Consult with a financial advisor for personalized financial planning.
""")
